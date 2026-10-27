# Open data internazionali: guida al lotto 16

Il lotto 16 aggiunge **1.623.453 osservazioni**, 54.592 identità di serie e 282 Excel dati. La raccolta cumulativa dei lotti 1–16 raggiunge 26.080.488 osservazioni, 2.307.076 identità e 4.007 Excel dati; la copertura integrale degli otto portali rimane incompleta.

## Risorse acquisite

| Codice FAOSTAT | Risorsa | Osservazioni | Identità | Anni presenti |
|---|---|---:|---:|---|
| [CP](https://bulks-faostat.fao.org/production/ConsumerPriceIndices_E_All_Data_(Normalized).zip) | Indici dei prezzi al consumo | 266.292 | 10.260 | 2000–2026 |
| [CS](https://bulks-faostat.fao.org/production/Investment_CapitalStock_E_All_Data_(Normalized).zip) | Stock di capitale | 144.944 | 5.082 | 1995–2023 |
| [FDI](https://bulks-faostat.fao.org/production/Investment_ForeignDirectInvestment_E_All_Data_(Normalized).zip) | Investimenti diretti esteri | 40.442 | 1.736 | 1990–2023 |
| [IC](https://bulks-faostat.fao.org/production/Investment_CreditAgriculture_E_All_Data_(Normalized).zip) | Credito agricolo | 62.899 | 2.776 | 1991–2024 |
| [IG](https://bulks-faostat.fao.org/production/Investment_GovernmentExpenditure_E_All_Data_(Normalized).zip) | Spesa pubblica | 156.256 | 11.616 | 2001–2024 |
| [MK](https://bulks-faostat.fao.org/production/Macro-Statistics_Key_Indicators_E_All_Data_(Normalized).zip) | Indicatori macroeconomici | 708.632 | 16.642 | 1970–2024 |
| [PD](https://bulks-faostat.fao.org/production/Deflators_E_All_Data_(Normalized).zip) | Deflatori | 92.776 | 1.816 | 1970–2024 |
| [PE](https://bulks-faostat.fao.org/production/Exchange_rate_E_All_Data_(Normalized).zip) | Tassi di cambio | 151.212 | 4.664 | 1970–2026 |

Sono incluse tutte le righe e le annualità presenti negli otto CSV acquisiti, senza soglie temporali. Le osservazioni numeriche sono 1.623.342; le altre 111 righe restano presenti con il valore originale mancante o non numerico, senza trasformarlo in zero.

Valori originali in testo, valori numerici, unità, codici, dimensioni, flag, note e provenienza restano distinti. Non sono applicate conversioni di unità o valuta, ribasamenti degli indici, armonizzazioni di prezzi correnti e costanti o stime proprie.

## Periodi e identità

CP e PE contengono campi mensili originali, che restano disponibili negli Excel insieme a Year e Year Code. Il campo comune Periodo originale conserva Year; Months, Months Code e gli eventuali codici di valuta non sono eliminati, convertiti in date fittizie o aggregati.

La chiave di serie mantiene la convenzione precedente: SHA256 di FAOSTAT|codice dataset|JSON canonico delle dimensioni codificate originali e dell'unità, escluso Year Code. Nei dataset mensili Months Code resta quindi una dimensione dell'identità; per una sequenza mensile completa occorre utilizzare congiuntamente anno e campi del mese, non il solo campo comune Year.

Gli anni estremi indicati nella tabella non certificano la presenza di ogni mese o di ogni anno per ogni singola serie. Eventuali stime, proiezioni e periodi futuri della fonte mantengono flag e provenienza e non sono presentati come rilevazioni già osservate.

## Organizzazione e dimensioni dei file

- **Indice del lotto 16**: elenco degli Excel e degli ZIP, conteggi, annualità, byte, SHA256, fonti e prima parte del registro cumulativo.
- **Archivi dati**: 238 Excel per paesi e territori originali e 44 Excel per aggregati statistici, distribuiti in 7 ZIP. Gli aggregati restano separati e non sono qualificati come regioni amministrative.
- **Dizionari originali**: tutti i CSV ausiliari degli otto archivi fonte, conservati senza tradurre o ricodificare codici e descrizioni.
- **Stato complessivo 1–16**: riepilogo per lotto e per portale, catalogo FAOSTAT e riferimenti a tutte le parti del registro.
- **Manifest e verifica**: risultati PASS, SHA256 degli allegati e dei singoli Excel, catalogo acquisito, recupero precedente e documentazione FO ereditata.

Gli Excel mantengono la struttura precedente: colonna A di margine, titolo alla riga 2, intestazioni alla riga 3 e dati dalla riga 4. I fogli DATI hanno le 16 colonne comuni più tutti i campi originali non già rappresentati; gli stili risultano identici a quelli del lotto 15 e sono verificati margini, intestazioni e blocchi dei riquadri in tutti i fogli.

Ogni XLSX e ZIP consegnato è strettamente inferiore a **29.000.000 byte**. Il più grande Excel del lotto misura 8.953.401 byte e lo ZIP dati più grande 21.829.722 byte; anche il pacchetto di verifica rispetta il limite.

## Recupero e continuità

Prima di acquisire nuovi dati sono state ricostruite e lette tutte le 23 parti del registro del lotto 15: 2.252.484 identità e 24.457.035 osservazioni. Gli allegati pubblicati sono stati recuperati e confrontati con hash, dimensioni e CRC, senza assumere attendibile il vecchio database di lavoro; sono stati verificati i 248 Excel dati del lotto 15, mentre per i precedenti 3.477 Excel resta esplicitamente ereditata la verifica storica documentata.

Il registro cumulativo è ora in **24 parti**. Occorre conservare insieme:

- **Parte 1**: foglio REGISTRO_SERIE dell'indice del lotto 16, copiato invariato dall'indice 15.
- **Parti 2–21**: file storici immutati nei sette ZIP di continuità del lotto 14.
- **Parte 22**: file separato del lotto 14, immutato.
- **Parte 23**: file separato del lotto 15, immutato.
- **Nuove appendici del lotto 16**: parte 24 con 54.592 identità.

Le nuove identità non intersecano le 2.252.484 precedenti e non vi sono ripetizioni serie-periodo. Il confronto esatto delle dimensioni codificate e delle unità fra dataset non trova candidati né con lo storico né tra gli otto nuovi dataset; non si dichiara un'armonizzazione semantica di sistemi di codici differenti.

## Scostamenti del catalogo e risorse residue

I conteggi riportati sono quelli dei record CSV effettivamente letti e confrontati con i file originali. Sono conservate anche le righe che eccedono FileRows del catalogo, senza tagli per far coincidere il totale; non sono inventate righe quando il CSV ne contiene meno.

- **MK**: 456.877 righe dichiarate nel catalogo, 708.632 record nel CSV acquisito; differenza +251.755 ([archivio FAOSTAT MK](https://bulks-faostat.fao.org/production/Macro-Statistics_Key_Indicators_E_All_Data_(Normalized).zip)).
- **PD**: 93.659 righe dichiarate nel catalogo, 92.776 record nel CSV acquisito; differenza -883 ([archivio FAOSTAT PD](https://bulks-faostat.fao.org/production/Deflators_E_All_Data_(Normalized).zip)).

Le altre sei risorse coincidono con i conteggi del catalogo. Il catalogo FAOSTAT contiene 69 risorse, delle quali 52 ora acquisite e 17 residue; gli altri sette portali mantengono la copertura dei lotti precedenti e non sono stati riverificati nel lotto 16.

FO, Forestry Production and Trade, resta **non incluso e non conteggiato**. L'ispezione del lotto 15 ha trovato 794 candidati con dimensioni codificate e unità identiche a serie FOP già consegnate: non sono duplicati accertati e, prima di includere FO, vanno confrontati contenuti, periodi, valori e provenienza; l'evidenza viene ereditata nel presente audit, non presentata come nuova ispezione.

## Controlli e fonti

Il controllo diretto verifica ogni record degli otto CSV contro la struttura acquisita e rilegge ogni cella dei fogli DATI nei 282 Excel. Testo originale e dizionari sono confrontati integralmente, i valori numerici sono verificati con tolleranza relativa e assoluta di 1e-14 mantenendo il testo esatto a fianco, e le appendici del registro sono confrontate riga per riga.

Ogni Excel contenuto negli ZIP è verificato per dimensione e SHA256 contro il file riletto, oltre ai controlli CRC e al limite in byte. I risultati completi sono nel pacchetto Manifest e verifica, con esito PASS.

Il riferimento è il [catalogo bulk FAOSTAT](https://bulks-faostat.fao.org/production/datasets_E.json), acquisito il 25 ottobre 2026. Gli archivi ufficiali inclusi sono:

- **CP**: [Prices: Consumer Price Indices](https://bulks-faostat.fao.org/production/ConsumerPriceIndices_E_All_Data_(Normalized).zip).
- **CS**: [Macro-Economic Indicators: Capital Stock](https://bulks-faostat.fao.org/production/Investment_CapitalStock_E_All_Data_(Normalized).zip).
- **FDI**: [Investment: Foreign Direct Investment (FDI)](https://bulks-faostat.fao.org/production/Investment_ForeignDirectInvestment_E_All_Data_(Normalized).zip).
- **IC**: [Investment: Credit to Agriculture](https://bulks-faostat.fao.org/production/Investment_CreditAgriculture_E_All_Data_(Normalized).zip).
- **IG**: [Investment: Government Expenditure](https://bulks-faostat.fao.org/production/Investment_GovernmentExpenditure_E_All_Data_(Normalized).zip).
- **MK**: [Macro-Economic Indicators: Macro Indicators](https://bulks-faostat.fao.org/production/Macro-Statistics_Key_Indicators_E_All_Data_(Normalized).zip).
- **PD**: [Prices: Deflators](https://bulks-faostat.fao.org/production/Deflators_E_All_Data_(Normalized).zip).
- **PE**: [Prices: Exchange rates](https://bulks-faostat.fao.org/production/Exchange_rate_E_All_Data_(Normalized).zip).
