"""Scrive l'elenco dei livelli in Markdown e in Excel a partire dall'indice.

Uso: python3 scrivi_elenco.py CARTELLA_DATI CARTELLA_USCITA
"""
import json
import pathlib
import sys

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill

GRUPPI = {"confini": "Confini amministrativi", "acque": "Acque", "rilievo": "Monti e rilievo",
          "natura": "Natura e aree protette", "trasporti": "Strade, ferrovie, ciclovie e sentieri",
          "insediamenti": "Centri abitati ed edifici", "servizi": "Servizi e luoghi di interesse"}
FONTI = {"REGIONE": "Regione FVG (IRDAT)", "ISTAT": "ISTAT, confini 2026", "ISTAT_CENS": "ISTAT, censimento 2021",
         "OSM": "OpenStreetMap", "GISCO": "Eurostat GISCO", "COPERNICUS": "Copernicus DEM"}
GEOMETRIE = {"Point": "punti", "MultiPoint": "punti", "LineString": "linee", "MultiLineString": "linee",
             "Polygon": "aree", "MultiPolygon": "aree"}
INTESTAZIONI = ["Gruppo", "Livello", "Identificativo", "Fonte", "Livello di origine", "Geometria", "Elementi",
                "File integrali", "Peso integrale (MB)", "Peso leggero (MB)", "Nel file unico", "Percorso"]


def megabyte(file):
    return round(sum(f["byte"] for f in file) / 1e6, 2)


def righe(indice):
    nel_unico = set(indice["file_unico"]["livelli"])
    for gruppo in GRUPPI:
        for s in indice["livelli"]:
            if s["gruppo"] != gruppo:
                continue
            geometria = ", ".join(sorted({GEOMETRIE[g] for g in s["geometrie"]}))
            percorso = s["file"][0]["percorso"] if len(s["file"]) == 1 else str(pathlib.Path(s["file"][0]["percorso"]).parent) + "/"
            yield [GRUPPI[gruppo], s["titolo"], s["id"], FONTI[s["fonte"]], s.get("livello_origine") or "", geometria,
                   s["elementi"], len(s["file"]), megabyte(s["file"]), megabyte(s["leggero"]),
                   "sì" if s["id"] in nel_unico else "no", percorso]


def principale():
    dati, uscita = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    indice = json.loads((dati / "indice.json").read_text(encoding="utf8"))
    tabella = list(righe(indice))
    numero = lambda n: f"{n:,}".replace(",", ".")
    testo = ["# Elenco dei livelli", "",
             f"Livelli: {len(tabella)}. Elementi: {numero(sum(r[6] for r in tabella))}. "
             f"File integrali: {numero(sum(r[7] for r in tabella))}.", ""]
    for gruppo in GRUPPI.values():
        scelte = [r for r in tabella if r[0] == gruppo]
        testo += [f"## {gruppo} ({len(scelte)} livelli)", "",
                  "| Livello | Identificativo | Fonte | Geometria | Elementi | Integrale (MB) | Leggero (MB) | Nel file unico |",
                  "|---|---|---|---|---:|---:|---:|---|"]
        testo += [f"| {r[1]} | `{r[2]}` | {r[3]} | {r[5]} | {numero(r[6])} | {str(r[8]).replace('.', ',')} | "
                  f"{str(r[9]).replace('.', ',')} | {r[10]} |" for r in scelte]
        testo.append("")
    (uscita / "ELENCO_LIVELLI.md").write_text("\n".join(testo), encoding="utf8")
    libro = openpyxl.Workbook()
    foglio = libro.active
    foglio.title = "Livelli"
    foglio.append(INTESTAZIONI)
    for riga in tabella:
        foglio.append(riga)
    for cella in foglio[1]:
        cella.font = Font(bold=True, color="FFFFFF")
        cella.fill = PatternFill("solid", fgColor="1F3F9E")
        cella.alignment = Alignment(vertical="center", wrap_text=True)
    for lettera, larghezza in zip("ABCDEFGHIJKL", (28, 52, 32, 24, 44, 12, 12, 10, 12, 12, 10, 60)):
        foglio.column_dimensions[lettera].width = larghezza
    foglio.freeze_panes = "A2"
    foglio.auto_filter.ref = foglio.dimensions
    libro.save(uscita / "elenco_livelli.xlsx")
    print("livelli", len(tabella), "elementi", sum(r[6] for r in tabella))


if __name__ == "__main__":
    principale()
