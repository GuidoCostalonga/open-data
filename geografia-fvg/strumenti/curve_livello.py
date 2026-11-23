"""Genera le curve di livello del FVG dal modello altimetrico Copernicus GLO-30.

Uso: python3 curve_livello.py CARTELLA_FONTI CARTELLA_INTERMEDI
Le quote sono riferite al geoide EGM2008. Il modello descrive la superficie
(compresi boschi ed edifici), quindi in pianura le curve sono indicative.
"""
import json
import pathlib
import sys

import contourpy
import geopandas as gpd
import numpy as np
import rasterio
import rasterio.merge
import shapely

EQUIDISTANZA_M = 25
DIRETTRICE_M = 100
PRECISIONE = 5          # circa un metro, coerente con la griglia a 30 metri
PUNTI_MINIMI = 6        # scarta gli anellini dovuti al rumore del modello
MARGINE_GRADI = 0.02


def principale():
    fonti, uscita = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    province = gpd.read_file(fonti / "istat" / "x" / "ProvCM01012026" / "ProvCM01012026_WGS84.shp", encoding="utf-8")
    province = province[province.COD_REG == 6].to_crs(4326)
    ovest, sud, est, nord = province.total_bounds
    riquadro = (ovest - MARGINE_GRADI, sud - MARGINE_GRADI, est + MARGINE_GRADI, nord + MARGINE_GRADI)
    tasselli = [rasterio.open(p) for p in sorted((fonti / "dem").glob("*.tif"))]
    quote, trasformazione = rasterio.merge.merge(tasselli, bounds=riquadro)
    quote = quote[0].astype("float32")
    righe, colonne = quote.shape
    x = trasformazione.c + trasformazione.a * (np.arange(colonne) + 0.5)
    y = trasformazione.f + trasformazione.e * (np.arange(righe) + 0.5)
    generatore = contourpy.contour_generator(x, y, quote, line_type="Separate")
    livelli = np.arange(EQUIDISTANZA_M, float(np.nanmax(quote)), EQUIDISTANZA_M)
    sagome = {r.SIGLA: r.geometry for r in province.itertuples()}
    for sagoma in sagome.values():
        shapely.prepare(sagoma)
    totale = 0
    with open(uscita / "curve_livello.jsonl", "w", encoding="utf8") as f:
        for quota in livelli:
            linee = [shapely.LineString(l) for l in generatore.lines(float(quota)) if len(l) >= PUNTI_MINIMI]
            if not linee:
                continue
            linee = np.array(linee)
            for sigla, sagoma in sagome.items():
                dentro = linee[shapely.intersects(sagoma, linee)]
                if not len(dentro):
                    continue
                ritagliate = shapely.intersection(dentro, sagoma)
                parti = [p for p in shapely.get_parts(ritagliate) if p.geom_type == "LineString" and len(p.coords) >= 2]
                if not parti:
                    continue
                coordinate = [np.round(np.asarray(p.coords), PRECISIONE).tolist() for p in parti]
                elemento = {"type": "Feature",
                            "properties": {"quota": int(quota), "tipo": "direttrice" if quota % DIRETTRICE_M == 0 else "ordinaria",
                                           "provincia": sigla},
                            "geometry": {"type": "MultiLineString", "coordinates": coordinate}}
                f.write(json.dumps(elemento, separators=(",", ":")) + "\n")
                totale += 1
    print("curve_livello", totale, "quota massima del modello", float(np.nanmax(quote)))


if __name__ == "__main__":
    principale()
