# Open data internazionali: guida al lotto 21

Il lotto 21 acquisisce integralmente [FAOSTAT FO, Forestry: Forestry Production and Trade](https://bulks-faostat.fao.org/production/Forestry_E_All_Data_(Normalized).zip), dopo la riconciliazione del rinvio storico con FOP. Sono pubblicati 2.457.869 record, 2.457.869 valori numerici, 0 righe non numeriche e 84.549 identità per dataset; nessuna di queste identità è automaticamente un nuovo fenomeno statistico armonizzato.

## Fonte e copertura

I periodi originali hanno estremi 1961–2024; non viene inventata continuità temporale per le singole serie. Aggiornamento originale: 2026-01-09T00:00:00; unità, codici, etichette, note, flag, provenienza e testo numerico restano quelli della fonte, senza conversioni o imputazioni di zeri. Gli zeri effettivi sono mantenuti, mentre stime e proiezioni non diventano dati osservati.

Il [catalogo ufficiale](https://bulks-faostat.fao.org/production/datasets_E.json) dichiara 2.443.480 righe FO contro 2.457.869 nel CSV, differenza 14.389. Il catalogo corrente è identico byte per byte a quello pubblicato nel lotto 20: 69 risorse, senza aggiunte, rimozioni o modifiche. Lo scostamento fra catalogo e CSV è documentato senza alterare retroattivamente alcun conteggio consegnato.

## File e geografie

I 274 Excel dati sono confezionati in 13 ZIP: 10 per paesi/territori e 3 per aggregati statistici. Le geografie sono 240 paesi/territori, anche storici, e 34 aggregati; conteggi ZIP, file e geografie sono distinti, non un conteggio di Stati sovrani attuali.

Ogni Excel e ZIP è strettamente sotto 29.000.000 byte. Sono mantenute le 16 colonne comuni e tutti i campi originali non già rappresentati, con margine A, titolo alla riga 2, intestazioni 3, dati 4, blocco D4, griglia nascosta e stili del modello pubblicato e recuperato. Le stringhe originali sono testo, non formule.

Le classificazioni d'archivio sono ereditate da manifest pubblicati con corrispondenze esatte dei nomi o derivano da evidenze fonte esplicite. Nessuna attribuzione amministrativa viene inferita; le evidenze per ciascuna geografia sono nell'audit.

## Recupero preventivo e registro

Prima di acquisire FO sono stati nuovamente recuperati e verificati tutti i 21 allegati del lotto 20: 19 contro hash e byte dell'audit, l'audit contro la ricevuta pubblicata e una seconda copia contestuale, la ricevuta mediante confronto delle sue 20 righe. Sono verificati i CRC dei 14 ZIP dati e SHA256/byte di tutti i 281 Excel contenuti; non si tratta di una nuova rilettura delle celle DATI storiche.

Tutte le 39 parti del registro precedente sono state rilette e ricostruite: 3.571.243 identità uniche, 42.872.418 osservazioni e 39.012.295 valori numerici. Le identità FAOSTAT sono ricalcolate dalle chiavi originali; non vi sono intersezioni delle nuove identità per dataset né ripetizioni serie-periodo interne a FO.

La parte 1 è copiata nell'indice 21 con XML identico byte per byte all'indice 20, SHA256 `b0512f0d7688578e2f3a55cd39f51ed2af1d1950ba4a24069e487dfa0004c791`. Le parti 2–39 restano i file pubblicati immutati nelle rispettive consegne; le nuove appendici sono 40 (84.549 identità). Non si presume la disponibilità futura dei vecchi percorsi locali: i recuperi vanno eseguiti dalla libreria.

## Riconciliazione FO–FOP

Il rinvio storico del lotto 15 è riesaminato sul nuovo download FO, non trattato come esclusione permanente. Il confronto corrente individua 794 coppie candidate con dimensioni codificate e unità esatte; sono state confrontate coperture, valori numerici, testo originale, flag, note, tutti i campi originali e provenienza con il FOP effettivamente pubblicato nel lotto 4.

Il confronto riguarda 3.964 periodi comuni: 3.061 differenze numeriche, 2.601 differenze di flag e 749 record coincidenti su tutti i campi originali comuni. Il confronto rigoroso anche dello schema completo restituisce 0 record identici, perché Note è vuoto in FO e assente dai campi originali disponibili nei file FOP pubblicati: è una differenza di schema, non una diversa nota testuale né prova di fenomeni differenti.

Non si eliminano record solo per uguaglianza di codici e non si dichiara novità semantica per i punti coincidenti; risultati per coppia, differenze di campo e di schema, aggiornamenti fonte, periodi esclusivi e campioni sono nell'audit. Il dato consegnato non viene modificato per rendere artificialmente identici o diversi gli schemi.

FO è conservato integralmente come dataset distinto di produzione e commercio forestale, dopo confronto dei contenuti con l’indagine FOP sulle capacità di pasta e carta. Su 3964 periodi comuni si rilevano 3061 differenze numeriche, 2601 differenze di flag, 749 punti coincidenti per numero e flag e 749 record coincidenti su tutti i campi originali comuni. I record identici anche nello schema completo sono 0: il campo Note è vuoto in FO ma assente dai campi originali disponibili nei file FOP pubblicati, differenza di schema e non di testo delle note. Le coincidenze non sono dichiarate fenomeni o serie semanticamente nuovi; coperture e provenienza restano distinte. Nessuna fusione, eliminazione basata solo sui codici o sostituzione retroattiva di FOP.

## QA nuova e QA ereditata

Tutti i campi CSV FO sono confrontati con lo staging, poi tutte le celle DATI nuove vengono rilette e confrontate ricostruendo il record originale. Il testo numerico è esatto; i valori Excel sono confrontati con tolleranza assoluta e relativa 1e-14, senza riscalamenti.

Dizionari, nuove appendici, indice e stato sono riletti e confrontati. La parte 1 XML è verificata identica, le righe storiche dei lotti e degli altri sette portali restano immutate, tutte le cache delle formule sono ricalcolate su copia e ripristinate senza modificare gli stili. SHA256, byte, CRC, banche degli stili e layout di tutti i nuovi fogli sono verificati; le anteprime visuali hanno un ambito campionato dichiarato, non una rilettura visiva di tutte le celle.

Le celle vuote hanno la stessa rappresentazione del modello nativo. Un controllo dedicato confronta anche la semantica dei valori mancanti con il lettore Excel, senza trasformare celle vuote in stringhe di lunghezza zero o in zeri numerici.

La QA storica integrale resta ereditata dagli audit, salvo la nuova rilettura mirata FOP documentata nel rapporto di riconciliazione. Nessuna nuova rilettura integrale degli altri DATI storici viene dichiarata.

## Cumulativo e coda residua

Il cumulativo 1–21 è 45.330.287 osservazioni, 3.655.792 identità per dataset, 5.386 Excel dati e 41.470.164 valori numerici, in 40 parti del registro. FAOSTAT è 59/69 e restano EA, FBS, FBSH, FDIQ, GLE, QCL, SCL, TCL, TI, TM.

QCL resta non acquisito: l'evidenza ereditata del lotto 19 contiene 4.154 coppie candidate, non duplicati accertati né necessariamente 4.154 serie distinte. FDIQ resta non acquisito e richiede una mappatura dedicata fedele allo schema per indagini, senza inventare geografie o annualità; nessuno dei due rinvii è un'esclusione definitiva.

Gli altri sette portali, data.europa.eu, UNdata, World Bank, OECD, Eurostat, IMF e WHO/GHO, non sono stati riverificati nel lotto 21. La loro copertura resta ereditata e la raccolta integrale degli otto portali non è dichiarata completa.
