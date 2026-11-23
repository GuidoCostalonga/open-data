# Geografia del Friuli Venezia Giulia

Raccolta di dati geografici del FVG (Friuli Venezia Giulia) in formato GeoJSON, con una mappa interattiva per consultarli.

| Voce | Valore |
|---|---|
| Livelli | 192 |
| Elementi geografici | 2.287.090 |
| File GeoJSON | 829 |
| Sistema di coordinate | WGS84, longitudine e latitudine (EPSG:4326) |
| Data di estrazione | 22 novembre 2026 |

L'elenco completo, livello per livello, è in [ELENCO_LIVELLI.md](ELENCO_LIVELLI.md) e in `elenco_livelli.xlsx`.

## Che cosa contiene

| Gruppo | Livelli | Esempi |
|---|---:|---|
| Confini amministrativi | 33 | regione, ex province, 215 comuni, Comunità di montagna, aziende e distretti sanitari, ambiti del Servizio sociale dei Comuni, sezioni di censimento, comuni censuari, confine di Stato, comuni confinanti di Veneto, Austria e Slovenia |
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
| `dati/fvg_unico.geojson` | File unico con 150 livelli alleggeriti; ogni elemento riporta `livello`, `gruppo`, `titolo_livello` e `fonte` |
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

`dati/fvg_unico.geojson` (89 MB) riunisce i 150 livelli la cui versione leggera pesa fino a 2,5 megabyte. Il file con tutti i 190 livelli alleggeriti pesa oltre 400 megabyte e non può stare su GitHub; si genera sul proprio computer con:

```bash
python3 strumenti/alleggerisci.py dati --unico-completo
```

## Fonti e licenze

| Fonte | Livelli | Che cosa fornisce | Licenza |
|---|---:|---|---|
| Regione autonoma FVG, catalogo IRDAT (Infrastruttura regionale di dati ambientali e territoriali) | 129 | confini, idrografia, aree protette, edifici, strade, numeri civici, piano paesaggistico | IODL 2.0 (Italian Open Data License) |
| Unione dei comuni secondo la composizione ufficiale degli enti | 5 | Comunità di montagna, Comunità collinare, ambiti del Servizio sociale dei Comuni, distretti e aziende sanitarie | IODL 2.0 per le forme dei comuni; composizione da atti pubblici |
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

## Enti sovracomunali ricostruiti dai comuni

Questi perimetri non sono pubblicati come dato geografico: sono ottenuti unendo i comuni della Regione secondo la composizione ufficiale di ogni ente. Ogni elemento riporta l'elenco dei comuni, i codici ISTAT e la fonte della composizione.

| Livello | Elementi | Fonte della composizione |
|---|---:|---|
| Comunità di montagna | 6 | statuti pubblicati sul portale regionale delle autonomie locali; legge regionale 29 novembre 2019, n. 21, articolo 17 |
| Comunità collinare del Friuli | 1 | legge regionale 29 novembre 2019, n. 21, articolo 21, comma 1 |
| Ambiti del Servizio sociale dei Comuni | 18 | pagina della Regione FVG sugli enti gestori, aggiornata al 31 gennaio 2025 |
| Distretti sanitari | 18 | atti aziendali delle tre aziende sanitarie |
| Aziende sanitarie | 3 | unione dei rispettivi distretti |

Controlli svolti: i 18 ambiti coprono tutti i 215 comuni, ciascuno una sola volta; le tre aziende corrispondono alle ex province (Udine 134 comuni, Pordenone 50, Gorizia e Trieste 31).

Punti da tenere presenti:

- **Distretti di Pordenone:** l'atto aziendale dice che ogni distretto coincide con l'ambito territoriale omonimo, senza elencare i comuni. L'elenco è quello dell'ambito del Servizio sociale dei Comuni corrispondente.
- **Distretti di Trieste:** il capoluogo è diviso tra due distretti secondo le circoscrizioni comunali, prese da OpenStreetMap. La fonte è l'atto aziendale adottato con decreto n. 454 del 19 maggio 2022, tuttora quello pubblicato dall'azienda; i quattro distretti (Trieste 1, Trieste 2, Alto Isontino, Basso Isontino) sono confermati dall'organigramma del 2 luglio 2026. Le modifiche successive all'atto (decreti n. 925 dell'8 novembre 2023, n. 767 del 4 ottobre 2024, n. 322 del 16 aprile 2025 e n. 496 del 12 giugno 2025) riguardano altre strutture e non toccano i distretti.
- **Comunità di montagna:** la composizione è quella degli statuti pubblicati; *eventuali adesioni o recessi successivi sono DA VERIFICARE*.

## Livelli non disponibili

| Livello | Motivo |
|---|---|
| Ispettorati forestali | il servizio regionale restituisce un file danneggiato |
| Edifici di OpenStreetMap | esclusi per non duplicare gli edifici ufficiali della Regione |

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
python3 strumenti/costruisci.py LAVORO dati comuni osm_frazioni_confini
```

```bash
python3 strumenti/prepara_enti.py dati LAVORO/intermedi
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

La mappa viene pubblicata su GitHub Pages dal flusso `.github/workflows/pagine.yml` a ogni aggiornamento del ramo principale. GitHub Pages ammette siti fino a 1 GB, quindi il sito pubblicato contiene la pagina, l'indice e i file leggeri (circa 0,5 GB); edifici, numeri civici e file integrali da scaricare vengono letti direttamente dal deposito.

Sul proprio computer la pagina va aperta avviando un piccolo servizio locale nella cartella `geografia-fvg`:

```bash
python3 -m http.server 8000
```

e poi aprendo `http://localhost:8000/` nel navigatore.
