"""Prepara i livelli ricavati da ISTAT e i comuni confinanti di Veneto, Austria e Slovenia.

Uso: python3 prepara_confini.py CARTELLA_FONTI CARTELLA_INTERMEDI
"""
import json
import pathlib
import sys

import geopandas as gpd
import osmium
import osmium.geom
import shapely
from shapely.geometry import shape

COD_FVG, COD_VENETO = 6, 5
TOLLERANZA_M = 50  # distanza entro cui due enti si considerano confinanti
UTM33 = 32633


def salva(tabella, percorso):
    tabella = tabella.to_crs(4326)
    with open(percorso, "w", encoding="utf8") as f:
        for riga in json.loads(tabella.to_json())["features"]:
            riga.pop("id", None)
            riga.pop("bbox", None)
            f.write(json.dumps(riga, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(percorso.name, len(tabella))


def comuni_austriaci(pbf):
    fabbrica = osmium.geom.GeoJSONFactory()
    righe = []
    lettore = osmium.FileProcessor(pbf).with_areas().with_filter(osmium.filter.KeyFilter("admin_level"))
    for o in lettore:
        if not o.is_area():
            continue
        t = dict(o.tags)
        if t.get("boundary") != "administrative" or t.get("admin_level") != "8":
            continue
        try:
            geometria = shape(json.loads(fabbrica.create_multipolygon(o)))
        except Exception:
            continue
        righe.append({"osm_id": f"relation/{o.orig_id()}", "nome": t.get("name"), "nome_it": t.get("name:it"),
                      "codice_comune": t.get("ref:at:gkz"), "stato": "Austria", "wikidata": t.get("wikidata"),
                      "geometry": geometria})
    return gpd.GeoDataFrame(righe, crs=4326)


def principale():
    fonti, uscita = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    uscita.mkdir(parents=True, exist_ok=True)
    base = fonti / "istat" / "x"
    leggi = lambda n: gpd.read_file(base / f"{n}01012026" / f"{n}01012026_WGS84.shp", encoding="utf-8")
    regioni, province, comuni = leggi("Reg"), leggi("ProvCM"), leggi("Com")
    fvg = regioni[regioni.COD_REG == COD_FVG]
    salva(fvg, uscita / "istat_regione.jsonl")
    salva(province[province.COD_REG == COD_FVG], uscita / "istat_province.jsonl")
    salva(comuni[comuni.COD_REG == COD_FVG], uscita / "istat_comuni.jsonl")

    sagoma = fvg.geometry.iloc[0]
    vicino = sagoma.buffer(TOLLERANZA_M)
    veneto = regioni[regioni.COD_REG == COD_VENETO].geometry.iloc[0]
    comune = sagoma.boundary.intersection(veneto.buffer(1))
    tratti = [g for g in shapely.get_parts(comune) if g.geom_type == "LineString"]
    linea = shapely.line_merge(shapely.MultiLineString(tratti))
    salva(gpd.GeoDataFrame([{"nome": "Confine tra Friuli Venezia Giulia e Veneto", "lunghezza_km": round(linea.length / 1000, 2),
                             "geometry": linea}], crs=regioni.crs), uscita / "confine_veneto.jsonl")
    com_veneto = comuni[(comuni.COD_REG == COD_VENETO) & comuni.intersects(vicino)]
    salva(com_veneto, uscita / "veneto_comuni_confinanti.jsonl")
    salva(province[(province.COD_REG == COD_VENETO) & province.intersects(vicino)], uscita / "veneto_province_confinanti.jsonl")

    sagoma33 = fvg.to_crs(UTM33).geometry.iloc[0].buffer(TOLLERANZA_M)
    austria = comuni_austriaci(str(fonti / "osm" / "karnten.osm.pbf"))
    salva(austria[austria.to_crs(UTM33).intersects(sagoma33)], uscita / "austria_comuni_confinanti.jsonl")
    lau = fonti / "lau2024.geojson"
    if lau.exists():
        slovenia = gpd.read_file(lau, where="CNTR_CODE = 'SI'")
        slovenia = slovenia[slovenia.to_crs(UTM33).intersects(sagoma33)]
        slovenia = slovenia.rename(columns={"LAU_NAME": "nome", "GISCO_ID": "codice_comune"})[["nome", "codice_comune", "geometry"]]
        slovenia["stato"] = "Slovenia"
        salva(slovenia, uscita / "slovenia_comuni_confinanti.jsonl")


if __name__ == "__main__":
    principale()
