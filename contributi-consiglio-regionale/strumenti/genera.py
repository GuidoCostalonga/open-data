#!/usr/bin/env python3
"""Genera le due dashboard sui contributi del Consiglio regionale FVG.

Legge:
  dati/CONTRIBUTO_CONSIGLIO_REGIONALE_2026_2025_2024_05112026.xlsx
  dati/comuni_fvg_semplificati.geojson   (confini comunali, openpolis, semplificati)
  dati/popolazione_istat_1gen2025_fvg.csv (ISTAT, popolazione al 1 gennaio 2025)
  dati/province_fvg_semplificate.geojson  (contorni delle province, ottenuti dai confini comunali)
Scrive:
  index.html  un solo file con due sezioni: Comuni 2024, 2025, 2026 e beneficiari 2026

Uso: python3 strumenti/genera.py   (dalla cartella contributi-consiglio-regionale)
Richiede openpyxl.
"""
import csv
import json
import re
import sys
import unicodedata
from datetime import datetime
from pathlib import Path

import openpyxl

BASE = Path(__file__).resolve().parent.parent
DATI = BASE / "dati"
MODELLI = Path(__file__).resolve().parent / "modelli"
XLSX = DATI / "CONTRIBUTO_CONSIGLIO_REGIONALE_2026_2025_2024_05112026.xlsx"
ANNI = (2026, 2025, 2024)  # ordine delle colonne nel Foglio1
OFFSET = {2026: 0, 2025: 5, 2024: 10}


def norm(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().upper()
    return re.sub(r"[^A-Z]", "", s)


ALIAS = {"REANADELROIALE": "REANADELROJALE"}


def carica_geo():
    g = json.loads((DATI / "comuni_fvg_semplificati.geojson").read_text(encoding="utf-8"))
    comuni = {}
    indice = {}
    for f in g["features"]:
        p = f["properties"]
        cod = p["com_istat_code"]
        nome = p["name"]
        geom = f["geometry"]
        polys = geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]
        # arrotonda a 4 decimali (circa 8 metri)
        polys = [[[[round(x, 4), round(y, 4)] for x, y in ring] for ring in poly] for poly in polys]
        comuni[cod] = {"c": cod, "n": nome, "p": p["prov_acr"], "g": polys, "k": centro(polys)}
        indice[norm(nome)] = cod
        # nomi bilingui: "Duino Aurisina-Devin Nabrežina" -> anche "Duino Aurisina"
        if "-" in nome:
            indice[norm(nome.split("-")[0])] = cod
    return comuni, indice


def area_anello(r):
    a = 0.0
    for i in range(len(r) - 1):
        a += r[i][0] * r[i + 1][1] - r[i + 1][0] * r[i][1]
    return a / 2


def centro(polys):
    # baricentro del poligono esterno più grande
    best = max((p[0] for p in polys), key=lambda r: abs(area_anello(r)))
    a = area_anello(best)
    if abs(a) < 1e-12:
        xs = [p[0] for p in best]
        ys = [p[1] for p in best]
        return [round(sum(xs) / len(xs), 4), round(sum(ys) / len(ys), 4)]
    cx = cy = 0.0
    for i in range(len(best) - 1):
        x0, y0 = best[i]
        x1, y1 = best[i + 1]
        f = x0 * y1 - x1 * y0
        cx += (x0 + x1) * f
        cy += (y0 + y1) * f
    return [round(cx / (6 * a), 4), round(cy / (6 * a), 4)]


def carica_pop():
    pop = {}
    with open(DATI / "popolazione_istat_1gen2025_fvg.csv", encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter=";"):
            pop[r["codice_istat"]] = int(r["popolazione_1gen2025"])
    return pop


def trova(indice, nome):
    k = norm(nome)
    k = ALIAS.get(k, k)
    return indice.get(k)


def iso(d):
    return d.strftime("%Y-%m-%d") if isinstance(d, datetime) else None


def tipologia(nome):
    s = " " + re.sub(r"[^A-Z0-9 ]", " ", unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode().upper()) + " "
    s = re.sub(r"\s+", " ", s)
    compatto = s.replace(" ", "")
    def ha(*parole):
        return any(p in s for p in parole)
    if ha(" PARROCCHIA", " ORATORIO ", " DIOCESI", " SEMINARIO ", " CATTOLICA "):
        return "Parrocchie ed enti religiosi"
    if ha(" ALPINI ", " BERSAGLIERI ", " ARMA AERONAUTICA", " DEL FANTE ", " CARABINIERI ", " MARINAI ",
          " COMBATTENTI", " PARACADUTISTI", " ARTIGLIERI") or s.startswith(" A N A ") or s.startswith(" ANA "):
        return "Alpini e associazioni d'arma"
    if ha(" PRO LOCO", " PROLOCO", " FESTEGGIAMENTI", " SAGRA ", " PRO CORDENONS ", " PRO BARCIS ",
          " PRO VILLA ", " BORGATE ") or re.match(r" (ASSOCIAZIONE )?(TURISTICA )?PRO ?[A-Z]", s) and " PROMETEO" not in s:
        return "Pro Loco e feste di paese"
    if ha(" CORO ", " CORALE ", " BANDA ", " BANDISTICO", " FILARMONICA", " MUSICA", " MUSICAL",
          " POLIFONIC", " ORCHESTRA", " GOSPEL", " ACCORDION", " ENSEMBLE", " FLUTE ", " ANBIMA ",
          " A N B I M A ", " MUSICISTI", " MUSICOLOGI", " SCHOLA ", " CANTA ", " CORALI", " CHORUS", " GLASBENA", " U S C I "):
        return "Musica, cori e bande"
    if ha(" ASD ", " A S D ", " SSD ", " SPORTIVA", " POLISPORTIVA", " CALCIO", " VOLLEY", " MOTOCLUB",
          " BOCCE", " BOCCIOFILA", " ATLETICA", " CANOA", " CICLO", " BIKE", " TRIATHLON", " PALLACANESTRO",
          " BASEBALL", " SOFTBALL", " UISP ", " SCI CLUB", " TRAIL", " GYM ", " APNEA ", " NAUTIC",
          " TIRO A VOLO", " CLUB ALPINO", " CAI ", " SPORT", " PATTINAGGIO", " RACING", " SOCCER",
          " TRI TEAM", " FUORISTRADA", " BASKET", " DANZA", " DANCE", " FIAB ", " PEDALE "):
        return "Sport"
    if ha(" ODV ", " O D V ", " VOLONTARIATO", " ONLUS", " GENITORI", " TERZA ETA", " MALATO", " CIECHI",
          " AUTISMO", " ACCOGLIENZA", " ANDOS ", " A N D O S ", " DONATORI", " BENESSERE", " CUORE "):
        return "Sociale e volontariato"
    if ha(" CULTURA", " TEATR", " CIRCOLO", " ACCADEMIA", " MUSEO", " FOLK", " STORIC", " FILOLOGICA",
          " CINEMA", " FOTOGRAF", " ECOMUSEO", " ARTE", " ARTS", " SCRITTORI", " KULTURNI", " FONDAZIONE",
          " UNIVERSITA", " STUDI", " FILATELICO", " TRADIZIONAL", " RICREATIV", " FOLCLOR", " STORIA ",
          " ARTISTIC", " ARCI ", " DRAMMA"):
        return "Cultura, teatro e tradizioni"
    return "Altro o non classificabile"


def forma(nome):
    s = " " + re.sub(r"[^A-Z ]", " ", unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode().upper()) + " "
    s = re.sub(r"\s+", " ", s)
    def ha(*p):
        return any(x in s for x in p)
    if ha(" PARROCCHIA"):
        return "Parrocchia"
    if ha(" ASD ", " A S D ", " SSD ", " SPORTIVA DILETTANTISTICA", " POLISPORTIVA DILETTANTISTICA"):
        return "ASD (Associazione sportiva dilettantistica)"
    if ha(" APS ", " A P S ", " PROMOZIONE SOCIALE"):
        return "APS (Associazione di promozione sociale)"
    if ha(" ODV ", " O D V ", " ORGANIZZAZIONE DI VOLONTARIATO"):
        return "ODV (Organizzazione di volontariato)"
    if ha(" FONDAZIONE "):
        return "Fondazione"
    if ha(" ETS ", " ONLUS ", " TERZO SETTORE"):
        return "ETS (Ente del Terzo settore) o ONLUS"
    return "Forma non indicata nel nome"


def main():
    comuni, indice = carica_geo()
    pop = carica_pop()
    wb = openpyxl.load_workbook(XLSX, data_only=True)

    # ---------- Foglio1: riepilogo per Comune ----------
    ws = wb["Foglio1"]
    righe = list(ws.iter_rows(min_row=4, values_only=True))
    per_comune = {c: {"c": c, "n": v["n"], "p": v["p"], "pop": pop.get(c), "k": v["k"], "a": {}} for c, v in comuni.items()}
    fuori = []  # comuni fuori regione
    totali_foglio = {}
    for anno in ANNI:
        o = OFFSET[anno]
        for r in righe:
            nome = r[o]
            if nome is None:
                continue
            if str(nome).strip().upper() == "TOTALE":
                totali_foglio[anno] = round(float(r[o + 3]), 2)
                break
            prov, num, imp = r[o + 1], r[o + 2], r[o + 3]
            if not isinstance(num, (int, float)):
                continue
            cod = trova(indice, nome)
            if cod is None:
                fuori.append({"n": str(nome).title(), "p": prov, "anno": anno, "num": int(num), "imp": round(float(imp), 2)})
                continue
            if per_comune[cod]["p"] != prov:
                sys.exit(f"Provincia diversa per {nome}: {prov} / {per_comune[cod]['p']}")
            per_comune[cod]["a"][str(anno)] = [int(num), round(float(imp), 2)]

    # verifica totali
    for anno in ANNI:
        s = sum(v["a"].get(str(anno), [0, 0])[1] for v in per_comune.values()) + sum(f["imp"] for f in fuori if f["anno"] == anno)
        if abs(s - totali_foglio[anno]) > 0.05:
            sys.exit(f"Totale {anno} non torna: {s} contro {totali_foglio[anno]}")
        print(f"{anno}: totale verificato {s:,.2f}")

    # ---------- beneficiari 2026 ----------
    wsb = wb["beneficiari 2026"]
    ben = []
    for r in wsb.iter_rows(min_row=2, values_only=True):
        if r[0] is None:
            continue
        num, ist, dtr, dpr, npr, den, cf, tit, dec, ddec, imp, com, prov = r[:13]
        cod = trova(indice, com)
        cfs = str(cf).strip() if cf is not None else ""
        ben.append({
            "n": int(num), "i": ist, "dt": dtr.strftime("%Y-%m-%d %H:%M") if isinstance(dtr, datetime) else None,
            "dp": iso(dpr), "np": npr, "d": str(den).strip(), "cf": cfs,
            "cfok": bool(re.fullmatch(r"\d{11}|[A-Z0-9]{16}", cfs.upper())),
            "t": str(tit).strip() if tit else "", "dn": str(dec).strip(), "dd": iso(ddec),
            "e": round(float(imp), 2), "cm": str(com).strip(), "pv": prov, "c": cod,
            "ty": tipologia(str(den)), "fg": forma(str(den)),
        })
    s_ben = round(sum(b["e"] for b in ben), 2)
    if abs(s_ben - totali_foglio[2026]) > 0.05:
        sys.exit(f"Totale beneficiari {s_ben} diverso dal riepilogo {totali_foglio[2026]}")
    print(f"beneficiari 2026: {len(ben)} righe, totale verificato {s_ben:,.2f}")
    # coerenza per Comune con il Foglio1
    agg = {}
    for b in ben:
        if b["c"]:
            a = agg.setdefault(b["c"], [0, 0.0])
            a[0] += 1
            a[1] += b["e"]
    for c, (n, e) in agg.items():
        rif = per_comune[c]["a"].get("2026")
        if rif is None or rif[0] != n or abs(rif[1] - e) > 0.05:
            sys.exit(f"Incoerenza 2026 per {c}: {rif} contro {(n, e)}")
    print("beneficiari 2026 coerenti con il riepilogo per Comune")

    geo = {c: v["g"] for c, v in comuni.items()}
    gp = json.loads((DATI / "province_fvg_semplificate.geojson").read_text(encoding="utf-8"))
    province = {}
    for f in gp["features"]:
        g = f["geometry"]
        polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
        province[f["properties"]["prov_acr"]] = [[[[round(x, 4), round(y, 4)] for x, y in r] for r in poly] for poly in polys]
    meta = {
        "fonte": "Consiglio regionale del Friuli Venezia Giulia, contributi: file CONTRIBUTO_CONSIGLIO_REGIONALE_2026_2025_2024_05112026.xlsx (estrazione del 5 novembre 2026)",
        "pop": "ISTAT, popolazione residente al 1° gennaio 2025 (demo.istat.it)",
        "fonte_breve": "Fonte: Consiglio regionale del Friuli Venezia Giulia, estrazione del 5 novembre 2026; popolazione ISTAT (Istituto nazionale di statistica) al 1° gennaio 2025.",
        "confini": "Confini comunali: openpolis, geojson-italy (dati ISTAT), semplificati",
        "totali": totali_foglio,
        "generato": datetime.now().strftime("%d/%m/%Y"),
    }
    dati = {"meta": meta, "comuni": list(per_comune.values()), "fuori": fuori, "ben": ben, "geo": geo, "prov": province}

    def parti(nome):
        v = (MODELLI / nome).read_text(encoding="utf-8")
        i = v.index("<script>")
        return v[:i].rstrip(), v[i:].strip()

    mc, sc = parti("vista-comuni.html")
    mb, sb = parti("vista-beneficiari.html")
    t = (MODELLI / "pagina.html").read_text(encoding="utf-8")
    t = t.replace("/*CSS*/", (MODELLI / "comune.css").read_text(encoding="utf-8"))
    t = t.replace("/*JS_COMUNE*/", (MODELLI / "comune.js").read_text(encoding="utf-8"))
    t = t.replace("/*VISTA_COMUNI*/", mc).replace("/*VISTA_BENEFICIARI*/", mb)
    t = t.replace("/*SCRIPT_VISTE*/", sc + "\n" + sb)
    t = t.replace("/*DATI*/", "window.DATI=" + json.dumps(dati, ensure_ascii=False, separators=(",", ":")) + ";")
    (BASE / "index.html").write_text(t, encoding="utf-8")
    print(f"scritto index.html ({len(t)//1024} kB)")


if __name__ == "__main__":
    main()
