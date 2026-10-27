# Open data internazionali: guida al lotto 30

Il lotto acquisisce integralmente FAOSTAT SCL, “Food Balances: Supply Utilization Accounts (2010-)”, dal [file ufficiale normalizzato](https://bulks-faostat.fao.org/production/SUA_Crops_Livestock_E_All_Data_(Normalized).zip). Il [catalogo ufficiale](https://bulks-faostat.fao.org/production/datasets_E.json) e la fonte sono stati recuperati soltanto dopo il completamento del controllo preventivo degli allegati e del registro.

## Dati acquisiti e cumulativo

| Misura | Lotto 30 | Cumulativo lotti 1–30 |
|---|---:|---:|
| Righe / osservazioni contabili | 11.615.212 | 126.867.053 |
| Identità di serie per dataset | 980.880 | 9.734.400 |
| Excel dati | 360 | 8.096 |
| Valori numerici | 11.581.236 | 122.644.066 |

La copertura è 2010–2023, con 213 aree originali della fonte. Queste aree non sono automaticamente altrettanti paesi: classificazioni amministrative non vengono inferite.

- **Valori**: 33.976 righe non numeriche conservate senza imputare zeri; 3.399.982 zeri effettivi conservati.
- **Flag**: E: 2.979.747; I: 1.749.391; A: 1.196.607; X: 5.655.488; M: 33.976; F: 3. Stime, imputazioni o proiezioni della fonte mantengono i flag e non diventano automaticamente dati osservati.
- **Confezionamento**: 91 ZIP dati (paesi-e-territori: 73; aggregati-statistici: 17; aree-non-classificate: 1), 10 nuove appendici e sei supporti, per 107 allegati complessivi. Gli ZIP sono confezioni, non conteggi di paesi.

## Recupero preventivo e continuità

Sono stati nuovamente recuperati dalla libreria tutti i 132 allegati del lotto 29. Per ciascuno sono stati verificati byte e SHA256 contro ricevuta e manifest pubblicati; per i 121 ZIP dati anche CRC e impronte dei 484 Excel interni.

Sono stati inoltre recuperati i file originali delle 94 parti del registro e riletti tutti gli 11 campi di ogni identità. Impronte dei campi decodificati e conteggi corrispondono agli audit pubblicati: 8.753.520 identità uniche, 115.251.841 righe e 111.062.830 numerici.

La parte 1 del registro è nel foglio REGISTRO_SERIE dell’indice30, con XML copiato byte per byte dall’indice29 nuovamente recuperato. Le parti 2–94 restano i file originali pubblicati, invariati; le nuove appendici sono 95–104, per 104 parti complessive.

Le celle DATI storiche non sono state integralmente rilette nel lotto 30: la relativa QA contenutistica rimane ereditata e distinta dalle nuove verifiche su manifest, hash, CRC, registro e modello. Il controllo CRC dei sette ZIP di continuità del lotto14 resta ereditato; i file originali delle parti contenute sono stati recuperati nuovamente e verificati individualmente.

Per predisporre memoria sufficiente è stato eliminato soltanto un vecchio indice SQLite derivato del recupero23, ricostruibile dai registri originali pubblicati. La rimozione della copia di lavoro è documentata con byte e SHA256; nessun originale pubblicato, dato o conteggio storico è stato modificato, né quella copia locale è stata usata come prova del nuovo recupero.

## Fedeltà alla fonte e confronto

Sono conservati tutti i 14 campi originali, rappresentati nelle 16 colonne comuni e nelle 8 aggiuntive. Valore numerico e testo originale restano separati; unità, codici e nomi, note presenti, flag, annualità e provenienza non vengono convertiti, aggregati o completati arbitrariamente.

La chiave canonica comprende tutti i campi Code tranne Year Code, più Unit. L’identità è SHA256 di FAOSTAT|SCL|JSON canonico, qualificata per dataset; i conteggi non sono conteggi di fenomeni semanticamente armonizzati.

Il confronto usa tutte le 8.753.520 identità e chiavi dimensionali complete delle 94 parti recuperate. Risultati: 0 intersezioni di identità, 155868 candidati dimensionali completi e 0 ripetizioni serie-periodo.

Il confronto di contenuto ha esaminato 155.868 coppie candidate, riferite a 153.894 serie SCL distinte: 132.194 coppie con TCL, 21.698 con QCL e 1.976 con EI. Sono stati nuovamente recuperati e verificati 152 archivi storici e gli hash di 1022 Excel.

Tutte le 21.762.494 righe dei tre dataset storici sono state scansionate per identità. Per le serie candidate sono stati inventariati tutti i periodi; i campi originali sono stati decodificati nel periodo SCL 2010–2023 e confrontati in ogni periodo comune. Fuori da questo intervallo sono stati riletti identità, periodo e digest XML della riga, non tutte le celle interpretate.

I confronti contano 1.708.254 punti comuni per coppia, con 436.965 differenze numeriche e 174.715 differenze di flag. Sono 48.712 le serie SCL i cui record originali risultano interamente contenuti in almeno una serie candidata storica; il corrispondente numero sul solo confronto numerico e flag è 49.065. Questi conteggi non equivalgono a nuove osservazioni uniche trasversali ai dataset.

SCL viene conservato integralmente come pubblicazione distinta, con provenienza, coperture e divergenze esplicite: nessuna riga esclusa, nessuna modifica retroattiva e nessuna pretesa di novità semantica per i punti sovrapposti. Il CSV di riconciliazione contiene una riga per ciascuna coppia, con periodi, esiti dei valori, testo numerico, flag, note, schema e provenienza; le corrispondenze dei soli codici non sono trattate come duplicati accertati.

L’ordine relativo originale delle righe entro ciascuna area viene conservato. Lo staging è riletto integralmente confrontando le impronte di tutti i campi originali con la fonte e verificando l’unicità serie-periodo, senza presumere contiguità delle serie e senza aggregare le righe DATI.

La codifica è verificata per ciascun membro: utf-8. Decodifica stretta e ricodifica restituiscono lo stesso SHA256 dei byte originali; non sono usati caratteri sostitutivi.

I dizionari originali sono consegnati integralmente: SUA_Crops_Livestock_E_AreaCodes.csv (213 righe); SUA_Crops_Livestock_E_Elements.csv (21 righe); SUA_Crops_Livestock_E_Flags.csv (6 righe); SUA_Crops_Livestock_E_ItemCodes.csv (485 righe). Eventuali voci ripetute o dizionari con sole intestazioni restano tali, senza integrazioni inventate.

Paesi e territori, aggregati statistici e aree non classificate sono confezionati separatamente. Le classificazioni ereditate sono riutilizzate solo per corrispondenze esatte di codice originale e nome con il manifest24 recuperato nella catena degli audit, senza inferenze amministrative.

Importazioni ed esportazioni eventualmente presenti restano distinte, senza saldi. Non vengono inventati partner assenti dallo schema; per i dati bilaterali i ruoli originali non vengono scambiati.

## Catalogo e copertura dei portali

Il confronto diretto del catalogo corrente col checkpoint29 è documentato in catalog_comparison.json. Il confronto byte-per-byte risulta identico; le variazioni per risorsa sono elencate nel riscontro, senza alterare retroattivamente i conteggi consegnati.

La continuità con il checkpoint19 del 25 ottobre 2026 è ereditata dalla catena degli audit pubblicati recuperati, non dichiarata come un nuovo confronto diretto col file19. Per SCL, il catalogo indica 12.955.142 righe e il CSV effettivo ne contiene 11.615.212, differenza -1.339.930.

FAOSTAT passa a 68 risorse acquisite su 69 e resta TM. Gli altri sette portali, data.europa.eu, UNdata, World Bank, OECD, Eurostat, IMF e WHO/GHO, non sono stati riverificati nel lotto30: la loro copertura rimane esplicitamente ereditata.

## Formato, QA e riproduzione

Ogni Excel e ZIP consegnato è strettamente inferiore a 29.000.000 byte. Rimangono margine A, titolo riga2, intestazioni riga3, dati dalla riga4, blocco D4, griglia nascosta, larghezze e stili del modello pubblicato.

La QA comprende rilettura di tutte le nuove celle DATI dagli Excel effettivamente contenuti negli ZIP, confronto dei campi originali, dizionari e registro, riepiloghi, CRC, SHA256, stili e layout. Le formule dello stato cumulativo sono ricalcolate e le cache verificate, senza alterare gli stili; righe dei lotti precedenti, degli altri sette portali e delle altre risorse FAOSTAT restano invariate.

Le anteprime PIL sono viewport campionati delle celle e degli stili nativi, non schermate Office né una revisione visiva integrale. I contenuti lunghi possono essere troncati dalle larghezze storiche nel viewport, mentre le celle complete sono state verificate.

L’audit include manifest, prove e codice. Per contenere la dimensione non incorpora gli audit29,28,27 e22: questi sono riferiti con identificativi, byte e SHA256, sono stati recuperati nuovamente e vanno recuperati dalla libreria per la riproduzione, senza presumere vecchi file locali.

La fonte ZIP non è duplicata nell’audit: URL, byte, SHA256 e impronte dei campi sono conservati, mentre tutti i dati acquisiti sono negli Excel allegati. La ricevuta finale elenca gli hash di tutti gli altri allegati e, dopo la loro effettiva pubblicazione, i relativi identificativi; il proprio hash e identificativo sono verificati separatamente per evitare ricorsioni.
