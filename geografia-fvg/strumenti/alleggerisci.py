"""Produce la versione alleggerita dei livelli, il file unico e l'indice finale.

Uso: python3 alleggerisci.py CARTELLA_DATI [id ...]

Legge CARTELLA_DATI/indice_integrale.json e, con mapshaper, scrive
CARTELLA_DATI/leggero/<gruppo>/<id>.geojson, CARTELLA_DATI/fvg_unico.geojson
e CARTELLA_DATI/indice.json. Con l'opzione --unico-completo scrive anche
fvg_unico_completo.geojson, che riunisce tutti i livelli alleggeriti (centinaia di megabyte).
"""
import json
import pathlib
import subprocess
import sys
import tempfile

from costruisci import FONTI, scrivi_raccolta

PRECISIONE = "0.00001"               # cinque decimali di grado: circa un metro
INTERVALLO_M = 10                    # tolleranza di semplificazione ordinaria
INTERVALLO_PESANTI_M = 25            # tolleranza per i livelli oltre la soglia
SOGLIA_PESANTE_BYTE = 15_000_000
SENZA_LEGGERO = {"edifici", "numeri_civici", "osm_edifici"}   # già essenziali: si usa il file integrale
FILTRI = {"curve_livello": 'tipo == "direttrice"'}
SOGLIA_FILE_UNICO_BYTE = 2_500_000   # il file unico pubblicato accoglie i livelli fino a questo peso
NOME_UNICO, NOME_UNICO_COMPLETO = "fvg_unico.geojson", "fvg_unico_completo.geojson"


def alleggerisci_file(origine, destinazione_temporanea, puntuale, intervallo, filtro):
    comando = ["mapshaper-xl", "8gb", str(origine)]
    if filtro:
        comando += ["-filter", filtro]
    if not puntuale:
        comando += ["-simplify", f"interval={intervallo}", "keep-shapes"]
    comando += ["-o", str(destinazione_temporanea), "format=geojson", "ndjson", f"precision={PRECISIONE}", "force"]
    esito = subprocess.run(comando, capture_output=True, text=True)
    # Con geometrie miste mapshaper scrive un file per tipo (suffissi -point, -polyline, -polygon).
    prodotti = sorted(destinazione_temporanea.parent.glob(destinazione_temporanea.stem + "*.json"))
    if esito.returncode != 0 or not prodotti:
        raise RuntimeError(f"mapshaper non riuscito su {origine}: {esito.stderr[-400:]}")
    righe = (riga_elemento(r) for p in prodotti for r in p.read_text(encoding="utf8").split("\n") if r)
    return [r for r in righe if r]


def riga_elemento(riga):
    """Riscrive una riga di mapshaper come elemento completo, con le proprietà prima della geometria."""
    oggetto = json.loads(riga)
    if oggetto.get("type") != "Feature":      # livello senza attributi: mapshaper scrive la sola geometria
        oggetto = {"properties": {}, "geometry": oggetto}
    if not (oggetto.get("geometry") or {}).get("coordinates"):           # forma più corta di un metro, svanita con l'arrotondamento
        return None
    elemento = {"type": "Feature", "properties": oggetto.get("properties") or {}, "geometry": oggetto["geometry"]}
    return json.dumps(elemento, ensure_ascii=False, separators=(",", ":"))


def alleggerisci_livello(scheda, dati, rifare):
    if scheda["id"] in SENZA_LEGGERO:
        return [dict(f) for f in scheda["file"]]
    puntuale = set(scheda["geometrie"]) <= {"Point", "MultiPoint"}
    peso = sum(f["byte"] for f in scheda["file"])
    intervallo = INTERVALLO_PESANTI_M if peso > SOGLIA_PESANTE_BYTE else INTERVALLO_M
    percorso = dati / "leggero" / scheda["gruppo"] / f"{scheda['id']}.geojson"
    if percorso.exists() and not rifare:
        with open(percorso, encoding="utf8") as f:
            elementi = sum(1 for riga in f if riga.startswith('{"type":"Feature"'))
        return [{"percorso": str(percorso.relative_to(dati)), "elementi": elementi, "byte": percorso.stat().st_size}]
    righe = []
    with tempfile.TemporaryDirectory() as cartella:
        for indice, file in enumerate(scheda["file"]):
            temporaneo = pathlib.Path(cartella) / f"parte_{indice}.json"
            righe += alleggerisci_file(dati / file["percorso"], temporaneo, puntuale, intervallo,
                                       FILTRI.get(scheda["id"]))
    voce = {"titolo": scheda["titolo"], "gruppo": scheda["gruppo"], "fonte": scheda["fonte"]}
    misura = scrivi_raccolta(percorso, voce, righe)
    return [{"percorso": str(percorso.relative_to(dati)), "elementi": len(righe), "byte": misura}]


def scrivi_file_unico(schede, dati, completo=False):
    """Riunisce i livelli alleggeriti in una sola raccolta; ogni elemento porta livello, gruppo e fonte."""
    percorso = dati / (NOME_UNICO_COMPLETO if completo else NOME_UNICO)
    inclusi, totale = [], 0
    with open(percorso, "w", encoding="utf8") as uscita:
        testata = {"type": "FeatureCollection", "name": "fvg_unico",
                   "titolo": "Friuli Venezia Giulia, tutti i livelli in versione alleggerita"}
        uscita.write(json.dumps(testata, ensure_ascii=False)[:-1] + ', "features": [\n')
        primo = True
        for scheda in schede:
            peso = sum(f["byte"] for f in scheda["leggero"])
            if scheda["id"] in SENZA_LEGGERO or (not completo and peso > SOGLIA_FILE_UNICO_BYTE):
                continue
            inclusi.append(scheda["id"])
            prefisso = json.dumps({"livello": scheda["id"], "gruppo": scheda["gruppo"],
                                   "titolo_livello": scheda["titolo"], "fonte": scheda["fonte"]},
                                  ensure_ascii=False, separators=(",", ":"))[:-1]
            for file in scheda["leggero"]:
                with open(dati / file["percorso"], encoding="utf8") as ingresso:
                    for riga in ingresso:
                        riga = riga.rstrip(",\n")
                        if not riga.startswith('{"type":"Feature"'):
                            continue
                        segno = '"properties":{'
                        posizione = riga.index(segno) + len(segno)
                        vuoto = riga[posizione] == "}"
                        riga = riga[:posizione - 1] + prefisso + ("" if vuoto else ",") + riga[posizione:]
                        uscita.write(("" if primo else ",\n") + riga)
                        primo = False
                        totale += 1
        uscita.write("\n]}\n")
    return {"percorso": percorso.name, "elementi": totale, "byte": percorso.stat().st_size, "livelli": inclusi}


def principale():
    dati = pathlib.Path(sys.argv[1])
    scelti = set(sys.argv[2:]) - {"--unico-completo"}
    integrale = json.loads((dati / "indice_integrale.json").read_text(encoding="utf8"))
    percorso_indice = dati / "indice.json"
    gia = {}
    if percorso_indice.exists():
        gia = {s["id"]: s for s in json.loads(percorso_indice.read_text(encoding="utf8"))["livelli"]}
    schede = []
    for scheda in integrale["livelli"]:
        rifare = scheda["id"] in scelti
        if rifare or scheda["id"] not in gia:
            scheda["leggero"] = alleggerisci_livello(scheda, dati, rifare)
            print(scheda["id"], sum(f["byte"] for f in scheda["file"]) // 1000, "->",
                  sum(f["byte"] for f in scheda["leggero"]) // 1000, "kB", flush=True)
        else:
            scheda["leggero"] = gia[scheda["id"]]["leggero"]
        schede.append(scheda)
    unico = scrivi_file_unico(schede, dati)
    print("file unico", unico["elementi"], "elementi", unico["byte"] // 1000, "kB")
    if "--unico-completo" in sys.argv:       # file di lavoro, troppo pesante per essere pubblicato
        completo = scrivi_file_unico(schede, dati, completo=True)
        print("file unico completo", completo["elementi"], "elementi", completo["byte"] // 1000, "kB")
    indice = {"fonti": FONTI, "file_unico": unico, "livelli": schede}
    percorso_indice.write_text(json.dumps(indice, ensure_ascii=False, indent=1), encoding="utf8")


if __name__ == "__main__":
    principale()
