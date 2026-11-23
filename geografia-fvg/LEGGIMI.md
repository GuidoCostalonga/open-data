# Geografia del Friuli Venezia Giulia

Raccolta di dati geografici del FVG (Friuli Venezia Giulia) in formato GeoJSON, con una mappa interattiva per consultarli.

| Voce | Valore |
|---|---|
| Livelli | 187 |
| Elementi geografici | 2.287.044 |
| File GeoJSON | 819 |
| Sistema di coordinate | WGS84, longitudine e latitudine (EPSG:4326) |
| Data di estrazione | 22 novembre 2026 |

L'elenco completo, livello per livello, è in [ELENCO_LIVELLI.md](ELENCO_LIVELLI.md) e in `elenco_livelli.xlsx`.

## Che cosa contiene

| Gruppo | Livelli | Esempi |
|---|---:|---|
| Confini amministrativi | 28 | regione, ex province, 215 comuni, sezioni di censimento, comuni censuari, confine di Stato, comuni confinanti di Veneto, Austria e Slovenia |
| Acque | 39 | fiumi, torrenti, canali, laghi, laguna, linea di costa, bacini idrografici, sorgenti, idrovore |
| Monti e rilievo | 21 | curve di livello ogni 25 metri, cime con quota, passi, ghiacciai, grotte, geositi, frane |
| Natura e aree protette | 27 | parchi, riserve, biotopi, Natura 2000, boschi, prati stabili, uso del suolo, habitat |
| Strade, ferrovie, ciclovie e sentieri | 35 | grafo stradale, ferrovie, ciclovie regionali, sentieri del CAI (Club alpino italiano), impianti a fune |
| Centri abitati ed edifici | 14 | 772.028 edifici, 512.753 numeri civici, perimetri dei centri abitati, località |
| Servizi e luoghi di interesse | 23 | scuole, municipi, sanità, sicurezza ed emergenza, beni culturali, impianti sportivi |

## Come sono organizzati i file

| Percorso | Contenuto |
|---|---|
| `index.html` | Mappa interattiva con i livelli da accendere e spegnere |
| `dati/indice.json` | Indice di tutti i livelli: titolo, fonte, numero di elementi, campi, file |
| `dati/integrale/<gruppo>/` | Un file per livello alla massima precisione, senza semplificazione delle forme |
| `dati/leggero/<gruppo>/` | Gli stessi livelli semplificati, adatti a mappe in rete e dashboard |
| `dati/fvg_unico.geojson` | File unico con 145 livelli alleggeriti; ogni elemento riporta `livello`, `gruppo`, `titolo_livello` e `fonte` |
| `strumenti/` | Programmi che scaricano, costruiscono e verificano i dati |

### Due versioni per ogni livello

| Versione | Precisione delle coordinate | Semplificazione | Peso complessivo |
|---|---|---|---|
| Integrale | 7 decimali, circa 1 centimetro | nessuna | 2,1 GB |
| Leggera | 5 decimali, circa 1 metro | tolleranza di 10 metri, 25 metri per i livelli più pesanti | 0,45 GB |

Nella versione leggera le curve di livello sono solo quelle ogni 100 metri e vengono scartate le forme più corte di un metro (circa 4.500 elementi su 2,3 milioni).

### Livelli divisi in più file

GitHub non accetta file oltre i 100 megabyte, quindi i livelli più pesanti sono divisi:

| Livello | Divisione |
|---|---|
| Edifici, numeri civici | un file per comune (nome del file con il codice ISTAT del comune) |
| Curve di livello, grafo stradale, uso del suolo, boschi, tipologie forestali, habitat | un file per ex provincia (UD, PN, GO, TS) |

Edifici e numeri civici non hanno una versione leggera separata: la mappa usa direttamente i file per comune.

### Il file unico

`dati/fvg_unico.geojson` (87 MB) riunisce i 145 livelli la cui versione leggera pesa fino a 2,5 megabyte. Il file con tutti i 185 livelli alleggeriti pesa oltre 400 megabyte e non può stare su GitHub; si genera sul proprio computer con:

```bash
python3 strumenti/alleggerisci.py dati --unico-completo
```

## Fonti e licenze

| Fonte | Livelli | Che cosa fornisce | Licenza |
|---|---:|---|---|
| Regione autonoma FVG, catalogo IRDAT (Infrastruttura regionale di dati ambientali e territoriali) | 129 | confini, idrografia, aree protette, edifici, strade, numeri civici, piano paesaggistico | IODL 2.0 (Italian Open Data License) |
| OpenStreetMap e contributori | 48 | strade di ogni classe, sentieri, luoghi, servizi, uso del suolo, confine di Stato | ODbL (Open Database License) |
| ISTAT (Istituto nazionale di statistica) | 7 | confini al 1 gennaio 2026, comuni veneti confinanti, perimetri dei centri abitati 2021 | CC BY 4.0 (Creative Commons Attribuzione) |
| Eurostat GISCO | 1 | comuni sloveni confinanti | riuso con citazione della fonte, solo per fini non commerciali (© EuroGeographics) |
| Copernicus DEM GLO-30 | 1 | modello altimetrico da cui sono ricavate le curve di livello | uso libero con citazione della fonte |
| OpenStreetMap, estratto della Carinzia | 1 | comuni austriaci confinanti | ODbL |

Chi riusa i dati deve citare la fonte indicata nel campo `fonte` di ogni file. Per i livelli OpenStreetMap vale anche l'obbligo di condividere allo stesso modo le banche dati derivate.

## Avvertenze

- I confini di Regione FVG e ISTAT differiscono di poco perché nascono da rilievi a scala diversa: quelli regionali sono più dettagliati, quelli ISTAT sono aggiornati al 1 gennaio 2026.
- Le curve di livello derivano da un modello a maglia di 30 metri che descrive la superficie, compresi boschi ed edifici: in montagna sono affidabili, in pianura sono indicative. Le quote sono riferite al geoide EGM2008.
- I livelli OpenStreetMap contengono per intero gli elementi che attraversano il confine regionale (per esempio rotte dei traghetti ed elettrodotti).
- I perimetri dei centri abitati sono ottenuti unendo le sezioni di censimento 2021 e non riportano il nome della località.
- La data di aggiornamento di ogni livello regionale è quella del catalogo IRDAT; OpenStreetMap è aggiornato al 21 novembre 2026.

## Livelli richiesti e non disponibili

| Livello | Motivo |
|---|---|
| Comunità di montagna e Comunità collinare (assetto attuale) | non pubblicate come dato geografico nelle fonti consultate; è presente l'assetto storico delle comunità montane |
| Aziende sanitarie, distretti sanitari, ambiti dei servizi sociali | non pubblicati come dato geografico nelle fonti consultate |
| Ispettorati forestali | il servizio regionale restituisce un file danneggiato |
| Edifici di OpenStreetMap | esclusi per non duplicare gli edifici ufficiali della Regione |

Questi perimetri si possono ricostruire unendo i comuni, a partire da un elenco ufficiale dei comuni che compongono ogni ente.

## Come aggiornare i dati

Servono Python 3 con `geopandas`, `shapely`, `rasterio`, `contourpy`, `osmium`, `openpyxl` e il programma `mapshaper`.

```bash
python3 strumenti/scarica_regione.py LAVORO/fonti
```

```bash
python3 strumenti/estrai_osm.py LAVORO/fonti/osm/fvg.osm.pbf LAVORO/osm_out
```

```bash
python3 strumenti/prepara_confini.py LAVORO/fonti LAVORO/intermedi
```

```bash
python3 strumenti/prepara_localita.py LAVORO/fonti LAVORO/intermedi
```

```bash
python3 strumenti/curve_livello.py LAVORO/fonti LAVORO/intermedi
```

```bash
python3 strumenti/costruisci.py LAVORO dati
```

```bash
python3 strumenti/alleggerisci.py dati
```

```bash
python3 strumenti/verifica.py dati
```

```bash
python3 strumenti/scrivi_elenco.py dati .
```

Prima di cominciare vanno scaricati in `LAVORO/fonti`: l'estratto OpenStreetMap del FVG e della Carinzia (`osm/fvg.osm.pbf`, `osm/karnten.osm.pbf`, da download.openstreetmap.fr), i confini ISTAT (`istat/x/`), i quattro tasselli Copernicus (`dem/`) e le unità amministrative locali di Eurostat (`lau2024.geojson`).

La verifica controlla che ogni file sia GeoJSON valido, che i conteggi coincidano con l'indice, che i comuni siano 215 e le ex province 4, che nessun file superi il limite di peso.

## Come aprire la mappa

La pagina `index.html` legge i dati dalla cartella `dati`, quindi va aperta da un servizio in rete (per esempio GitHub Pages) oppure, sul proprio computer, avviando un piccolo servizio locale nella cartella:

```bash
python3 -m http.server 8000
```

e poi aprendo `http://localhost:8000/` nel navigatore.
