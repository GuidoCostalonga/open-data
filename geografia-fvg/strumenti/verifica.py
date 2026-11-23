"""Controlla i file prodotti: validità GeoJSON, conteggi, riquadro e limite di peso.

Uso: python3 verifica.py CARTELLA_DATI
Termina con errore se trova anomalie.
"""
import json
import pathlib
import sys

LIMITE_FILE_BYTE = 95_000_000            # GitHub rifiuta i file oltre 100 MB
RIQUADRO_AMMESSO = (11.9, 45.3, 14.3, 46.9)  # FVG con margine per i comuni confinanti
# Livelli che per natura escono dal riquadro: zone marittime, province venete, uso del suolo
# con fascia esterna, rotte ed elettrodotti che OpenStreetMap restituisce per intero.
FUORI_RIQUADRO_AMMESSI = {"zone_marittime", "veneto_province_confinanti", "uso_suolo_corine", "osm_traghetti",
                          "osm_porti", "osm_linee_elettriche", "osm_infrastrutture"}
COMUNI_ATTESI, PROVINCE_ATTESE = 215, 4
TIPI = {"Point", "MultiPoint", "LineString", "MultiLineString", "Polygon", "MultiPolygon"}


def conta_e_controlla(percorso, problemi):
    """Legge l'intera raccolta e restituisce il numero di elementi."""
    try:
        raccolta = json.loads(percorso.read_text(encoding="utf8"))
    except ValueError as errore:
        problemi.append(f"{percorso}: JSON non valido ({errore})")
        return 0
    if raccolta.get("type") != "FeatureCollection":
        problemi.append(f"{percorso}: non è una FeatureCollection")
        return 0
    for elemento in raccolta["features"]:
        geometria = elemento.get("geometry") or {}
        if geometria.get("type") not in TIPI or not geometria.get("coordinates"):
            problemi.append(f"{percorso}: geometria assente o di tipo non previsto")
            break
    return len(raccolta["features"])


def principale():
    dati = pathlib.Path(sys.argv[1])
    indice = json.loads((dati / "indice.json").read_text(encoding="utf8"))
    problemi = []
    per_id = {s["id"]: s for s in indice["livelli"]}
    for ident, attesi in (("comuni", COMUNI_ATTESI), ("istat_comuni", COMUNI_ATTESI),
                          ("province", PROVINCE_ATTESE), ("istat_province", PROVINCE_ATTESE), ("regione", 1)):
        if per_id.get(ident, {}).get("elementi") != attesi:
            problemi.append(f"{ident}: attesi {attesi} elementi, trovati {per_id.get(ident, {}).get('elementi')}")
    elencati = set()
    for scheda in indice["livelli"]:
        ovest, sud, est, nord = scheda["riquadro"]
        fuori = scheda["id"] not in FUORI_RIQUADRO_AMMESSI
        if fuori and (ovest < RIQUADRO_AMMESSO[0] or sud < RIQUADRO_AMMESSO[1] or est > RIQUADRO_AMMESSO[2] or nord > RIQUADRO_AMMESSO[3]):
            problemi.append(f"{scheda['id']}: riquadro fuori dal FVG {scheda['riquadro']}")
        for versione in ("file", "leggero"):
            totale = 0
            for file in scheda[versione]:
                percorso = dati / file["percorso"]
                elencati.add(percorso.resolve())
                if not percorso.exists():
                    problemi.append(f"{percorso}: file mancante")
                    continue
                if percorso.stat().st_size > LIMITE_FILE_BYTE:
                    problemi.append(f"{percorso}: supera il limite di peso")
                trovati = conta_e_controlla(percorso, problemi)
                if trovati != file["elementi"]:
                    problemi.append(f"{percorso}: l'indice dichiara {file['elementi']} elementi, il file ne ha {trovati}")
                totale += trovati
            if versione == "file" and totale != scheda["elementi"]:
                problemi.append(f"{scheda['id']}: somma delle parti {totale} diversa da {scheda['elementi']}")
    unico = dati / indice["file_unico"]["percorso"]
    if unico.stat().st_size > LIMITE_FILE_BYTE:
        problemi.append("file unico: supera il limite di peso")
    if conta_e_controlla(unico, problemi) != indice["file_unico"]["elementi"]:
        problemi.append("file unico: numero di elementi diverso dall'indice")
    orfani = [p for p in dati.rglob("*.geojson") if p.resolve() not in elencati and p != unico]
    if orfani:
        problemi.append(f"file non elencati nell'indice: {[str(p) for p in orfani[:5]]}")
    print(f"Livelli controllati: {len(indice['livelli'])}. Problemi: {len(problemi)}")
    for problema in problemi:
        print(" -", problema)
    sys.exit(1 if problemi else 0)


if __name__ == "__main__":
    principale()
