# Contributi del Consiglio regionale FVG

Un solo file, `index.html`, che si apre con un doppio clic e funziona anche senza connessione (serve la rete solo per i caratteri tipografici). Ha due sezioni, scelte con i pulsanti in alto a destra:

| Sezione | Indirizzo | Contenuto |
|---|---|---|
| Comuni 2024 · 2026 | `index.html#comuni` | Contributi per Comune 2024, 2025 e 2026: mappa, filtri, confronti fra anni, classifiche, tabella completa |
| Beneficiari 2026 | `index.html#beneficiari` | I 578 contributi 2026 uno per uno: beneficiario, codice fiscale, iniziativa, decreto, date, importo |

## Sezione Comuni (`#comuni`)

- **Periodo**: 2024, 2025, 2026 o triennio; **confronto** fra due anni con mappa a colori divergenti (aumenti in blu, cali in rosso).
- **Indicatore sulla mappa**: importo, numero di contributi, importo per abitante, contributi ogni 10.000 abitanti, importo medio. I cerchi arancioni mostrano il numero di contributi.
- **Filtri**: provincia (anche «fuori regione»), dimensione del Comune, Comuni con o senza contributi, Comuni presenti in tutti e tre gli anni, Comuni nuovi nel 2026, intervallo di importo, intervallo di numero, ricerca per nome; si filtra anche toccando le colonne dei grafici.
- **Dettaglio del Comune**: tre anni a confronto, importo per abitante, posizione in regione, collegamento ai beneficiari 2026 del Comune.
- **Tabella** ordinabile ed esportabile in CSV (si apre in Excel).

## Sezione Beneficiari 2026 (`#beneficiari`)

- **Filtri**: ricerca libera (nome, iniziativa, codice fiscale, decreto), provincia, Comune della sede, settore, forma giuridica, fascia e intervallo di importo, mese della domanda, mese del decreto, intervallo di date del decreto, giorni fra protocollo e decreto.
- **Grafici** cliccabili: settore, forma giuridica, decreti per mese, domande per mese, fasce di importo, tempi, Comuni con più contributi.
- **Tabella** con pagine, ordinabile, esportabile in CSV con i soli beneficiari filtrati.
- Collegamento diretto a un Comune: `index.html#beneficiari-<codice ISTAT>` per i suoi beneficiari 2026 (es. `#beneficiari-093033` per Pordenone), `index.html#comuni-<codice ISTAT>` per il suo dettaglio 2024-2026 (es. `#comuni-093036` per Roveredo in Piano).

## Fonti e verifiche

| Dato | Fonte |
|---|---|
| Contributi | `dati/CONTRIBUTO_CONSIGLIO_REGIONALE_2026_2025_2024_05112026.xlsx` (Consiglio regionale FVG, estrazione del 5 novembre 2026) |
| Popolazione | ISTAT (Istituto nazionale di statistica), popolazione residente al 1° gennaio 2025, `dati/popolazione_istat_1gen2025_fvg.csv` |
| Confini | openpolis, geojson-italy (su dati ISTAT), semplificati con mapshaper: `dati/comuni_fvg_semplificati.geojson`, `dati/province_fvg_semplificate.geojson` |

Il generatore controlla ogni volta che:

- la somma per Comune coincida con il totale di ciascun anno (2024: 1.389.940,98 €; 2025: 2.112.522,53 €; 2026: 3.294.948,61 €);
- i 578 beneficiari 2026 sommino 3.294.948,61 € e coincidano, Comune per Comune, con il riepilogo del 2026.

Note sui dati:

- il Comune è quello della **sede del beneficiario**, non necessariamente il luogo dell'iniziativa;
- un contributo 2026 (1.513,70 €) va a una sede fuori regione, San Michele al Tagliamento (VE): è nei totali ma non sulla mappa;
- il codice fiscale della riga N. 280 (Trieste Flute Association) nel file di origine è «salin»: è segnalato come DA VERIFICARE;
- **settore** e **forma giuridica** sono ricavati automaticamente dalla denominazione: servono a orientarsi, non sono una classificazione ufficiale;
- gli indicatori per abitante usano la popolazione al 1° gennaio 2025 per tutti e tre gli anni.

## Aggiornare le dashboard

Sostituire il file Excel in `dati/` (stessa struttura dei fogli «Foglio1» e «beneficiari 2026»), aggiornare il nome del file in `strumenti/genera.py` se cambia, poi dalla cartella `contributi-consiglio-regionale`:

```bash
python3 strumenti/genera.py
```

I modelli sono in `strumenti/modelli/`: `pagina.html` (struttura e navigazione), `vista-comuni.html` e `vista-beneficiari.html` (le due sezioni), `comune.css` e `comune.js` (stile, mappa, grafici). Serve il pacchetto Python `openpyxl`.
