# Open data internazionali: guida al lotto 17

Il lotto 17 aggiunge **2.504.569 osservazioni**, 119.201 identità di serie e 234 Excel dati. Il cumulativo dei lotti 1–17 raggiunge 28.585.057 osservazioni, 2.426.277 identità e 4.241 Excel dati; l'acquisizione integrale degli otto portali resta incompleta.

## Risorse acquisite

| Codice FAOSTAT | Risorsa | Osservazioni | Identità | Periodi originali estremi |
|---|---|---:|---:|---|
| [CBH](https://bulks-faostat.fao.org/production/CommodityBalances_(non-food)_(-2013_old_methodology)_E_All_Data_(Normalized).zip) | Bilanci storici delle commodity non alimentari, vecchia metodologia fino al 2013 | 1.184.986 | 24.500 | 1961–2013 |
| [PP](https://bulks-faostat.fao.org/production/Prices_E_All_Data_(Normalized).zip) | Prezzi alla produzione | 1.319.583 | 94.701 | 1991–2025 |

Il lotto comprende due delle 17 risorse residue iniziali, acquisite senza soglie temporali e con tutti i record effettivi dei CSV fonte. Tutte le 2.504.569 osservazioni hanno un valore numerico; il testo originale è comunque conservato, senza sostituire i mancanti con zero.

CBH mantiene la vecchia metodologia e la qualificazione di archivio storico, senza confonderla con metodologie successive. PP mantiene i campi originali, i periodi e le dimensioni della fonte; i prezzi non sono convertiti fra valute o unità e non sono ribasati gli indici.

## Formato e periodi

Ogni foglio DATI mantiene le 16 colonne comuni precedenti più tutti i campi originali non già rappresentati. Sono conservati valori numerici e testo numerico originale, unità, codici, flag, note, aggiornamento e URL della fonte, con intestazioni alla riga 3 e dati dalla riga 4.

La chiave mantiene la convenzione precedente: SHA256 di FAOSTAT|dataset|JSON canonico delle dimensioni codificate e dell'unità, escludendo Year Code. Il campo comune Periodo originale conserva Year esattamente come pubblicato; eventuali mesi, periodi pluriennali e dimensioni di indagine rimangono nei campi originali, senza date fittizie, medie o aggregazioni.

PP contiene Months e Months Code: i campi mensili sono conservati e Months Code resta una dimensione dell'identità, come nei lotti precedenti. Per una sequenza mensile occorre usare congiuntamente Year e i campi del mese, non il solo campo comune Periodo originale.

Gli estremi temporali non certificano una sequenza completa per ogni serie. Stime, proiezioni, periodi futuri e dati storici conservano i flag della fonte e non sono automaticamente qualificati come osservazioni già rilevate.

## Archivi e limite dimensionale

- **Dati**: 200 Excel per paesi e territori originali e 34 per aggregati statistici, distribuiti in 9 ZIP.
- **Indice**: elenco di file, archivi, conteggi, periodi, byte, SHA256, fonti e prima parte del registro.
- **Registro**: appendici nuove dal numero 25, senza modificare le identità dei lotti precedenti.
- **Dizionari originali**: tutti i CSV ausiliari degli archivi fonte, senza tradurre o ricodificare i valori.
- **Stato complessivo**: riepilogo dei lotti 1–17, otto portali, catalogo FAOSTAT e continuità del registro.
- **Audit**: recupero verificato, confronto record e celle, controlli SHA256 e CRC, catalogo e risorse residue.

Gli aggregati statistici restano separati dai paesi e territori e non sono qualificati come regioni amministrative. Non sono inferite appartenenze amministrative o ricodifiche geografiche delle osservazioni originali.

Ogni XLSX e ZIP consegnato è strettamente inferiore a **29.000.000 byte**. Il maggiore Excel misura 9.187.316 byte e lo ZIP dati maggiore 20.811.057 byte; il pacchetto di audit è verificato separatamente rispetto allo stesso limite.

## Recupero e continuità cumulativa

Prima di acquisire nuovi dati sono stati scaricati nuovamente l'audit, l'indice e la parte 24 pubblicati del lotto 16. Le altre consegne disponibili sono state accettate solo dopo verifica di dimensioni e SHA256 contro il manifest appena recuperato, senza presumere accessibili o validi i vecchi file locali.

Sono state lette e ricostruite tutte le **24 parti** del registro precedente: 2.307.076 identità, 26.080.488 osservazioni e 22.238.228 valori numerici. Sono stati verificati hash, dimensioni e CRC dei 282 Excel dati del lotto 16; per i precedenti 3.725 Excel resta esplicitamente ereditata la verifica storica pubblicata, non dichiarata come nuova rilettura integrale.

Il registro cumulativo contiene ora **26 parti**, da conservare insieme:

- **Parte 1**: REGISTRO_SERIE dell'indice del lotto 17, copiata invariata dall'indice 16.
- **Parti 2–21**: file immutati nei sette ZIP di continuità del lotto 14.
- **Parte 22**: file separato del lotto 14.
- **Parte 23**: file separato del lotto 15.
- **Parte 24**: file separato del lotto 16.
- **Nuove appendici del lotto 17**: parte 25 con 100.000 identità, parte 26 con 19.201 identità.

Le nuove identità non intersecano le 2.307.076 precedenti e non vi sono ripetizioni serie-periodo. Il confronto esatto di dimensioni codificate e unità non trova candidati con lo storico o fra i due dataset nuovi; questo controllo non equivale a un'armonizzazione semantica fra sistemi di codici differenti.

È inoltre verificata l'assenza di sovrapposizione temporale fra PP e l'archivio storico PA già consegnato: il primo periodo di PP è successivo all'ultimo di PA. Le due risorse mantengono i rispettivi codici e la provenienza, senza fondere le serie o attribuire una continuità metodologica non verificata.

## Catalogo e risorse residue

I conteggi consegnati provengono dai record effettivi dei CSV. Nessuna riga viene tagliata per adattarsi al catalogo e nessun record viene inventato per compensare eventuali differenze.

Entrambe le risorse coincidono con i conteggi dichiarati dal catalogo.

FAOSTAT comprende 69 risorse nel catalogo acquisito: **54 acquisite e 15 residue**. Gli altri sette portali mantengono la copertura precedente e non sono stati riverificati in questo lotto.

FDIQ è stato scaricato e ispezionato, ma resta non acquisito e non conteggiato. Il CSV contiene Survey Code, Survey, Geographic Level e dimensioni delle indagini, senza Area, Area Code, Year o Year Code: occorre una mappatura dedicata che non inventi campi geografici o annuali, e l'evidenza di schema è inclusa nell'audit.

FO resta escluso e non conteggiato: l'ispezione del lotto 15 trovò 794 candidati con dimensioni e unità uguali a serie FOP già consegnate. Non sono duplicati accertati; occorre ancora verificare contenuti, periodi, valori e provenienza prima dell'inclusione, e l'audit riporta questa evidenza come ereditata.

Le risorse ancora da acquisire sono:

- **EA**: [Investment: Development Flows to Agriculture](https://bulks-faostat.fao.org/production/Development_Assistance_to_Agriculture_E_All_Data_(Normalized).zip).
- **FBS**: [Food Balances: Food Balances (2010-)](https://bulks-faostat.fao.org/production/FoodBalanceSheets_E_All_Data_(Normalized).zip).
- **FBSH**: [Food Balances: Food Balances (-2013, old methodology and population)](https://bulks-faostat.fao.org/production/FoodBalanceSheetsHistoric_E_All_Data_(Normalized).zip).
- **FDIQ**: [Food and Diet: Intake (based on individual quantitative dietary surveys)](https://bulks-faostat.fao.org/production/Individual_Quantitative_Dietary_Data_Food_and_Diet_E_All_Data_(Normalized).zip).
- **FO**: [Forestry: Forestry Production and Trade](https://bulks-faostat.fao.org/production/Forestry_E_All_Data_(Normalized).zip).
- **FT**: [Discontinued archives and data series: Forestry Trade Flows](https://bulks-faostat.fao.org/production/Forestry_Trade_Flows_E_All_Data_(Normalized).zip).
- **GLE**: [Climate Change: Agrifood systems emissions: Emissions from Livestock](https://bulks-faostat.fao.org/production/Emissions_livestock_E_All_Data_(Normalized).zip).
- **GT**: [Climate Change: Agrifood systems emissions: Emissions totals](https://bulks-faostat.fao.org/production/Emissions_Totals_E_All_Data_(Normalized).zip).
- **QCL**: [Production: Crops and livestock products](https://bulks-faostat.fao.org/production/Production_Crops_Livestock_E_All_Data_(Normalized).zip).
- **QV**: [Production: Value of Agricultural Production](https://bulks-faostat.fao.org/production/Value_of_Production_E_All_Data_(Normalized).zip).
- **RFM**: [Land, Inputs and Sustainability: Detailed trade matrix (fertilizers)](https://bulks-faostat.fao.org/production/Fertilizers_DetailedTradeMatrix_E_All_Data_(Normalized).zip).
- **SCL**: [Food Balances: Supply Utilization Accounts (2010-)](https://bulks-faostat.fao.org/production/SUA_Crops_Livestock_E_All_Data_(Normalized).zip).
- **TCL**: [Trade: Crops and livestock products](https://bulks-faostat.fao.org/production/Trade_CropsLivestock_E_All_Data_(Normalized).zip).
- **TI**: [Trade: Trade Indices](https://bulks-faostat.fao.org/production/Trade_Indices_E_All_Data_(Normalized).zip).
- **TM**: [Trade: Detailed trade matrix](https://bulks-faostat.fao.org/production/Trade_DetailedTradeMatrix_E_All_Data_(Normalized).zip).

## Verifica e provenienza

Il controllo confronta ogni record dei due CSV con i dati acquisiti, quindi rilegge ogni cella DATI di tutti i 234 Excel. Testo originale, dizionari e appendici del registro sono confrontati integralmente; per i numeri si usa tolleranza relativa e assoluta di 1e-14, conservando il testo numerico esatto a fianco.

Tutti gli Excel negli ZIP sono verificati per dimensioni e SHA256 contro i file riletti, oltre al controllo CRC. Stili, margini, intestazioni e blocchi dei riquadri sono verificati sul formato del lotto 16; l'esito completo è PASS nel pacchetto di audit.

Il [catalogo ufficiale bulk FAOSTAT](https://bulks-faostat.fao.org/production/datasets_E.json) è stato acquisito il 25 ottobre 2026. Le fonti ufficiali del lotto sono:

- **CBH**: [Food Balances: Commodity Balances (non-food) (-2013, old methodology)](https://bulks-faostat.fao.org/production/CommodityBalances_(non-food)_(-2013_old_methodology)_E_All_Data_(Normalized).zip).
- **PP**: [Prices: Producer Prices](https://bulks-faostat.fao.org/production/Prices_E_All_Data_(Normalized).zip).
