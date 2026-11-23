"""Recupera gli ispettorati forestali dal servizio WFS della Regione FVG, un elemento alla volta.

Uso: python3 prepara_ispettorati.py CARTELLA_DATI CARTELLA_INTERMEDI

Il servizio non riesce a restituire tutti gli elementi insieme. Quando la geometria di un
ispettorato non è leggibile, il perimetro viene ricostruito unendo le giurisdizioni delle
stazioni forestali che gli appartengono (campo NOMEIRF del livello stazioni_forestali);
l'elemento porta allora il campo "nota". Lo stesso metodo viene applicato per controllo
agli ispettorati leggibili, e lo scarto viene stampato.
"""
import json
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request

import shapely
from shapely.geometry import mapping, shape

WFS = "https://serviziogc.regione.fvg.it/geoserver/ows"
LIVELLO = "UNIT_AMM:ISPETTORATI_FORESTALI"
SCARTO_MASSIMO = 0.01   # quota di superficie che può differire tra perimetro ufficiale e ricostruito
NOTA = ("Geometria non restituita dal servizio regionale: perimetro ricostruito unendo le "
        "giurisdizioni delle stazioni forestali dell'ispettorato")


def richiedi(parametri):
    base = {"service": "WFS", "version": "2.0.0", "request": "GetFeature", "typeNames": LIVELLO,
            "outputFormat": "application/json"}
    url = WFS + "?" + urllib.parse.urlencode({**base, **parametri})
    with urllib.request.urlopen(url, timeout=300) as risposta:
        return json.loads(risposta.read())


def senza_quota(geometria):
    return shapely.make_valid(shapely.force_2d(shape(geometria)))


def principale():
    dati, uscita = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    stazioni = json.loads((dati / "integrale" / "confini" / "stazioni_forestali.geojson").read_text(encoding="utf8"))
    per_ispettorato = {}
    for e in stazioni["features"]:
        per_ispettorato.setdefault(e["properties"]["NOMEIRF"], []).append(senza_quota(e["geometry"]))
    ricostruiti = {nome: shapely.unary_union(forme) for nome, forme in per_ispettorato.items()}

    schede = richiedi({"propertyName": "NOMEIRF,ID,INDIRIZZO,TELEFONO,EMAIL"})["features"]
    elementi = []
    for scheda in schede:
        proprieta = {k: v for k, v in scheda["properties"].items() if v not in (None, "")}
        nome = proprieta["NOMEIRF"]
        try:
            completo = richiedi({"featureID": scheda["id"], "srsName": "EPSG:4326"})["features"][0]
            forma = senza_quota(completo["geometry"])
            scarto = forma.symmetric_difference(ricostruiti[nome]).area / forma.area
            if scarto > SCARTO_MASSIMO:
                raise ValueError(f"{nome}: il perimetro ricostruito differisce del {scarto:.1%} da quello ufficiale")
            print(f"{nome}: geometria ufficiale; scarto del metodo di ricostruzione {scarto:.3%}")
        except (urllib.error.HTTPError, json.JSONDecodeError):
            forma = ricostruiti[nome]
            proprieta["nota"] = NOTA
            print(f"{nome}: geometria non leggibile, perimetro ricostruito da {len(per_ispettorato[nome])} stazioni forestali")
        elementi.append({"type": "Feature", "properties": proprieta, "geometry": mapping(forma)})
    with open(uscita / "ispettorati_forestali.jsonl", "w", encoding="utf8") as f:
        for e in elementi:
            f.write(json.dumps(e, ensure_ascii=False, separators=(",", ":")) + "\n")
    print("ispettorati_forestali", len(elementi))


if __name__ == "__main__":
    principale()
