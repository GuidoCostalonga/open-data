"""Scarica dal servizio WFS della Regione FVG i livelli elencati in catalogo_regione.txt.

Uso: python3 scarica_regione.py CARTELLA_GREZZI [id ...]
Ogni livello viene salvato a pagine in CARTELLA_GREZZI/regione/<id>/pagina_N.json (WGS84).
"""
import concurrent.futures as cf
import json
import pathlib
import sys
import time
import urllib.parse
import urllib.request

WFS = "https://serviziogc.regione.fvg.it/geoserver/ows"
PAGINA = 10000
TENTATIVI = 4
# Viste molto grandi e senza chiave primaria: si scaricano un comune alla volta.
FILTRO_PER_COMUNE = {"numeri_civici": "ISTAT_COMUNE"}
QUI = pathlib.Path(__file__).parent


def leggi_catalogo():
    righe = (QUI / "catalogo_regione.txt").read_text(encoding="utf8").splitlines()
    return [r.split("|") for r in righe if r and not r.startswith("#")]


def richiedi(parametri, attesa=600):
    url = WFS + "?" + urllib.parse.urlencode(parametri)
    ultimo = None
    for tentativo in range(TENTATIVI):
        try:
            with urllib.request.urlopen(url, timeout=attesa) as risposta:
                return risposta.read()
        except Exception as errore:  # rete instabile: si riprova con attesa crescente
            ultimo = errore
            time.sleep(5 * (tentativo + 1))
    raise RuntimeError(f"richiesta fallita: {url}: {ultimo}")


def pagina_valida(parametri, attesa=600):
    """Scarica una pagina e controlla che sia JSON completo; riprova se arriva troncata."""
    for _ in range(TENTATIVI):
        dati = richiedi(parametri, attesa)
        try:
            json.loads(dati)
            return dati
        except ValueError:
            time.sleep(5)
    raise RuntimeError(f"risposta non valida per {parametri.get('typeNames')}")


def scarica_per_comune(voce, radice, attesi):
    """Scarica un livello filtrandolo per codice ISTAT del comune (serve il livello comuni già scaricato)."""
    ident, _, _, livello = voce
    cartella = radice / "regione" / ident
    comuni = json.loads((radice / "regione" / "comuni" / "pagina_0000.json").read_text(encoding="utf8"))
    codici = sorted(c["properties"]["COD_ISTAT"] for c in comuni["features"])
    scaricati = 0
    for indice, codice in enumerate(codici):
        dati = pagina_valida({"service": "WFS", "version": "2.0.0", "request": "GetFeature", "typeNames": livello,
                              "outputFormat": "application/json", "srsName": "EPSG:4326",
                              "CQL_FILTER": f"{FILTRO_PER_COMUNE[ident]}='{codice}'"}, attesa=1200)
        (cartella / f"pagina_{indice:04d}.json").write_bytes(dati)
        scaricati += len(json.loads(dati)["features"])
    if scaricati != attesi:
        raise RuntimeError(f"{ident}: attesi {attesi}, scaricati {scaricati}")
    (cartella / "FATTO.json").write_text(json.dumps({"livello": livello, "elementi": scaricati,
                                                     "data": time.strftime("%Y-%m-%d")}))
    return scaricati


def scarica(voce, radice):
    ident, _, _, livello = voce
    cartella = radice / "regione" / ident
    fatto = cartella / "FATTO.json"
    if fatto.exists():
        return ident, json.loads(fatto.read_text())["elementi"], "già presente"
    cartella.mkdir(parents=True, exist_ok=True)
    base = {"service": "WFS", "version": "2.0.0", "request": "GetFeature", "typeNames": livello}
    testo = richiedi({**base, "resultType": "hits"}).decode("utf8", "replace")
    attesi = int(testo.split('numberMatched="')[1].split('"')[0])
    if ident in FILTRO_PER_COMUNE:
        return ident, scarica_per_comune(voce, radice, attesi), "scaricato"
    scaricati, indice = 0, 0
    richiesta = {**base, "outputFormat": "application/json", "srsName": "EPSG:4326"}
    while scaricati < attesi:
        try:
            dati = pagina_valida({**richiesta, "count": PAGINA, "startIndex": scaricati})
        except RuntimeError:
            if scaricati:
                raise
            # Le viste senza chiave primaria non ammettono la paginazione: richiesta unica.
            dati = pagina_valida({**richiesta, "count": attesi + 10}, attesa=3600)
        elementi = len(json.loads(dati)["features"])
        if elementi == 0:
            break
        (cartella / f"pagina_{indice:04d}.json").write_bytes(dati)
        scaricati += elementi
        indice += 1
    if scaricati != attesi:
        raise RuntimeError(f"{ident}: attesi {attesi}, scaricati {scaricati}")
    fatto.write_text(json.dumps({"livello": livello, "elementi": scaricati,
                                 "data": time.strftime("%Y-%m-%d")}))
    return ident, scaricati, "scaricato"


def principale():
    radice = pathlib.Path(sys.argv[1])
    scelti = set(sys.argv[2:])
    voci = [v for v in leggi_catalogo() if not scelti or v[0] in scelti]
    errori = []
    with cf.ThreadPoolExecutor(4) as gruppo:
        futuri = {gruppo.submit(scarica, v, radice): v[0] for v in voci}
        for futuro in cf.as_completed(futuri):
            try:
                print(*futuro.result(), flush=True)
            except Exception as errore:
                errori.append(futuri[futuro])
                print("ERRORE", futuri[futuro], errore, flush=True)
    print("FINE. Errori:", errori)
    sys.exit(1 if errori else 0)


if __name__ == "__main__":
    principale()
