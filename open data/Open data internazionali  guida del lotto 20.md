# Open data internazionali: guida al lotto 20

Il lotto 20 acquisisce integralmente FAOSTAT GT, [Climate Change: Agrifood systems emissions: Emissions totals](https://bulks-faostat.fao.org/production/Emissions_Totals_E_All_Data_(Normalized).zip), con 2.500.090 osservazioni, 64.430 nuove identità e 281 Excel dati. Il cumulativo dei lotti 1–20 raggiunge 42.872.418 osservazioni, 3.571.243 identità, 5.112 Excel dati e 39.012.295 valori numerici.

## Fonte e copertura

Sono conservate tutte le righe del CSV e tutte le annualità disponibili, con estremi 1961–2050; gli estremi non garantiscono una sequenza completa per ogni serie. Le righe numeriche sono 2.500.090, quelle non numeriche 0; nessuna riga non numerica o mancante è stata trasformata in zero, mentre gli zeri effettivi sono mantenuti.

L'aggiornamento originale indicato nel [catalogo ufficiale FAOSTAT](https://bulks-faostat.fao.org/production/datasets_E.json) è 2025-10-28T00:00:00. Il confronto con il [catalogo bulk](https://bulks-faostat.fao.org/production/datasets_E.json) del checkpoint del 25 ottobre 2026 non rileva aggiunte, rimozioni o cambiamenti: restano 69 risorse, ora 58 acquisite e 11 residue; nessun conteggio storico è stato modificato retroattivamente.

Il catalogo dichiara 2.415.025 righe GT, mentre il CSV scaricato ne contiene 2.500.090: scostamento di 85.065 righe, documentato senza inventare o sopprimere record. I periodi futuri 2030 e 2050 comprendono 21.304 righe, tutte con flag fonte F conservato; non sono presentate automaticamente come dati osservati.

## Formato e geografie

I dati mantengono le 16 colonne comuni e tutti i campi originali non già rappresentati. Valori numerici e testo originale, unità, codici, note, flag, provenienza e periodi sono conservati senza conversioni, aggregazioni non richieste o armonizzazioni semantiche non dimostrate.

Il layout mantiene margine A, titolo alla riga 2, intestazioni alla riga 3, dati dalla riga 4, blocco D4 e griglia nascosta. Gli stili derivano dall'Excel pubblicato del lotto 19 e sono verificati sui nuovi file; tutte le stringhe originali sono scritte come testo, non come formule.

La ripartizione riguarda 243 geografie classificate negli archivi come paesi/territori, anche storici, e 38 aggregati statistici, con 243 Excel per i primi e 38 per i secondi. Non è un conteggio di Stati sovrani attuali; le denominazioni storiche e le entità statistiche restano quelle della fonte. I dati sono confezionati in 11 ZIP per paesi/territori e 3 ZIP per aggregati: i conteggi degli ZIP, degli Excel e delle geografie sono distinti.

Classificazioni e identificativi d'archivio derivano dai dizionari fonte o dalle corrispondenze esatte dei nomi nei manifest pubblicati, con evidenza per ciascuna geografia. Codici e denominazioni originali restano nelle celle; non vengono inferite regioni o appartenenze amministrative.

## Recupero preventivo effettivamente svolto

Prima di acquisire GT sono stati recuperati dalla libreria l'audit e l'indice 19 e gli allegati pubblicati necessari. Sono stati verificati 38 allegati del lotto 19: 37 file confrontati per byte e SHA256 con il manifest, più l'audit stesso verificato per CRC, leggibilità e corrispondenza con una seconda copia recuperata.

I 26 ZIP del lotto 19 sono stati verificati per CRC e i 290 Excel contenuti per byte e SHA256. Questa verifica di integrità non è una nuova rilettura delle celle DATI storiche: i controlli integrali sui dati dei lotti 1–19 restano esplicitamente ereditati dagli audit pubblicati.

Sono state rilette tutte le righe delle 38 parti del registro cumulativo, ricostruendo 3.506.813 identità uniche, 40.372.328 osservazioni e 36.512.205 numerici. I conteggi per parte sono nel rapporto di recupero; per FAOSTAT è stato ricalcolato anche l'hash dell'identità sulla chiave originaria.

## Continuità del registro

- **Parte 1**: foglio REGISTRO_SERIE nell'indice 20, trasferito senza modifiche dall'indice 19; XML identico byte per byte, SHA256 `b0512f0d7688578e2f3a55cd39f51ed2af1d1950ba4a24069e487dfa0004c791`.
- **Parti 2–21**: file originali nei sette ZIP di continuità del lotto 14, estratti senza modifiche e verificati contro gli hash ereditati dall'audit 19.
- **Parti 22–31**: file separati originali dei lotti 14–18, conservati invariati.
- **Parti 32–38**: file originali del lotto 19, conservati invariati; le parti 32–37 hanno 100.000 identità ciascuna e la parte 38 ne ha 69.432.
- **Nuove parti**: 39 (64.430 identità).

Le identità GT usano SHA256 di FAOSTAT|GT|JSON canonico delle dimensioni codificate e dell'unità, escludendo Year Code; la dimensione completa resta visibile in ogni riga. Non vi sono intersezioni delle identità per dataset né ripetizioni serie-periodo interne a GT; il conteggio delle identità non è un conteggio armonizzato di fenomeni statistici unici fra dataset.

## Riconciliazione completa dei candidati GT–GI

Sono state rilevate 1.717 coppie con dimensioni codificate e unità esatte rispetto a GI, non eliminate né accettate sulla sola base dei codici. Sono stati recuperati i sei ZIP del lotto 10, verificati CRC e hash dei 325 Excel contro l'indice 10, scansionate le 428.347 righe GI e confrontati integralmente periodi, numeri, testo originale, flag, note e provenienza per tutte le identità candidate.

Il confronto copre 55.774 punti comuni: 2.953 differiscono numericamente alla tolleranza 1e-14 e 0 differiscono nei flag; 52.821 coincidono per numero e flag. Le coppie con copertura completa e numeri/flag coincidenti sono 115; i dettagli per coppia e i campioni sono nell'audit.

Il confronto di tutti i campi originali del CSV identifica 51.071 record interamente coincidenti e 1.503 coppie in cui tutti i record GT sono già ripubblicati in GI. Queste coincidenze sono dichiarate, non trasformate in un'affermazione di novità semantica.

GT è conservato integralmente come dataset distinto, non come nuova versione temporale di GI: entrambi riportano aggiornamento 2025-10-28, con URL e contesto di dominio differenti. L'audit distingue anche i record originali interamente coincidenti, che non vengono dichiarati fenomeni o serie semanticamente nuovi; nessuna fusione o sostituzione retroattiva delle serie GI e nessuna eliminazione basata soltanto sui codici.

## QA del lotto 20

Ogni campo originale del CSV è confrontato nuovamente con lo staging. Tutte le celle dei fogli DATI nuovi sono rilette; il record fonte completo viene ricostruito e confrontato, insieme a identità, dimensioni, campi comuni, unità, flag, testo numerico e provenienza; i numeri hanno tolleranza relativa e assoluta 1e-14.

Dizionari, appendici nuove, indice e stato cumulativo sono riletti e confrontati. Gli Excel contenuti negli ZIP sono verificati per byte, SHA256 e CRC, e ogni Excel e ZIP consegnato è strettamente inferiore a 29.000.000 byte.

## Coda residua e altri portali

Restano EA, FBS, FBSH, FDIQ, FO, GLE, QCL, SCL, TCL, TI, TM. QCL resta non acquisito: l'evidenza ereditata del lotto 19 contiene 4.154 coppie candidate, non duplicati accertati né necessariamente 4.154 serie QCL distinte; FO conserva 794 candidati con FOP da riconciliare e FDIQ richiede una mappatura fedele allo schema per indagini, senza inventare geografie o annualità.

Le evidenze originali dei rinvii sono incluse nell'audit e dichiarate ereditate, non nuove ispezioni. Nessuna risorsa rinviata è trattata come esclusione definitiva e nessuna riga è eliminata sulla sola corrispondenza dei codici.

Gli altri sette portali, data.europa.eu, UNdata, World Bank, OECD, Eurostat, IMF e WHO/GHO, non sono stati riverificati nel lotto 20. La loro copertura resta quella ereditata, distinta dalla nuova acquisizione FAOSTAT; la raccolta integrale degli otto portali non è dichiarata completata.
