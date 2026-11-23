"""Costruisce i file GeoJSON integrali del FVG a partire dai dati scaricati.

Uso: python3 costruisci.py CARTELLA_LAVORO CARTELLA_DATI [id ...]

CARTELLA_LAVORO contiene fonti/regione (pagine WFS), osm_out e intermedi (file .jsonl).
Scrive CARTELLA_DATI/integrale/<gruppo>/<id>.geojson e CARTELLA_DATI/indice_integrale.json.
I livelli troppo pesanti vengono divisi per comune o per ex provincia.
"""
import collections
import json
import pathlib
import sys

import numpy as np
import shapely
from shapely.geometry import shape

QUI = pathlib.Path(__file__).parent
PRECISIONE = 7                      # sette decimali di grado: circa un centimetro
SOGLIA_DIVISIONE_BYTE = 45_000_000  # oltre questa misura il livello viene diviso
LIMITE_PARTE_BYTE = 70_000_000     # una parte più pesante viene spezzata in blocchi
DIVISI_PER_COMUNE = {"edifici", "numeri_civici"}
SIGLE = {"030": "UD", "031": "GO", "032": "TS", "093": "PN"}
FONTI = {
    "REGIONE": {
        "nome": "Regione autonoma Friuli Venezia Giulia, catalogo IRDAT (Infrastruttura regionale di dati ambientali e territoriali)",
        "indirizzo": "https://irdat.regione.fvg.it/",
    },
    "ISTAT": {
        "nome": "ISTAT (Istituto nazionale di statistica), confini delle unità amministrative al 1 gennaio 2026",
        "indirizzo": "https://www.istat.it/notizia/confini-delle-unita-amministrative-a-fini-statistici-al-1-gennaio-2018-2/",
    },
    "ISTAT_CENS": {
        "nome": "ISTAT (Istituto nazionale di statistica), basi territoriali del censimento 2021, distribuite dalla Regione FVG; perimetri ottenuti unendo le sezioni di censimento",
        "indirizzo": "https://www.istat.it/notizia/basi-territoriali-e-variabili-censuarie/",
    },
    "ENTI": {
        "nome": "Perimetri ottenuti unendo i comuni della Regione FVG (catalogo IRDAT) secondo la composizione ufficiale di ogni ente, indicata nei campi fonte_composizione e indirizzo_fonte",
        "indirizzo": "https://irdat.regione.fvg.it/",
    },
    "OSM": {
        "nome": "OpenStreetMap e contributori",
        "indirizzo": "https://www.openstreetmap.org/copyright",
    },
    "GISCO": {
        "nome": "Eurostat GISCO, unità amministrative locali 2024, © EuroGeographics per i confini amministrativi",
        "indirizzo": "https://ec.europa.eu/eurostat/web/gisco/geodata/statistical-units/local-administrative-units",
    },
    "COPERNICUS": {
        "nome": "Copernicus DEM GLO-30, © DLR e.V. 2010-2014 e © Airbus Defence and Space GmbH 2014-2018, fornito nell'ambito di COPERNICUS dall'Unione europea e dall'ESA (Agenzia spaziale europea)",
        "indirizzo": "https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM",
    },
}


def leggi_catalogo():
    """Restituisce le voci dei tre cataloghi: id, gruppo, titolo, fonte, origine."""
    voci = []
    for nome, fonte in (("catalogo_regione.txt", "REGIONE"), ("catalogo_osm.txt", "OSM"), ("catalogo_altri.txt", None)):
        for riga in (QUI / nome).read_text(encoding="utf8").splitlines():
            if not riga or riga.startswith("#"):
                continue
            campi = riga.split("|")
            voce = {"id": campi[0], "gruppo": campi[1], "titolo": campi[2], "fonte": fonte or campi[3]}
            if fonte == "REGIONE":
                voce["livello_origine"] = campi[3]
            voci.append(voce)
    return voci


def elementi_grezzi(voce, lavoro):
    """Genera gli elementi GeoJSON di un livello, qualunque sia la sua origine."""
    if voce["fonte"] == "REGIONE" and "livello_origine" in voce:
        cartella = lavoro / "fonti" / "regione" / voce["id"]
        if not (cartella / "FATTO.json").exists():
            raise FileNotFoundError(f"scaricamento non completato: {voce['id']}")
        for pagina in sorted(cartella.glob("pagina_*.json")):
            yield from json.loads(pagina.read_text(encoding="utf8"))["features"]
        return
    cartella = "osm_out" if voce["id"].startswith("osm_") else "intermedi"
    percorso = lavoro / cartella / f"{voce['id']}.jsonl"
    if not percorso.exists():
        raise FileNotFoundError(str(percorso))
    with open(percorso, encoding="utf8") as f:
        for riga in f:
            yield json.loads(riga)


def arrotonda(coordinate):
    if not coordinate:
        return coordinate
    if isinstance(coordinate[0], (int, float)):
        return [round(coordinate[0], PRECISIONE), round(coordinate[1], PRECISIONE)]
    return [arrotonda(c) for c in coordinate]


def normalizza(elemento):
    """Toglie la quota, arrotonda le coordinate ed elimina gli attributi vuoti."""
    geometria = elemento.get("geometry")
    if not geometria or not geometria.get("coordinates"):
        return None
    proprieta = {k: v for k, v in (elemento.get("properties") or {}).items() if v not in (None, "")}
    return {"type": "Feature", "properties": proprieta,
            "geometry": {"type": geometria["type"], "coordinates": arrotonda(geometria["coordinates"])}}


class Ripartitore:
    """Assegna ogni elemento a un comune tramite un suo punto interno."""

    def __init__(self, lavoro):
        comuni = [normalizza(e) for e in elementi_grezzi({"id": "comuni", "fonte": "REGIONE", "livello_origine": ""}, lavoro)]
        self.codici = [c["properties"]["COD_ISTAT"] for c in comuni]
        self.nomi = {c["properties"]["COD_ISTAT"]: c["properties"]["NOME"] for c in comuni}
        self.sagome = np.array([shapely.make_valid(shape(c["geometry"])) for c in comuni])
        self.albero = shapely.STRtree(self.sagome)

    def comune(self, geometria):
        forma = shape(geometria)
        try:
            punto = shapely.point_on_surface(forma)
        except shapely.errors.GEOSException:
            punto = shapely.centroid(shapely.make_valid(forma))  # geometria irregolare
        if punto.is_empty:
            punto = shapely.centroid(forma)
        trovati = self.albero.query(punto, predicate="intersects")
        if len(trovati) == 0:
            trovati = [self.albero.nearest(punto)]
        return self.codici[int(trovati[0])]


def scrivi_raccolta(percorso, voce, elementi, parte=None):
    """Scrive una raccolta GeoJSON con un elemento per riga e i metadati in testa."""
    percorso.parent.mkdir(parents=True, exist_ok=True)
    testata = {"type": "FeatureCollection", "name": percorso.stem, "titolo": voce["titolo"],
               "gruppo": voce["gruppo"], "fonte": FONTI[voce["fonte"]]["nome"]}
    if parte:
        testata["parte"] = parte
    with open(percorso, "w", encoding="utf8") as f:
        f.write(json.dumps(testata, ensure_ascii=False)[:-1] + ', "features": [\n')
        for indice, riga in enumerate(elementi):
            f.write(("" if indice == 0 else ",\n") + riga)
        f.write("\n]}\n")
    return percorso.stat().st_size


def spezza(righe):
    """Divide un gruppo di righe in blocchi che restano sotto il limite di peso per file."""
    peso = sum(len(r.encode("utf8")) for r in righe)
    blocchi = -(-peso // LIMITE_PARTE_BYTE)
    passo = -(-len(righe) // blocchi)
    return [righe[i:i + passo] for i in range(0, len(righe), passo)]


def costruisci_livello(voce, lavoro, dati, ripartitore):
    righe, tipi, campi = [], collections.Counter(), collections.Counter()
    riquadro = [180.0, 90.0, -180.0, -90.0]
    geometrie = []
    for grezzo in elementi_grezzi(voce, lavoro):
        elemento = normalizza(grezzo)
        if elemento is None:
            continue
        tipi[elemento["geometry"]["type"]] += 1
        campi.update(elemento["properties"].keys())
        geometrie.append(elemento["geometry"])
        righe.append(json.dumps(elemento, ensure_ascii=False, separators=(",", ":")))
    if not righe:
        raise ValueError(f"{voce['id']}: nessun elemento")
    limiti = shapely.bounds(shapely.from_geojson([json.dumps(g) for g in geometrie], on_invalid="ignore"))
    limiti = limiti[~np.isnan(limiti).any(axis=1)]
    riquadro = [round(float(limiti[:, 0].min()), 5), round(float(limiti[:, 1].min()), 5),
                round(float(limiti[:, 2].max()), 5), round(float(limiti[:, 3].max()), 5)]
    base = dati / "integrale" / voce["gruppo"]
    peso = sum(len(r.encode("utf8")) for r in righe)
    file = []
    if voce["id"] in DIVISI_PER_COMUNE or peso > SOGLIA_DIVISIONE_BYTE:
        per_comune = voce["id"] in DIVISI_PER_COMUNE
        gruppi = collections.defaultdict(list)
        for riga, geometria in zip(righe, geometrie):
            codice = ripartitore.comune(geometria)
            gruppi[codice if per_comune else SIGLE[codice[:3]]].append(riga)
        for chiave in sorted(gruppi):
            nome = f"{chiave} {ripartitore.nomi[chiave]}" if per_comune else chiave
            blocchi = spezza(gruppi[chiave])
            for numero, blocco in enumerate(blocchi, 1):
                suffisso = f"_{numero}" if len(blocchi) > 1 else ""
                parte = nome + (f", parte {numero} di {len(blocchi)}" if suffisso else "")
                percorso = base / voce["id"] / f"{voce['id']}_{chiave}{suffisso}.geojson"
                misura = scrivi_raccolta(percorso, voce, blocco, parte)
                file.append({"percorso": str(percorso.relative_to(dati)), "parte": parte,
                             "elementi": len(blocco), "byte": misura})
    else:
        percorso = base / f"{voce['id']}.geojson"
        misura = scrivi_raccolta(percorso, voce, righe)
        file.append({"percorso": str(percorso.relative_to(dati)), "elementi": len(righe), "byte": misura})
    scheda = {k: voce[k] for k in ("id", "gruppo", "titolo")}
    scheda.update({"fonte": voce["fonte"], "livello_origine": voce.get("livello_origine"),
                   "elementi": len(righe), "geometrie": dict(tipi), "riquadro": riquadro,
                   "campi": [c for c, _ in campi.most_common(40)], "file": file})
    return scheda


def salva_indice(schede, percorso_indice):
    """Scrive l'indice nell'ordine dei cataloghi; va richiamato dopo ogni livello."""
    ordine = [v["id"] for v in leggi_catalogo()]
    elenco = [schede[i] for i in ordine if i in schede]
    percorso_indice.parent.mkdir(parents=True, exist_ok=True)
    percorso_indice.write_text(json.dumps({"fonti": FONTI, "livelli": elenco}, ensure_ascii=False, indent=1), encoding="utf8")
    return elenco


def principale():
    lavoro, dati = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    scelti = set(sys.argv[3:])
    percorso_indice = dati / "indice_integrale.json"
    schede = {}
    if percorso_indice.exists():
        schede = {s["id"]: s for s in json.loads(percorso_indice.read_text(encoding="utf8"))["livelli"]}
    ripartitore = Ripartitore(lavoro)
    mancanti = []
    for voce in leggi_catalogo():
        if scelti and voce["id"] not in scelti:
            continue
        if not scelti and voce["id"] in schede:
            continue
        try:
            schede[voce["id"]] = costruisci_livello(voce, lavoro, dati, ripartitore)
            salva_indice(schede, percorso_indice)
            s = schede[voce["id"]]
            print(voce["id"], s["elementi"], len(s["file"]), sum(f["byte"] for f in s["file"]) // 1000, "kB", flush=True)
        except (FileNotFoundError, ValueError) as errore:
            mancanti.append(voce["id"])
            print("MANCA", voce["id"], errore, flush=True)
    elenco = salva_indice(schede, percorso_indice)
    print("Livelli costruiti:", len(elenco), "Mancanti:", mancanti)


if __name__ == "__main__":
    principale()
