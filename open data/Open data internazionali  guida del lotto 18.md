# Open data internazionali: guida al lotto 18

Il lotto 18 aggiunge **6.221.982 osservazioni**, 411.104 identità di serie e 300 Excel dati. Il cumulativo dei lotti 1–18 raggiunge 34.807.039 osservazioni, 2.837.381 identità e 4.541 Excel dati; l'acquisizione integrale degli otto portali resta incompleta.

## Risorse acquisite

| Codice FAOSTAT | Risorsa | Osservazioni | Identità | Periodi originali estremi |
|---|---|---:|---:|---|
| [FT](https://bulks-faostat.fao.org/production/Forestry_Trade_Flows_E_All_Data_(Normalized).zip) | Flussi commerciali forestali, archivio storico | 2.829.802 | 333.646 | 1997–2018 |
| [QV](https://bulks-faostat.fao.org/production/Value_of_Production_E_All_Data_(Normalized).zip) | Valore della produzione agricola | 3.392.180 | 77.458 | 1961–2024 |

Il lotto comprende due delle 15 risorse residue iniziali, acquisite senza soglie temporali e con tutti i record effettivi dei CSV fonte. Tutte le 6.221.982 osservazioni hanno un valore numerico; il testo originale è comunque conservato.

FT mantiene la qualificazione di archivio storico e tutti i flussi bilaterali originali, senza aggregare i partner o trasformare le importazioni e le esportazioni in saldi. QV conserva le distinzioni originali di elemento e unità, prezzi correnti o costanti e basi di riferimento, senza conversioni di valuta, ribasamenti o stime proprie.

## Formato, geografia e dimensioni bilaterali

I fogli DATI mantengono le 16 colonne comuni precedenti più tutti i campi originali non già rappresentati. Sono conservati valori numerici e testo numerico originale, unità, codici, flag, note, aggiornamento e URL, con intestazioni alla riga 3 e dati dalla riga 4.

FT è ripartito per paese dichiarante: le prime due colonne comuni riportano esattamente Reporter Country Code e Reporter Countries. Tutti i campi originali restano anche nelle colonne aggiuntive, inclusi i codici M49 del dichiarante, Partner Country Code, Partner Country Code (M49), Partner Countries e Note.

I codici e i nomi di partner e dichiarante non sono fusi né intercambiati. I partner possono essere paesi, territori o aggregati statistici, senza essere qualificati come regioni amministrative; l'organizzazione degli archivi dipende dal dichiarante e non elimina alcun partner.

QV usa Area Code e Area nelle prime due colonne comuni, secondo la convenzione precedente. I codici geografici e i nomi storici originali restano conservati, senza attribuzioni amministrative inferite.

La chiave resta SHA256 di FAOSTAT|dataset|JSON canonico delle dimensioni codificate e dell'unità, escludendo Year Code. Per FT comprende quindi sia dichiarante sia partner; Periodo originale conserva Year esattamente come pubblicato, senza armonizzazioni, medie o aggregazioni.

Gli estremi temporali non certificano una sequenza completa per ogni singola serie. Stime, proiezioni, periodi futuri e dati storici mantengono i flag della fonte e non sono automaticamente qualificati come osservazioni già rilevate.

## Consegna e dimensioni

- **Dati**: 266 Excel per paesi e territori originali e 34 per aggregati statistici, distribuiti in 25 ZIP.
- **Indice**: elenco di file e archivi, conteggi, periodi, byte, SHA256, fonti e prima parte del registro.
- **Registro**: appendici nuove dal numero 27, senza modificare le identità precedenti.
- **Dizionari originali**: tutti i CSV ausiliari dei due ZIP fonte, conservati senza ricodificare o tradurre i valori.
- **Stato complessivo**: riepilogo dei lotti 1–18, otto portali, catalogo FAOSTAT e continuità del registro.
- **Audit**: recupero verificato, confronto di ogni record e cella, SHA256 e CRC, catalogo e risorse residue.

Gli aggregati statistici del dichiarante o dell'area restano separati dai paesi e territori e non sono qualificati come regioni amministrative. Il layout e gli stili restano quelli del lotto 17, con verifica su tutti i fogli.

Ogni XLSX e ZIP consegnato è strettamente inferiore a **29.000.000 byte**. Il maggiore Excel misura 9.554.231 byte e lo ZIP dati maggiore 21.868.782 byte; il pacchetto di audit è controllato separatamente rispetto allo stesso limite.

## Recupero e continuità

Prima di acquisire nuovi dati sono stati scaricati nuovamente l'audit, l'indice e le parti 25–26 pubblicati del lotto 17. Le altre consegne locali disponibili sono state accettate solo dopo verifica di dimensioni e SHA256 contro il manifest appena recuperato, senza presumere validi o accessibili i vecchi file di lavoro.

Sono state lette e ricostruite tutte le **26 parti** del registro precedente: 2.426.277 identità, 28.585.057 osservazioni e 24.742.797 valori numerici. Sono stati verificati hash, dimensioni e CRC dei 234 Excel dati del lotto 17; per i precedenti 4.007 Excel resta esplicitamente ereditata la verifica storica pubblicata, non dichiarata come nuova rilettura integrale.

Il registro cumulativo comprende ora **31 parti**, da conservare insieme:

- **Parte 1**: REGISTRO_SERIE dell'indice del lotto 18, copiata invariata dall'indice 17.
- **Parti 2–21**: file immutati nei sette ZIP di continuità del lotto 14.
- **Parte 22**: file separato del lotto 14.
- **Parte 23**: file separato del lotto 15.
- **Parte 24**: file separato del lotto 16.
- **Parti 25–26**: file separati del lotto 17.
- **Nuove appendici del lotto 18**: parte 27 con 100.000 identità, parte 28 con 100.000 identità, parte 29 con 100.000 identità, parte 30 con 100.000 identità, parte 31 con 11.104 identità.

Le nuove identità non intersecano le 2.426.277 precedenti e non vi sono ripetizioni serie-periodo. Il confronto esatto di dimensioni codificate e unità non trova candidati con lo storico o fra i due dataset nuovi; il controllo non costituisce un'armonizzazione semantica fra schemi di campi o codici differenti.

## Catalogo e risorse residue

I conteggi consegnati sono quelli dei record effettivi dei CSV. Nessuna riga viene tagliata per adattarsi al catalogo e nessun record viene inventato per compensare eventuali differenze.

Entrambe le risorse coincidono con i conteggi dichiarati dal catalogo.

FAOSTAT comprende 69 risorse nel catalogo acquisito: **56 acquisite e 13 residue**. Gli altri sette portali mantengono la copertura precedente e non sono stati riverificati in questo lotto.

FDIQ resta non acquisito e non conteggiato: lo schema ispezionato nel lotto 17 usa Survey Code, Survey, Geographic Level e altre dimensioni, senza Area, Area Code, Year o Year Code. Richiede una mappatura dedicata che non inventi campi geografici o annuali; l'evidenza di schema è ereditata nell'audit e non presentata come nuova ispezione.

FO resta escluso e non conteggiato: l'ispezione del lotto 15 trovò 794 candidati con dimensioni e unità uguali a serie FOP già consegnate. Non sono duplicati accertati e occorre verificarne contenuti, periodi, valori e provenienza prima dell'inclusione; FT è invece il distinto archivio dei flussi commerciali bilaterali.

Le risorse ancora da acquisire sono:

- **EA**: [Investment: Development Flows to Agriculture](https://bulks-faostat.fao.org/production/Development_Assistance_to_Agriculture_E_All_Data_(Normalized).zip).
- **FBS**: [Food Balances: Food Balances (2010-)](https://bulks-faostat.fao.org/production/FoodBalanceSheets_E_All_Data_(Normalized).zip).
- **FBSH**: [Food Balances: Food Balances (-2013, old methodology and population)](https://bulks-faostat.fao.org/production/FoodBalanceSheetsHistoric_E_All_Data_(Normalized).zip).
- **FDIQ**: [Food and Diet: Intake (based on individual quantitative dietary surveys)](https://bulks-faostat.fao.org/production/Individual_Quantitative_Dietary_Data_Food_and_Diet_E_All_Data_(Normalized).zip).
- **FO**: [Forestry: Forestry Production and Trade](https://bulks-faostat.fao.org/production/Forestry_E_All_Data_(Normalized).zip).
- **GLE**: [Climate Change: Agrifood systems emissions: Emissions from Livestock](https://bulks-faostat.fao.org/production/Emissions_livestock_E_All_Data_(Normalized).zip).
- **GT**: [Climate Change: Agrifood systems emissions: Emissions totals](https://bulks-faostat.fao.org/production/Emissions_Totals_E_All_Data_(Normalized).zip).
- **QCL**: [Production: Crops and livestock products](https://bulks-faostat.fao.org/production/Production_Crops_Livestock_E_All_Data_(Normalized).zip).
- **RFM**: [Land, Inputs and Sustainability: Detailed trade matrix (fertilizers)](https://bulks-faostat.fao.org/production/Fertilizers_DetailedTradeMatrix_E_All_Data_(Normalized).zip).
- **SCL**: [Food Balances: Supply Utilization Accounts (2010-)](https://bulks-faostat.fao.org/production/SUA_Crops_Livestock_E_All_Data_(Normalized).zip).
- **TCL**: [Trade: Crops and livestock products](https://bulks-faostat.fao.org/production/Trade_CropsLivestock_E_All_Data_(Normalized).zip).
- **TI**: [Trade: Trade Indices](https://bulks-faostat.fao.org/production/Trade_Indices_E_All_Data_(Normalized).zip).
- **TM**: [Trade: Detailed trade matrix](https://bulks-faostat.fao.org/production/Trade_DetailedTradeMatrix_E_All_Data_(Normalized).zip).

## Verifica e provenienza

Ogni record dei due CSV è confrontato con i dati acquisiti e ogni cella DATI dei 300 Excel è riletta e confrontata. Per FT sono verificati esplicitamente il riporto del dichiarante nelle colonne comuni e la conservazione di tutti i campi partner, oltre alle dimensioni usate nell'identità.

Testo originale, dizionari e appendici del registro sono confrontati integralmente. I numeri sono verificati con tolleranza relativa e assoluta di 1e-14, mantenendo il testo numerico originale esatto a fianco.

Ogni membro Excel negli ZIP è controllato per dimensione e SHA256 contro il file riletto, oltre al controllo CRC. Stili, margini, intestazioni e blocchi dei riquadri sono verificati sul formato del lotto 17; l'esito completo è PASS.

Il [catalogo ufficiale bulk FAOSTAT](https://bulks-faostat.fao.org/production/datasets_E.json) è stato acquisito il 25 ottobre 2026. Gli archivi fonte ufficiali del lotto sono:

- **FT**: [Discontinued archives and data series: Forestry Trade Flows](https://bulks-faostat.fao.org/production/Forestry_Trade_Flows_E_All_Data_(Normalized).zip).
- **QV**: [Production: Value of Agricultural Production](https://bulks-faostat.fao.org/production/Value_of_Production_E_All_Data_(Normalized).zip).
