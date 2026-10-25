# Atlante dei dati

Sito di esplorazione di tutti i valori contenuti nel repository, con sei viste sincronizzate: Mappa, Bolle, Linee, Barre, Tabella e Confronta.

## Contenuto

| Famiglia | Fonte | Lotti | Copertura nel repository |
|---|---|---|---|
| Indicatori nazionali | Banca Mondiale, WDI (Indicatori di sviluppo mondiale): 150 indicatori | 1 e 2 | completa: 217 paesi e 49 aggregati, dal 1960 |
| Regioni europee | Eurostat, 5 dataset demografici per territorio NUTS: 21 serie più 3 quote per età calcolate | 1 e 2 | completa: 37 paesi, livelli NUTS da 0 a 3, dal 1990 |
| Archivi parziali | FAOSTAT (15 insiemi di dati) e OCSE (3 flussi) | 5, 9, 11, 15, 18 | parziale: nel repository c'è un solo archivio per lotto, quindi solo alcuni paesi |

I lotti 3, 4, 6, 7, 8, 10, 12, 13, 14, 16 e 17 sono presenti solo con indici, registri o guide, senza valori: l'Atlante li elenca nella finestra "Fonti e metodo" ma non può mostrarli.

Mappe: Natural Earth 1:50 milioni (paesi, continenti, regioni del mondo) e GISCO NUTS 2024 1:10 milioni (regioni europee, © EuroGeographics per i confini amministrativi).

## Funzioni

- **Mappe per continente**: Mondo, Europa, Africa, Asia, America settentrionale e centrale, America meridionale, Oceania.
- **Mappe regionali europee**: con un indicatore Eurostat si sceglie il livello (paesi, macroregioni, regioni, province) e il paese.
- **Confronta**: righe = indicatori di un gruppo, colonne = territori selezionati (paesi, aggregati, regioni). Un paese mostra anche i dati Eurostat nazionali.
- **Confronti pronti**: Friuli Venezia Giulia e vicini, province del Friuli Venezia Giulia, Italia e grandi paesi europei, regioni del mondo.
- **Archivi parziali**: ricerca fra le serie FAOSTAT e OCSE; la serie scelta si apre in tutte le viste.

## Aprire il sito

```
cd atlante
python3 -m http.server 8000
```

poi aprire `http://localhost:8000`.

## Struttura

| Percorso | Contenuto |
|---|---|
| `index.html`, `stile.css`, `app.js` | pagina, stile e logica delle viste |
| `dati/meta.json` | indicatori, territori (paesi, aggregati, regioni NUTS, codici storici FAOSTAT), regioni del mondo, catalogo degli archivi |
| `dati/indicatori/<codice>.json` | Banca Mondiale: valori annuali per territorio; `null` = dato mancante |
| `dati/eurostat/<codice>.json` | Eurostat: valori annuali per territorio NUTS (chiavi `EU:<codice NUTS>`) |
| `dati/archivi/<lotto>_<insieme>.json` | archivi parziali: tutte le serie di un insieme di dati |
| `dati/note/<codice>.json` | note e stati originali della fonte per osservazione |
| `dati/mondo.topo.json`, `dati/nuts.topo.json` | confini semplificati |
| `strumenti/` | script di estrazione e generazione |

## Regole sui valori

- Nessun valore stimato, interpolato o ricostruito; i dati mancanti restano tali e sono contati in ogni vista.
- Unica elaborazione: le quote di popolazione per età Eurostat (classe d'età divisa per totale, stesso territorio e anno, per 100), indicate come calcolate.
- Negli archivi FAOSTAT l'identità SHA256 della fonte comprende il territorio: le serie sono raggruppate per descrizione e unità per confrontare i paesi.
- Decimali arrotondati a 6 cifre significative per la visualizzazione; conteggi interi esatti.

## Rigenerare i dati

```
cd atlante/strumenti
# 1. decomprimere gli ZIP dei lotti 1 e 2 in una cartella (PAESI/ e AGGREGATI/)
python3 estrai_eurostat.py <cartella lotti 1-2> /tmp/eurostat.json
# 2. decomprimere gli ZIP dei lotti 5, 9, 11, 15, 18 in <cartella>/L5, L9, L11, L15, L18
python3 estrai_archivi_parziali.py <cartella> /tmp/parziali.json
# 3. generare i file del sito
python3 genera_dati.py --cache /tmp/grezzi.json --eurostat /tmp/eurostat.json --parziali /tmp/parziali.json
```

Confini NUTS: scaricare da GISCO `NUTS_RG_10M_2024_4326_LEVL_{0,1,2,3}.json`, ridurre le proprietà a `id`, `n`, `l`, `c` (codice ISO3 del paese) e unire con `mapshaper -simplify 35% keep-shapes -o format=topojson quantization=1e5`.
