# Open data internazionali: guida al lotto 25

Il lotto acquisisce integralmente FAOSTAT FDIQ, «Food and Diet: Intake (based on individual quantitative dietary surveys)», dopo il recupero preventivo dei 46 allegati del lotto 24 e la rilettura completa delle 47 parti del registro. Lo schema per indagini rimane fedele alla fonte: non vengono inventati paesi, unità amministrative o annualità ([archivio ufficiale FAOSTAT](https://bulks-faostat.fao.org/production/Individual_Quantitative_Dietary_Data_Food_and_Diet_E_All_Data_(Normalized).zip)).

## Contenuto e conteggi

- **Record FDIQ:** 2.191.084, relativi a 8 indagini, conservati in 59 Excel dati e 26 ZIP per indagini fonte. Otto indagini non significa otto paesi, e i contenitori ZIP non sono un conteggio di paesi ([archivio ufficiale FAOSTAT](https://bulks-faostat.fao.org/production/Individual_Quantitative_Dietary_Data_Food_and_Diet_E_All_Data_(Normalized).zip)).
- **Valori numerici:** 1.956.551; 234.533 record senza valore numerico sono mantenuti senza imputare zeri. Restano distinti i 312.878 zeri effettivi, con testo numerico originale conservato esattamente ([archivio ufficiale FAOSTAT](https://bulks-faostat.fao.org/production/Individual_Quantitative_Dietary_Data_Food_and_Diet_E_All_Data_(Normalized).zip)).
- **Identità dimensionali:** 2.191.084 per dataset e indagine; ogni chiave completa compare una volta nella fonte. Non sono necessariamente serie annuali, persone, fenomeni nuovi o misure semanticamente armonizzate ([archivio ufficiale FAOSTAT](https://bulks-faostat.fao.org/production/Individual_Quantitative_Dietary_Data_Food_and_Diet_E_All_Data_(Normalized).zip)).
- **Registro:** nuove appendici dalla parte 48 alla 69; parti 48–68 da 100.000 identità e parte 69 da 91.084. La parte 1 è copiata come XML invariato dall'indice 24, e le parti 2–47 già pubblicate non sono modificate.
- **Consegna:** 54 allegati: 26 ZIP dati, 22 appendici Excel, indice, stato cumulativo, dizionari, questa guida, audit e ricevuta SHA256. Ogni Excel e ZIP è strettamente inferiore a 29.000.000 byte.

Il cumulativo consegnato dei lotti 1–25 è di 63.201.399 osservazioni, 6.415.710 identità per dataset, 6.157 Excel dati e 59.012.388 valori numerici. I conteggi dei lotti precedenti restano invariati e le appendici nuove sono in ordine di riga della fonte.

## Mappatura dedicata alle indagini

- **Archivio:** Survey Code e Survey originali identificano l'indagine, senza ricavare un paese dal prefisso del codice o dal nome. Le colonne geografiche comuni riportano Geographic Level Code e Geographic Level, mentre il foglio TERRITORI conserva i livelli della specifica indagine ([archivio ufficiale FAOSTAT](https://bulks-faostat.fao.org/production/Individual_Quantitative_Dietary_Data_Food_and_Diet_E_All_Data_(Normalized).zip)).
- **Periodo:** la fonte non ha Area, Area Code, Year o Year Code. Periodo originale e gli estremi Primo periodo/Ultimo periodo del nuovo registro restano quindi vuoti; i nomi delle indagini, anche quando contengono anni, rimangono etichette originali e non vengono annualizzati ([archivio ufficiale FAOSTAT](https://bulks-faostat.fao.org/production/Individual_Quantitative_Dietary_Data_Food_and_Diet_E_All_Data_(Normalized).zip)).
- **Sesso ed età:** Sex Code e Population Age Group Code alimentano i rispettivi campi comuni; codici e descrizioni originali restano anche nelle colonne della fonte. Non vengono costruite classi nuove o aggregati aggiuntivi ([archivio ufficiale FAOSTAT](https://bulks-faostat.fao.org/production/Individual_Quantitative_Dietary_Data_Food_and_Diet_E_All_Data_(Normalized).zip)).
- **Chiave:** tutti i campi originali che terminano in « Code», incluso Survey Code, più Unit, in JSON canonico; identità SHA256 di `FAOSTAT|FDIQ|JSON`. I 16 campi comuni sono seguiti dai 15 campi originali non sostituiti da Value, Unit e Flag, per 31 colonne dati oltre al margine A.
- **Stato:** tutte le righe mantengono il flag E, «Estimated value» nel dizionario originale. Non vengono riclassificate come dati osservati; unità, note, numeri, testo numerico e provenienza restano invariati ([archivio ufficiale FAOSTAT](https://bulks-faostat.fao.org/production/Individual_Quantitative_Dietary_Data_Food_and_Diet_E_All_Data_(Normalized).zip)).

## Recupero e controlli

- **Nuove verifiche storiche:** recuperati e verificati tutti i 46 allegati24; SHA256 e byte, CRC dei 38 ZIP dati, hash dei 250 Excel contenuti e CRC dell'audit e degli Excel di supporto. Riletti tutti gli undici campi di tutte le 47 parti: 4.224.626 identità, 61.010.315 record e 57.055.837 numerici confermati prima dell'acquisizione FDIQ.
- **Continuità:** per le parti 2–21 sono stati nuovamente scaricati gli originali pubblicati nel lotto13, byte-identici secondo SHA256 agli originali nei sette ZIP di continuità14 riportati nell'audit24. I CRC di quei sette ZIP14 sono ereditati e non nuovamente eseguiti; non vengono presentati come nuove verifiche.
- **Riconciliazione:** zero intersezioni con le identità precedenti e zero coppie dimensionali esatte. La prova confronta anche gli schemi completi delle chiavi dimensionali: lo schema FDIQ non compare fra i 37 schemi ricostruiti nello storico; ciò non prova un'assenza di equivalenze semantiche fra fonti diverse.
- **QA nuova:** confronto integrale fonte/staging streaming e rilettura di tutte le celle dei DATI effettivamente contenuti nei nuovi ZIP, tutti i metadati, dizionari e appendici; controllo di indice, stato, formule ricalcolate e cache senza errori. Il testo originale è confrontato esattamente; per i numeri Excel si applicano tolleranze relativa e assoluta di 1e-12, senza alterare il testo numerico originale.
- **Formato:** banca stili OOXML uguale al modello pubblicato recuperato; verifica di tutte le celle serializzate e di ogni foglio: margine A, titolo alla riga2, intestazioni alla riga3, dati dalla riga4, blocco D4 e griglia nascosta. Nessun ridisegno, conversione o nuova impostazione di stampa.
- **Limite visivo:** sei viewport campionati ricostruiti dalle celle, larghezze, altezze e font nativi, non schermate di Excel/LibreOffice né un'ispezione visiva integrale. JSON, SHA256 e denominazioni lunghe possono essere ritagliati alla larghezza ereditata: il contenuto memorizzato completo è comunque verificato cella per cella.
- **QA ereditata:** nessuna nuova rilettura integrale dei DATI storici. I precedenti controlli contenutistici restano esplicitamente ereditati, distinti da manifest, hash, CRC e nuova rilettura del registro.
- **Spazio operativo:** rilasciate soltanto nuove copie temporanee di recupero25 dopo le verifiche; gli originali pubblicati rimangono immutati. Le ricollocazioni di cache sono lossless, verificate tramite hash e documentate, con percorsi di accesso mantenuti.

## Catalogo e copertura

Il catalogo corrente contiene 69 risorse ed è byte-identico ai checkpoint19 e24, senza modifiche retroattive ai conteggi consegnati; per FDIQ le 2.191.084 righe indicate coincidono con il CSV acquisito. La copertura del checkpoint diventa FAOSTAT 63/69, con sei residue: EA, FBSH, SCL, TCL, TI e TM ([catalogo ufficiale FAOSTAT](https://bulks-faostat.fao.org/production/datasets_E.json)).

Gli altri sette portali, data.europa.eu, UNdata, World Bank, OECD, Eurostat, IMF e WHO/GHO, mantengono la copertura ereditata e non vengono riverificati nel lotto25. Le relative righe dello stato e tutte le righe dei lotti1–24 sono conservate; la correzione24 di Sub-Saharan Africa come aggregato statistico non è annullata.

## Uso degli allegati

L'indice elenca tutti gli Excel, gli ZIP, le indagini e le 69 parti del registro; lo stato conserva la continuità degli otto portali. Il foglio DATI_FDIQ_1 di ogni Excel contiene i dati, mentre LEGGIMI, DIZ_DATASET e TERRITORI descrivono mappatura, fonte e livelli originali.

L'audit contiene manifest, hash, prove QA, cataloghi, dizionari originali, codice di lavoro e copia byte-identica del bulk FDIQ. La copia della fonte è evidenza riproducibile, non un secondo conteggio di dati; la ricevuta esterna include SHA256 e byte anche dell'audit, escludendo necessariamente il proprio hash autoreferenziale.
