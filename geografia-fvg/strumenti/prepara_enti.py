"""Costruisce i perimetri degli enti sovracomunali unendo i comuni che li compongono.

Uso: python3 prepara_enti.py CARTELLA_DATI CARTELLA_INTERMEDI
Le composizioni stanno in enti_sovracomunali.json, con la fonte ufficiale di ciascuna.
I due distretti di Trieste seguono le circoscrizioni comunali, prese da OpenStreetMap.
"""
import json
import pathlib
import sys
import unicodedata

import shapely
from shapely.geometry import mapping, shape

QUI = pathlib.Path(__file__).parent
COMUNI_FVG = 215
PROVINCE = {"030": "Udine", "031": "Gorizia", "032": "Trieste", "093": "Pordenone"}
PROVINCE_AZIENDA = {"ASUFC": {"030"}, "ASFO": {"093"}, "ASUGI": {"031", "032"}}
COD_TRIESTE = "032006"


def chiave(nome):
    """Riduce un nome di comune a una forma confrontabile: senza accenti, trattini e apostrofi."""
    testo = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode().upper()
    return "".join(c for c in testo if c.isalnum())


def leggi_raccolta(percorso):
    return json.loads(percorso.read_text(encoding="utf8"))["features"]


class Comuni:
    def __init__(self, dati):
        self.per_chiave = {}
        for e in leggi_raccolta(dati / "integrale" / "confini" / "comuni.geojson"):
            p = e["properties"]
            self.per_chiave[chiave(p["NOME"])] = (p["COD_ISTAT"], p["NOME"], shapely.make_valid(shape(e["geometry"])))
        if len(self.per_chiave) != COMUNI_FVG:
            raise ValueError("i comuni della Regione non sono 215")

    def uno(self, nome):
        """Cerca il comune per nome esatto o, per i nomi bilingui, per parte iniziale univoca."""
        k = chiave(nome)
        if k in self.per_chiave:
            return self.per_chiave[k]
        simili = [v for c, v in self.per_chiave.items() if c.startswith(k)]
        return simili[0] if len(simili) == 1 else None

    def trova(self, nomi):
        trovati = [self.uno(n) for n in nomi]
        mancanti = [n for n, t in zip(nomi, trovati) if t is None]
        if mancanti:
            raise ValueError(f"comuni non riconosciuti: {mancanti}")
        # Si conserva la grafia del nome usata nella fonte.
        return [(t[0], n, t[2]) for n, t in zip(nomi, trovati)]


def elemento(nome, comuni, extra, forma=None):
    """Un ente: unione dei comuni (o forma già pronta), con elenco e numero dei comuni."""
    forma = forma if forma is not None else shapely.unary_union([c[2] for c in comuni])
    proprieta = {"nome": nome, "numero_comuni": len(comuni),
                 "comuni": ", ".join(sorted(c[1] for c in comuni)),
                 "codici_istat": ", ".join(sorted(c[0] for c in comuni)), **extra}
    return {"type": "Feature", "properties": proprieta, "geometry": mapping(forma)}


def scrivi(percorso, elementi):
    with open(percorso, "w", encoding="utf8") as f:
        for e in elementi:
            f.write(json.dumps(e, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(percorso.name, len(elementi))


def controlla_partizione(gruppi, attesi, nome):
    """Ogni comune atteso deve comparire in un gruppo e in uno solo."""
    visti = [c[0] for comuni in gruppi for c in comuni]
    if sorted(visti) != sorted(attesi):
        doppi = {c for c in visti if visti.count(c) > 1}
        raise ValueError(f"{nome}: comuni doppi {doppi}, mancanti {set(attesi) - set(visti)}, estranei {set(visti) - set(attesi)}")


def circoscrizioni_trieste(dati, nomi, sagoma_trieste):
    trovate = {e["properties"].get("name"): shape(e["geometry"])
               for e in leggi_raccolta(dati / "integrale" / "confini" / "osm_frazioni_confini.geojson")}
    mancanti = [n for n in nomi if n not in trovate]
    if mancanti:
        raise ValueError(f"circoscrizioni di Trieste non trovate: {mancanti}")
    return shapely.unary_union([shapely.make_valid(trovate[n]) for n in nomi]).intersection(sagoma_trieste)


def principale():
    dati, uscita = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    enti = json.loads((QUI / "enti_sovracomunali.json").read_text(encoding="utf8"))
    fonti, comuni = enti["fonti"], Comuni(dati)
    tutti = [c[0] for c in comuni.per_chiave.values()]
    fonte = lambda k: {"fonte_composizione": fonti[k]["documento"], "indirizzo_fonte": fonti[k]["indirizzo"]}

    ambiti = {n: comuni.trova(v["comuni"]) for n, v in enti["ambiti_servizio_sociale"].items()}
    controlla_partizione(ambiti.values(), tutti, "ambiti del Servizio sociale")
    scrivi(uscita / "ambiti_servizio_sociale.jsonl",
           [elemento(n, c, {"ente_gestore": enti["ambiti_servizio_sociale"][n]["ente_gestore"], **fonte("ambiti")})
            for n, c in ambiti.items()])

    scrivi(uscita / "comunita_montagna.jsonl",
           [elemento(n, comuni.trova(v), fonte("statuti")) for n, v in enti["comunita_montagna"].items()])
    scrivi(uscita / "comunita_collinare.jsonl",
           [elemento(n, comuni.trova(v), fonte("collinare")) for n, v in enti["comunita_collinare"].items()])

    trieste = comuni.uno("Trieste")
    distretti, aziende = [], []
    for sigla, azienda in enti["distretti_sanitari"].items():
        membri = []
        for nome, regola in azienda["distretti"].items():
            extra = {"azienda": azienda["nome"], "sigla_azienda": sigla, **fonte(azienda["fonte"])}
            if isinstance(regola, str):
                distretti.append(elemento(nome, ambiti[regola], {**extra, "ambito_servizio_sociale": regola}))
                membri += ambiti[regola]
                continue
            # Distretti di Trieste: circoscrizioni del capoluogo, più gli eventuali comuni di un ambito.
            if "ambito" not in regola:
                parte = prima_parte = circoscrizioni_trieste(dati, regola["circoscrizioni_trieste"], trieste[2])
            else:   # il secondo distretto prende il resto del capoluogo, così le due parti lo coprono per intero
                circoscrizioni_trieste(dati, regola["circoscrizioni_trieste"], trieste[2])
                parte = trieste[2].difference(prima_parte)
            altri = ambiti[regola["ambito"]] if "ambito" in regola else []
            forma = shapely.unary_union([parte] + [c[2] for c in altri])
            extra["circoscrizioni_di_trieste"] = ", ".join(regola["circoscrizioni_trieste"])
            extra["nota"] = "Trieste è divisa tra due distretti secondo le circoscrizioni comunali, tratte da OpenStreetMap"
            distretti.append(elemento(nome, altri, extra, forma))
            membri += altri + ([trieste] if "ambito" not in regola else [])
        attesi = [c for c in tutti if c[:3] in PROVINCE_AZIENDA[sigla]]
        controlla_partizione([membri], attesi, f"azienda {sigla}")
        province = ", ".join(PROVINCE[p] for p in sorted(PROVINCE_AZIENDA[sigla]))
        aziende.append(elemento(azienda["nome"], membri, {"sigla": sigla, "ex_province": province, **fonte(azienda["fonte"])}))
    scrivi(uscita / "distretti_sanitari.jsonl", distretti)
    scrivi(uscita / "aziende_sanitarie.jsonl", aziende)
    # Le due parti di Trieste devono coprire l'intero comune.
    parti = [shape(d["geometry"]).intersection(trieste[2]).area for d in distretti if "Trieste" in d["properties"]["nome"]]
    print("copertura di Trieste da parte dei due distretti:", round(sum(parti) / trieste[2].area, 4))


if __name__ == "__main__":
    principale()
