#!/usr/bin/env python3
"""
confronta_dati.py
Verifica che la revisione grafica non abbia alterato, perso o inventato dati.

Uso:
    python3 confronta_dati.py <originale.html> <rivista.html>
    python3 confronta_dati.py <prima/testo.txt> <dopo/testo.txt>

La prima forma legge il codice della pagina. La seconda legge il testo reso dal
navigatore (prodotto da ispeziona.js) ed e' indispensabile quando la pagina
carica i dati da file esterni o li calcola con JavaScript: in quel caso i numeri
non stanno nel codice HTML. Eseguire sempre entrambe.

Confronta tre cose tra la pagina originale e quella rivista:
  1. i numeri presenti nel testo (compresi quelli nascosti in schede o pannelli);
  2. i numeri presenti nei blocchi <script> (dove spesso stanno i dati dei grafici);
  3. i blocchi di testo.

Esito:
  0  nessun numero del testo e' andato perso
  1  almeno un numero del testo originale manca, o compare meno volte, nella
     versione rivista
  2  errore d'uso

I numeri nuovi non sono un errore in se' (assi dei grafici, passaggi numerati),
ma ciascuno va giustificato: deve derivare da dati gia' presenti nella pagina.
"""
import re
import sys
from collections import Counter
from html.parser import HTMLParser

SENZA_TESTO = {"script", "style", "noscript", "template"}
# Attributi il cui contenuto viene letto o visto dall'utente
ATTRIBUTI_LETTI = {"alt", "title", "aria-label", "placeholder", "value", "content", "label"}
NUMERO = re.compile(r"\d+(?:[.,   ]\d{3})*(?:[.,]\d+)?|\d+")


class Estrattore(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pila = []
        self.testi = []
        self.attributi = []
        self.script = []
        self._blocco = []

    def _chiudi_blocco(self):
        t = " ".join("".join(self._blocco).split())
        if t:
            self.testi.append(t)
        self._blocco = []

    def handle_starttag(self, tag, attrs):
        self.pila.append(tag)
        if tag not in ("span", "b", "i", "em", "strong", "a", "small", "sup", "sub",
                       "abbr", "mark", "code", "tspan", "u", "s"):
            self._chiudi_blocco()
        for nome, valore in attrs:
            if valore and nome in ATTRIBUTI_LETTI:
                self.attributi.append(valore)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if self.pila and self.pila[-1] == tag:
            self.pila.pop()

    def handle_endtag(self, tag):
        if tag in self.pila:
            while self.pila and self.pila.pop() != tag:
                pass
        if tag not in ("span", "b", "i", "em", "strong", "a", "small", "sup", "sub",
                       "abbr", "mark", "code", "tspan", "u", "s"):
            self._chiudi_blocco()

    def handle_data(self, data):
        if any(t in ("script",) for t in self.pila):
            self.script.append(data)
        elif not any(t in SENZA_TESTO for t in self.pila):
            self._blocco.append(data)

    def close(self):
        super().close()
        self._chiudi_blocco()


def normalizza_numero(n):
    """Rende confrontabili 1.234,5 e 1234,5: toglie i separatori delle migliaia
    solo quando sono spazi; punti e virgole restano come scritti."""
    return re.sub(r"[   ]", "", n)


def numeri(testi):
    c = Counter()
    for t in testi:
        for m in NUMERO.findall(t):
            c[normalizza_numero(m)] += 1
    return c


def leggi(percorso):
    with open(percorso, encoding="utf-8", errors="replace") as f:
        sorgente = f.read()
    e = Estrattore()
    if percorso.lower().endswith(".txt"):
        e.testi = [" ".join(r.split()) for r in sorgente.splitlines() if r.strip()]
        return e
    e.feed(sorgente)
    e.close()
    return e


def chiave(t):
    return re.sub(r"\W+", " ", t.lower()).strip()


def elenco(c, limite=60):
    voci = sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))
    testo = ", ".join(f"{n} (x{q})" if q > 1 else n for n, q in voci[:limite])
    if len(voci) > limite:
        testo += f" ... e altri {len(voci) - limite}"
    return testo


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    prima, dopo = leggi(sys.argv[1]), leggi(sys.argv[2])

    n_prima = numeri(prima.testi + prima.attributi)
    n_dopo = numeri(dopo.testi + dopo.attributi)
    persi = n_prima - n_dopo
    # Un numero conta come perso solo se sparisce del tutto o diminuisce di frequenza
    spariti = Counter({n: q for n, q in persi.items() if n not in n_dopo})
    diminuiti = Counter({n: q for n, q in persi.items() if n in n_dopo})
    nuovi = Counter({n: q for n, q in (n_dopo - n_prima).items() if n not in n_prima})

    s_prima, s_dopo = numeri(prima.script), numeri(dopo.script)
    script_spariti = Counter({n: q for n, q in (s_prima - s_dopo).items()
                              if n not in s_dopo and n not in n_dopo})

    chiavi_dopo = {chiave(t) for t in dopo.testi}
    tutto_dopo = " " + " ".join(sorted(chiavi_dopo)) + " "
    testi_persi = []
    for t in prima.testi:
        k = chiave(t)
        if len(k) < 12 or k in chiavi_dopo:
            continue
        if f" {k} " in tutto_dopo or k in chiave(" ".join(dopo.testi)):
            continue
        testi_persi.append(t)

    print("VERIFICA DI INTEGRITA' DEI DATI")
    print(f"  originale: {sys.argv[1]}")
    print(f"  rivista:   {sys.argv[2]}")
    print()
    print(f"Numeri nel testo: {sum(n_prima.values())} prima, {sum(n_dopo.values())} dopo "
          f"({len(n_prima)} e {len(n_dopo)} valori distinti)")
    print()

    if spariti:
        print(f"[ERRORE] Numeri del testo SPARITI ({len(spariti)}):")
        print("  " + elenco(spariti))
    else:
        print("[OK] Nessun numero del testo e' sparito.")

    if diminuiti:
        print(f"[CONTROLLARE] Numeri che compaiono meno volte di prima ({len(diminuiti)}):")
        print("  " + elenco(diminuiti))

    if nuovi:
        print(f"[GIUSTIFICARE] Numeri nuovi nel testo ({len(nuovi)}): ciascuno deve derivare "
              "da dati gia' presenti (assi, passaggi numerati, somme dichiarate).")
        print("  " + elenco(nuovi))
    else:
        print("[OK] Nessun numero nuovo nel testo.")

    if script_spariti:
        print(f"[CONTROLLARE] Numeri spariti dai blocchi script ({len(script_spariti)}): "
              "se erano dati di grafici o tabelle, vanno ripristinati.")
        print("  " + elenco(script_spariti, 40))
    else:
        print("[OK] Nessun numero sparito dai blocchi script.")

    if testi_persi:
        print(f"[CONTROLLARE] Blocchi di testo non ritrovati ({len(testi_persi)}): "
              "riformulati, spostati dentro un altro blocco oppure rimossi.")
        for t in testi_persi[:40]:
            print("  * " + (t if len(t) <= 160 else t[:157] + "..."))
        if len(testi_persi) > 40:
            print(f"  ... e altri {len(testi_persi) - 40}")
    else:
        print("[OK] Tutti i blocchi di testo originali sono ancora presenti.")

    return 1 if (spariti or diminuiti) else 0


if __name__ == "__main__":
    sys.exit(main())
