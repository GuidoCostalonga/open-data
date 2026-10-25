# Atlante dei dati

Sito di esplorazione dei dati del repository, con cinque viste sincronizzate: Mappa, Bolle, Linee, Barre e Tabella.

## Contenuto

- **Dati**: 150 indicatori WDI (Indicatori di sviluppo mondiale) della Banca Mondiale dai lotti 1 e 2, per 217 paesi ed economie e 49 aggregati; serie annuali dal 1960 al 2025 secondo l'indicatore.
- **Confini e regioni**: Natural Earth 1:50 milioni, versione 5.1.2 (campo `REGION_WB` per i colori delle regioni, `NAME_IT` per i nomi in italiano).
- **Non inclusi**: dati territoriali Eurostat (NUTS) e lotti successivi (FAOSTAT, OCSE, ONU, FMI).

## Aprire il sito

I dati sono letti con `fetch`, quindi serve un server web, anche locale:

```
cd atlante
python3 -m http.server 8000
```

poi aprire `http://localhost:8000`. Funziona anche con GitHub Pages puntato sulla cartella `atlante`.

## Struttura

| Percorso | Contenuto |
|---|---|
| `index.html`, `stile.css`, `app.js` | pagina, stile e logica delle viste |
| `dati/meta.json` | indicatori (etichette italiane, unità, periodo, fonte, aggiornamento), territori, regioni |
| `dati/indicatori/<codice>.json` | valori annuali per territorio; `null` = dato mancante |
| `dati/note/<codice>.json` | note originali della fonte per osservazione (79 indicatori) |
| `dati/mondo.topo.json` | confini semplificati |
| `strumenti/genera_dati.py` | rigenera `meta.json`, `indicatori/` e `note/` dagli ZIP di `open data` |
| `strumenti/etichette.py` | etichette italiane, unità e temi degli indicatori; nomi italiani degli aggregati |

## Regole sui valori

- Nessun valore stimato, interpolato o ricostruito: i dati mancanti restano tali e sono contati in ogni vista.
- L'opzione "ultimo dato disponibile" riporta il valore più recente dei 10 anni precedenti, mostrando sempre l'anno effettivo.
- Decimali arrotondati a 6 cifre significative per la visualizzazione; i conteggi interi restano esatti. I valori originali sono negli Excel dei lotti.

## Rigenerare i dati

```
cd atlante/strumenti
python3 genera_dati.py --cache /tmp/grezzi.json
```

Per rifare i confini: scaricare `ne_50m_admin_0_countries.geojson` (Natural Earth 5.1.2), ridurre le proprietà a `id` (codice Banca Mondiale), `n` (nome italiano), `r` (`REGION_WB`), `a2`, e semplificare con `mapshaper -simplify 18% keep-shapes -o format=topojson quantization=1e5`.
