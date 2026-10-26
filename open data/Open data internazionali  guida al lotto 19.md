# Open data internazionali: guida al lotto 19

Il lotto 19 aggiunge **5.565.289 osservazioni**, 669.432 identità di serie e 290 Excel dati. Il cumulativo dei lotti 1–19 raggiunge 40.372.328 osservazioni, 3.506.813 identità e 4.831 Excel dati; la raccolta integrale degli otto portali resta incompleta.

## Risorsa acquisita

| Codice FAOSTAT | Risorsa originale | Osservazioni | Identità | Periodi originali estremi |
|---|---|---:|---:|---|
| [RFM](https://bulks-faostat.fao.org/production/Fertilizers_DetailedTradeMatrix_E_All_Data_(Normalized).zip) | Land, Inputs and Sustainability: Detailed trade matrix (fertilizers) | 5.565.289 | 669.432 | 1990–2024 |

Il lotto acquisisce integralmente una delle 13 risorse residue iniziali: la matrice commerciale dettagliata dei fertilizzanti. Sono incluse tutte le righe e tutte le annualità del CSV originale, senza soglie temporali. Il conteggio effettivo coincide con le 5.565.289 righe dichiarate dal catalogo.

Le righe numeriche sono 5.547.426; le altre 17.863 mantengono il testo originale e non sono sostituite con zero o stime. Prodotti, elementi e flussi bilaterali restano distinti secondo codici, nomi e unità della fonte, senza aggregare partner, trasformare importazioni ed esportazioni in saldi, convertire scale o introdurre stime proprie.

## Formato, dimensioni e geografia

I fogli DATI mantengono le 16 colonne comuni dei lotti precedenti e tutte le colonne originali non già rappresentate. Valori numerici, testo numerico originale, unità, codici geografici, Item Code, Item Code (CPC), Element Code, Year Code, flag e tutti gli altri campi presenti nella fonte restano conservati senza traduzioni o ricodifiche.

Le prime due colonne comuni riportano Reporter Country Code e Reporter Countries esattamente come nel CSV. La ripartizione dei file dipende dal dichiarante e non elimina alcun partner; tutti i campi originali del dichiarante e del partner restano nelle colonne aggiuntive, compresi entrambi i codici M49.

Dichiarante e partner non sono fusi né intercambiati. Codici e denominazioni storiche restano riconoscibili; gli aggregati statistici sono separati dai paesi e territori, senza qualificarli come regioni amministrative o inferire appartenenze amministrative.

La ripartizione geografica degli archivi riguarda il dichiarante: in questa fonte tutti i 217 dichiaranti sono classificati come paesi o territori e non vi sono Excel intestati ad aggregati dichiaranti. L'eventuale aggregato presente come partner resta un partner originale del flusso, riconoscibile per codice e nome, e non diventa una regione amministrativa né cambia l'archivio del dichiarante.

La chiave è SHA256 di FAOSTAT|dataset|JSON canonico delle dimensioni codificate e dell'unità, escludendo Year Code. Include quindi sia dichiarante sia partner e i rispettivi codici M49; Periodo originale conserva Year esattamente, mentre gli estremi temporali non garantiscono una sequenza completa per ciascuna serie.

Stime, proiezioni e periodi futuri eventualmente presenti mantengono i flag originali e non sono presentati automaticamente come dati osservati. Celle mancanti e valori non numerici non diventano zeri, mentre ogni eventuale zero effettivamente pubblicato resta conservato.

## Consegna e dimensioni

- **Dati**: 290 Excel per paesi e territori e 0 per aggregati statistici, distribuiti in 26 ZIP.
- **Indice**: elenco degli Excel e degli ZIP con conteggi, periodi, byte, SHA256, provenienza e prima parte del registro cumulativo.
- **Registro**: nuove appendici dal numero 32, mantenendo immutate le 31 parti precedenti.
- **Dizionari**: tutti i CSV ausiliari dello ZIP fonte, conservati e confrontati integralmente.
- **Stato complessivo**: riepilogo dei lotti 1–19, otto portali, catalogo FAOSTAT e continuità del registro.
- **Audit**: recupero verificato, confronti integrali, cataloghi, trasferimenti HTTP, SHA256 e CRC, risorse residue ed evidenze storiche di rinvio.

Gli stili e il layout restano identici al lotto 18: margine A, titolo alla riga 2, intestazioni alla riga 3, dati dalla riga 4, riquadri bloccati in D4 e griglia nascosta. Tutti i fogli e tutti gli stili sono stati controllati sul formato precedente.

Ogni Excel e ZIP consegnato è strettamente inferiore a **29.000.000 byte**. L'Excel maggiore misura 9.715.211 byte e lo ZIP dati maggiore 22.908.410 byte; anche l'audit è verificato separatamente rispetto allo stesso limite.

## Recupero preventivo e continuità

Prima di scaricare nuovi dati sono stati recuperati nuovamente l'audit, l'indice e le parti 27–31 pubblicati del lotto 18. Gli altri allegati disponibili sono stati accettati soltanto dopo confronto di byte e SHA256 con il manifest appena recuperato, senza presumere accessibili o validi i vecchi file locali.

Sono stati verificati i **35 allegati** del lotto 18 e ricostruite tutte le **31 parti** del registro precedente: 2.837.381 identità, 34.807.039 osservazioni e 30.964.779 valori numerici. I 300 Excel dati contenuti nei 25 ZIP del lotto 18 sono stati verificati individualmente per dimensioni e SHA256, oltre al CRC degli archivi.

La verifica dei precedenti 4.241 Excel dei lotti 1–17 resta esplicitamente ereditata dall'audit pubblicato, non dichiarata come nuova rilettura integrale. Sono stati eliminati soltanto database di lavoro ricostruibili e copie scompattate degli Excel, dopo averne verificato la corrispondenza byte per byte con gli ZIP conservati; nessun allegato pubblicato o archivio fonte è stato eliminato.

Il registro comprende ora **38 parti**, da conservare insieme:

- **Parte 1**: foglio REGISTRO_SERIE dell'indice del lotto 19, copiato invariato dall'indice 18.
- **Parti 2–21**: file originali nei sette ZIP di continuità del lotto 14.
- **Parte 22**: file separato del lotto 14.
- **Parte 23**: file separato del lotto 15.
- **Parte 24**: file separato del lotto 16.
- **Parti 25–26**: file separati del lotto 17.
- **Parti 27–31**: file separati del lotto 18.
- **Nuove appendici del lotto 19**: parte 32 con 100.000 identità, parte 33 con 100.000 identità, parte 34 con 100.000 identità, parte 35 con 100.000 identità, parte 36 con 100.000 identità, parte 37 con 100.000 identità, parte 38 con 69.432 identità.

Le nuove identità non intersecano le precedenti e non vi sono ripetizioni serie-periodo. Il confronto esatto di dimensioni codificate e unità non rileva candidati fra RFM e lo storico; non si dichiara un'armonizzazione semantica fra schemi o sistemi di codifica differenti.

## Catalogo e risorse residue

FAOSTAT comprende 69 risorse nel [catalogo ufficiale bulk](https://bulks-faostat.fao.org/production/datasets_E.json) acquisito il 25 ottobre 2026: **57 acquisite e 12 residue**. Gli altri sette portali mantengono la copertura precedente e non sono stati riverificati in questo lotto.

QCL è stato scaricato e acquisito soltanto nello staging di ispezione, ma non è consegnato né conteggiato. Le 4.209.110 righe effettive contengono 78.974 identità per dataset e 4.154 coppie candidate dimensionali con serie precedenti: 585 con CB, 2.230 con EI e 1.339 con EMN.

I campioni includono produzione e consistenze con intervalli temporali differenti; non è stata dimostrata né l'identità né la diversità dei valori per tutti i periodi. Nessuna serie o riga QCL è eliminata come duplicato accertato: il file fonte resta conservato e l'audit riporta chiavi, dimensioni, coperture e campioni per la successiva riconciliazione.

FO resta escluso e non conteggiato: nel lotto 15 erano stati rilevati 794 candidati dimensionali con FOP, non duplicati accertati. Occorre ancora confrontare contenuti, periodi, valori e provenienza prima dell'inclusione, e l'evidenza nell'audit è dichiarata come ereditata.

FDIQ resta escluso e non conteggiato: lo schema ispezionato nel lotto 17 usa dimensioni per indagini e non contiene Area, Area Code, Year o Year Code. Richiede una mappatura dedicata fedele alla fonte, senza inventare geografie o annualità; anche questa evidenza è ereditata e non presentata come nuova ispezione.

Le risorse residue sono:

- **EA**: [Investment: Development Flows to Agriculture](https://bulks-faostat.fao.org/production/Development_Assistance_to_Agriculture_E_All_Data_(Normalized).zip).
- **FBS**: [Food Balances: Food Balances (2010-)](https://bulks-faostat.fao.org/production/FoodBalanceSheets_E_All_Data_(Normalized).zip).
- **FBSH**: [Food Balances: Food Balances (-2013, old methodology and population)](https://bulks-faostat.fao.org/production/FoodBalanceSheetsHistoric_E_All_Data_(Normalized).zip).
- **FDIQ**: [Food and Diet: Intake (based on individual quantitative dietary surveys)](https://bulks-faostat.fao.org/production/Individual_Quantitative_Dietary_Data_Food_and_Diet_E_All_Data_(Normalized).zip).
- **FO**: [Forestry: Forestry Production and Trade](https://bulks-faostat.fao.org/production/Forestry_E_All_Data_(Normalized).zip).
- **GLE**: [Climate Change: Agrifood systems emissions: Emissions from Livestock](https://bulks-faostat.fao.org/production/Emissions_livestock_E_All_Data_(Normalized).zip).
- **GT**: [Climate Change: Agrifood systems emissions: Emissions totals](https://bulks-faostat.fao.org/production/Emissions_Totals_E_All_Data_(Normalized).zip).
- **QCL**: [Production: Crops and livestock products](https://bulks-faostat.fao.org/production/Production_Crops_Livestock_E_All_Data_(Normalized).zip).
- **SCL**: [Food Balances: Supply Utilization Accounts (2010-)](https://bulks-faostat.fao.org/production/SUA_Crops_Livestock_E_All_Data_(Normalized).zip).
- **TCL**: [Trade: Crops and livestock products](https://bulks-faostat.fao.org/production/Trade_CropsLivestock_E_All_Data_(Normalized).zip).
- **TI**: [Trade: Trade Indices](https://bulks-faostat.fao.org/production/Trade_Indices_E_All_Data_(Normalized).zip).
- **TM**: [Trade: Detailed trade matrix](https://bulks-faostat.fao.org/production/Trade_DetailedTradeMatrix_E_All_Data_(Normalized).zip).

## Verifiche integrali

Ogni record del CSV fonte è confrontato con lo staging e ogni cella DATI dei 290 Excel è riletta e confrontata. Testi, codici, unità, flag, campi aggiuntivi e testo numerico originale sono controllati esattamente; i valori numerici sono verificati con tolleranza relativa e assoluta di 1e-14.

Dizionari, nuove appendici del registro, riepiloghi, catalogo e manifest nei file finali sono confrontati integralmente. Ogni membro Excel negli ZIP è verificato per byte e SHA256 contro il file riletto, con controllo CRC; l'esito completo è PASS.

L'archivio ufficiale del lotto è [FAOSTAT RFM: Detailed trade matrix, fertilizers](https://bulks-faostat.fao.org/production/Fertilizers_DetailedTradeMatrix_E_All_Data_(Normalized).zip). URL, data di aggiornamento originale, data del trasferimento, dimensione, hash e intestazioni fonte sono conservati nei file e nell'audit; la traccia dei trasferimenti distingue RFM selezionato da QCL ispezionato e rinviato.
