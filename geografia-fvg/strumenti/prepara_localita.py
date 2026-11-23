"""Ricava i perimetri delle località abitate ISTAT 2021 unendo le sezioni di censimento.

Uso: python3 prepara_localita.py CARTELLA_FONTI CARTELLA_INTERMEDI
"""
import json
import pathlib
import sys

import geopandas as gpd
import pandas as pd

TIPI_LOCALITA = {1: "centro abitato", 2: "nucleo abitato", 3: "località produttiva"}


def principale():
    fonti, uscita = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    pagine = sorted((fonti / "regione" / "sezioni_censimento_2021").glob("pagina_*.json"))
    sezioni = pd.concat([gpd.read_file(p) for p in pagine], ignore_index=True)
    sezioni = sezioni[sezioni.TIPO_LOC.isin(TIPI_LOCALITA)].copy()
    sezioni["geometry"] = sezioni.geometry.force_2d().make_valid()
    localita = sezioni.dissolve(by="LOC21_ID", aggfunc={"PRO_COM": "first", "TIPO_LOC": "first", "POP21": "sum",
                                                        "FAM21": "sum", "ABI21": "sum", "EDI21": "sum", "SEZ21": "count"})
    localita = localita.reset_index().rename(columns={"SEZ21": "sezioni"})
    localita["LOC21_ID"] = localita.LOC21_ID.astype("int64")
    localita["tipo"] = localita.TIPO_LOC.map(TIPI_LOCALITA)
    with open(uscita / "localita_istat_2021.jsonl", "w", encoding="utf8") as f:
        for riga in json.loads(localita.to_json())["features"]:
            riga.pop("id", None)
            f.write(json.dumps(riga, ensure_ascii=False, separators=(",", ":")) + "\n")
    print("localita_istat_2021", len(localita), localita.tipo.value_counts().to_dict(), "popolazione", int(localita.POP21.sum()))


if __name__ == "__main__":
    principale()
