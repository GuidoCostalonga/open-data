"""Dati aggiuntivi dell'Atlante: territori NUTS Eurostat (lotti 1 e 2) e archivi parziali (lotti 5, 9, 11, 15, 18).

Chiamato da genera_dati.py con --eurostat e --parziali (file prodotti da estrai_eurostat.py
ed estrai_archivi_parziali.py).
"""
import json, os, re

TEMA_EU = 'eur'
NOME_TEMA_EU = 'Demografia regionale europea (Eurostat)'

ETA = {'TOTAL': None, 'Y_LT15': 'sotto i 15 anni', 'Y15-64': 'da 15 a 64 anni', 'Y_GE65': 'di 65 anni e oltre', 'UNK': 'età non nota'}
SESSO = {'T': None, 'M': 'uomini', 'F': 'donne'}
FIND3 = {
    'TOTFERRT': ('Figli per donna, regioni europee', 'nati per donna', 'Total fertility rate'),
    'AGEMOTH': ('Età media delle madri al parto', 'anni', 'Mean age of women at childbirth'),
    'MEDAGEMOTH': ('Età mediana delle madri al parto', 'anni', 'Median age of women at childbirth'),
}
DATASET_EU = {
    'demo_r_d3dens': ('Population density by NUTS 3 region', 1),
    'demo_r_pjanaggr3': ('Population on 1 January by broad age group, sex and NUTS 3 region', 1),
    'demo_r_births': ('Live births (total) by NUTS 3 region', 2),
    'demo_r_deaths': ('Deaths (total) by NUTS 3 region', 2),
    'demo_r_find3': ('Fertility indicators by NUTS 3 region', 2),
}
STATI_EU = {'b': 'interruzione della serie', 'c': 'riservato', 'd': 'definizione diversa', 'e': 'stimato',
            'f': 'previsione', 'n': 'non significativo', 'p': 'provvisorio', 'r': 'rivisto', 's': 'stima di Eurostat',
            'u': 'bassa affidabilità', 'z': 'non applicabile', ':': 'non disponibile'}
ISO3_EXTRA = {'UK': 'GBR', 'EL': 'GRC'}
AGG_EU_IT = {'DE_TOT': 'Germania, compresa l’ex RDT (Repubblica democratica tedesca)',
             'EFTA': 'Associazione europea di libero scambio (EFTA)', 'EU27_2007': 'Unione europea a 27 (2007/2013)',
             'EU27_2020': 'Unione europea a 27 (dal 2020)', 'EU28': 'Unione europea a 28 (2013/2020)'}

# Nomi italiani dei dataset degli archivi parziali (dal catalogo FAOSTAT e OCSE)
DATASET_IT = {
    'CB': 'Bilanci delle merci non alimentari', 'EI': 'Intensità delle emissioni agroalimentari',
    'EK': 'Caratteristiche degli allevamenti', 'ESB': 'Bilancio dei nutrienti nei terreni coltivati',
    'FA': 'Spedizioni di aiuti alimentari del PAM (archivio storico)', 'RFB': 'Fertilizzanti per prodotto',
    'RFN': 'Fertilizzanti per nutriente', 'EM': 'Indicatori delle emissioni agroalimentari',
    'GPP': 'Emissioni prima e dopo la produzione agricola', 'SUA': 'Disponibilità alimentare da bilanci di utilizzo',
    'EMN': 'Letame degli allevamenti', 'GFDI': 'Quote di valore della filiera alimentare',
    'PA': 'Prezzi alla produzione (archivio storico)', 'FT': 'Flussi commerciali forestali (archivio storico)',
    'QV': 'Valore della produzione agricola',
    'DSD_EAG_LSO_EA@DF_LSO_NEAC_DISTR_EA': 'Adulti per titolo di studio, età e sesso',
    'DSD_EAG_LSO_EA@DF_LSO_NEAC_DISTR_GENDER': 'Adulti per sesso, titolo di studio ed età',
    'DSD_EAG_UOE_NON_FIN_PERS@DF_UOE_NF_PERS_RAW_INST2': 'Assistenti degli insegnanti',
}
STORICI_IT = {'TWN': 'Taiwan', 'AIA': 'Anguilla', 'SHN': 'Ascensione, Sant’Elena e Tristan da Cunha',
              'BES': 'Bonaire, Sint Eustatius e Saba', 'COK': 'Isole Cook', 'FAO_351': 'Cina (totale FAOSTAT)',
              'FAO_357': 'Cina, esclusi Hong Kong e Macao', 'FAO_15': 'Belgio e Lussemburgo (codice storico FAOSTAT)',
              'FAO_259': 'Isole del Canale'}
UNITA_IT = {
    '1000 USD': 'migliaia di dollari USA', 't': 'tonnellate', 'mg/cap/d': 'mg per persona al giorno', 'm3': 'm³',
    'PT_POP_SEX_AGE': '% della popolazione dello stesso sesso ed età', 'PT_POP_SUB': '% del sottogruppo di popolazione',
    'g/cap/d': 'g per persona al giorno', 'kt': 'migliaia di tonnellate', 'μg/cap/d': 'µg per persona al giorno',
    'kg/ha': 'kg per ettaro', '1000 SLC': 'migliaia in valuta locale standard', 'million USD': 'milioni di dollari USA',
    'TJ': 'terajoule', '1000 Int$': 'migliaia di dollari internazionali', 't CO2eq/cap': 't di CO₂ equivalente per abitante',
    'LCU': 'valuta locale', 'kcal/cap/d': 'kcal per persona al giorno', 'million LCU': 'milioni in valuta locale',
    'million SLC': 'milioni in valuta locale standard', '%LSU': '% delle unità di bestiame adulto', 'LSU': 'unità di bestiame adulto',
    'LSU/ha': 'unità di bestiame adulto per ettaro', 'kg CO2eq/kg': 'kg di CO₂ equivalente per kg di prodotto', 'An': 'capi',
    'PS': 'persone', 't CO2eq/ha': 't di CO₂ equivalente per ettaro', 'kg CO2eq/Int$': 'kg di CO₂ equivalente per dollaro internazionale',
    'kg/cap': 'kg per persona', 'g/Int$': 'g per dollaro internazionale', 'PS_FTE': 'persone equivalenti a tempo pieno',
}
LOTTO_ARCHIVIO = {5: 'archivio 9 di 11', 9: 'archivio 1 di 6', 11: 'archivio 1 di 5', 15: 'archivio 2 di 9', 18: 'archivio 2 di 22'}
FONTE_LOTTO = {5: 'OCSE (Organizzazione per la cooperazione e lo sviluppo economico)', 9: 'FAOSTAT', 11: 'FAOSTAT', 15: 'FAOSTAT', 18: 'FAOSTAT'}


def _scrivi(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump(obj, f, separators=(',', ':'), ensure_ascii=False)


def _serie_annuale(per_terr, arrotonda, interi):
    anni = sorted({int(y) for t in per_terr.values() for y, v in t.items() if v[0] is not None})
    if not anni:
        return None
    y0, y1 = anni[0], anni[-1]
    dati = {}
    for c, t in per_terr.items():
        arr = [arrotonda(t.get(str(y), [None])[0], interi) for y in range(y0, y1 + 1)]
        if any(x is not None for x in arr):
            dati[c] = arr
    return y0, y1, dati


def eurostat(percorso, uscita, territori, arrotonda):
    """Aggiunge territori NUTS e indicatori Eurostat; restituisce l'elenco degli indicatori."""
    d = json.load(open(percorso))
    geo = json.load(open(os.path.join(uscita, 'nuts.topo.json')))
    iso3 = {}
    for g in geo['objects'][next(iter(geo['objects']))]['geometries']:
        p = g['properties']
        if p['l'] == 0:
            iso3[p['id']] = p['c']
    iso3.update(ISO3_EXTRA)
    per_id = {t['id']: t for t in territori}
    con_geo = {g['properties']['id'] for g in geo['objects'][next(iter(geo['objects']))]['geometries']}
    for cod, (nome, liv) in sorted(d['territori'].items()):
        paese = iso3.get(cod[:2])
        if liv == 'Aggregato' or not re.match(r'^[A-Z]{2}[0-9A-Z]{0,3}$', cod) or not paese:
            territori.append({'id': 'EU:' + cod, 'n': AGG_EU_IT.get(cod, nome), 'en': nome, 'k': 'agg_eu', 'cod': cod})
            continue
        l = len(cod) - 2
        base = per_id.get(paese)
        n_it = base['n'] if (l == 0 and base) else nome
        territori.append({'id': 'EU:' + cod, 'n': n_it, 'en': nome, 'k': 'nuts', 'l': l, 'p': paese, 'cod': cod,
                          'r': base.get('r') if base else None, 'g': cod in con_geo})

    def scrivi(ident, per_terr, nome, unita, ds, en, extra=None):
        # chiavi territoriali con prefisso EU:
        pt = {'EU:' + c: t for c, t in per_terr.items()}
        interi = all(float(v[0]).is_integer() for t in pt.values() for v in t.values() if v[0] is not None)
        y = _serie_annuale(pt, arrotonda, interi)
        if not y:
            return None
        y0, y1, dati = y
        _scrivi(os.path.join(uscita, 'eurostat', ident + '.json'), {'c': ident, 'y0': y0, 'y1': y1, 'd': dati})
        note = {}
        for c, t in pt.items():
            for anno, v in t.items():
                if v[1]:
                    note.setdefault(c, {})[anno] = [STATI_EU.get(v[1].strip(), v[1]), None]
        if note:
            _scrivi(os.path.join(uscita, 'note', ident + '.json'), note)
        nome_ds, lotto = DATASET_EU[ds]
        voce = {'c': ident, 'fam': 'eu', 't': TEMA_EU, 'n': nome, 'u': unita, 'en': en,
                'def': f'Dataset Eurostat {ds}: {nome_ds}.', 'org': 'Eurostat',
                'agg': (d['agg'].get(ds) or '')[:10], 'url': f'https://ec.europa.eu/eurostat/databrowser/view/{ds}/default/table?lang=it',
                'y0': y0, 'y1': y1, 'righe': sum(len(t) for t in pt.values()),
                'valori': sum(1 for t in pt.values() for v in t.values() if v[0] is not None),
                'interi': interi, 'note': bool(note), 'lotto': lotto, 'ds': ds}
        if extra:
            voce.update(extra)
        return voce

    indicatori = []
    S = d['serie']
    for chiave, per_terr in S.items():
        parti = chiave.split('|')
        ds = parti[0]
        if ds == 'demo_r_d3dens':
            v = scrivi('EU_DENS', per_terr, 'Densità di popolazione, regioni europee', 'abitanti per km²', ds, 'Population density')
        elif ds == 'demo_r_pjanaggr3':
            sesso, eta = parti[2], parti[3]
            pezzi = ['Popolazione al 1° gennaio'] + [x for x in (ETA[eta], SESSO[sesso]) if x]
            v = scrivi(f'EU_POP_{sesso}_{eta.replace("-", "")}', per_terr, ', '.join(pezzi), 'persone', ds,
                       f'Population on 1 January, sex {sesso}, age {eta}')
        elif ds == 'demo_r_births':
            v = scrivi('EU_NATI', per_terr, 'Nati vivi', 'nati nell’anno', ds, 'Live births')
        elif ds == 'demo_r_deaths':
            v = scrivi('EU_MORTI', per_terr, 'Decessi', 'decessi nell’anno', ds, 'Deaths')
        elif ds == 'demo_r_find3':
            n, u, en = FIND3[parti[4]]
            v = scrivi('EU_' + parti[4], per_terr, n, u, ds, en)
        else:
            continue
        if v:
            indicatori.append(v)

    # Quote per età calcolate dall'Atlante: stessa fonte, stesso territorio, stesso anno
    tot = S['demo_r_pjanaggr3|NR|T|TOTAL']
    for eta, nome in (('Y_LT15', 'sotto i 15 anni'), ('Y15-64', 'da 15 a 64 anni'), ('Y_GE65', 'di 65 anni e oltre')):
        num = S[f'demo_r_pjanaggr3|NR|T|{eta}']
        quota = {}
        for c, t in num.items():
            for anno, v in t.items():
                den = tot.get(c, {}).get(anno)
                if v[0] is not None and den and den[0]:
                    quota.setdefault(c, {})[anno] = [round(100 * v[0] / den[0], 4), None]
        v = scrivi(f'EU_QUOTA_{eta.replace("-", "")}', quota, f'Quota di popolazione {nome}', '% della popolazione al 1° gennaio',
                   'demo_r_pjanaggr3', f'Share of population, age {eta} (computed)',
                   {'calc': f'Calcolato dall’Atlante: popolazione {nome} divisa per popolazione totale, stesso territorio e stesso anno, per 100.'})
        if v:
            indicatori.append(v)
    return indicatori, NOME_TEMA_EU


def archivi(percorso, uscita, territori, arrotonda):
    """Catalogo degli archivi parziali: un file per dataset con tutte le serie e i territori presenti."""
    d = json.load(open(percorso))
    per_id = {t['id']: t for t in territori}
    catalogo = []
    for chiave, ds in sorted(d.items(), key=lambda x: (int(x[0].split('|')[0]), x[0])):
        lotto, codice = chiave.split('|')
        lotto = int(lotto)
        terr = {}
        for c, nome in ds['terr'].items():
            if c not in per_id:
                nuovo = {'id': c, 'n': STORICI_IT.get(c, nome), 'en': nome, 'k': 'storico'}
                territori.append(nuovo)
                per_id[c] = nuovo
            terr[c] = nome
        # l'identità SHA256 della fonte comprende il territorio: si raggruppano le serie per descrizione e unità,
        # tenendo separate due identità diverse che cadrebbero sullo stesso territorio
        gruppi = {}
        for ident, s in ds['serie'].items():
            # toglie dall'etichetta il nome del territorio, presente in alcune fonti (es. paese beneficiario in FA)
            nomi = {str(ds['terr'][c]) for c in s['d']}
            s['l'] = ' · '.join(x for x in s['l'].split(' · ') if x not in nomi)
            if codice == 'FT' and s['l']:
                s['l'] = 'Paese partner ' + s['l']
            k = (s['l'], s['u'])
            elenco = gruppi.setdefault(k, [])
            for g in elenco:
                if not set(g['d']) & set(s['d']):
                    g['d'].update(s['d'])
                    break
            else:
                elenco.append({'l': s['l'], 'u': s['u'], 'd': dict(s['d'])})
        serie = []
        for s in (g for elenco in gruppi.values() for g in elenco):
            pt = s['d']
            interi = all(float(v[0]).is_integer() for t in pt.values() for v in t.values() if v[0] is not None)
            y = _serie_annuale(pt, arrotonda, interi)
            if not y:
                continue
            y0, y1, dati = y
            serie.append({'l': s['l'] or codice, 'u': UNITA_IT.get(s['u'], s['u'] or ''), 'uo': s['u'] or '', 'y0': y0, 'y1': y1, 'd': dati, 'i': interi})
        serie.sort(key=lambda s: (s['l'], s['u']))
        nome_file = f'L{lotto:02d}_{re.sub(r"[^A-Za-z0-9]+", "_", codice)}'
        _scrivi(os.path.join(uscita, 'archivi', nome_file + '.json'), {'s': serie})
        catalogo.append({
            'f': nome_file, 'lotto': lotto, 'cod': codice, 'n': DATASET_IT.get(codice, ds['n']), 'en': ds['n'],
            'fonte': FONTE_LOTTO[lotto], 'archivio': LOTTO_ARCHIVIO[lotto], 'url': ds['url'], 'agg': (ds['agg'] or '')[:10],
            'terr': sorted(terr), 'serie': len(serie),
            'y0': min(s['y0'] for s in serie), 'y1': max(s['y1'] for s in serie),
        })
    return catalogo
