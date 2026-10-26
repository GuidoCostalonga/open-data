# Open data internazionali: guida al lotto 22

Il lotto 22 acquisisce integralmente [FAOSTAT QCL, Production: Crops and livestock products](https://bulks-faostat.fao.org/production/Production_Crops_Livestock_E_All_Data_(Normalized).zip), dopo confronto dei candidati con lo storico. Sono consegnati 4.209.110 record, 4.114.755 valori numerici, 94.355 righe non numeriche e 78.974 identità per dataset, non fenomeni statisticamente armonizzati.

## Fonte, valori e copertura

Annualità con estremi 1961–2024, aggiornamento fonte 2025-12-31T00:00:00. Numeri, testo numerico originale, unità, codici, note, flag e provenienza restano quelli originali; nessuna conversione o imputazione di zeri. I valori mancanti e non numerici non diventano zeri, mentre gli zeri effettivi sono conservati; stime e proiezioni non diventano dati osservati.

Il [catalogo ufficiale](https://bulks-faostat.fao.org/production/datasets_E.json) riporta 4.209.110 righe; il CSV ne contiene 4.209.110, scostamento 0. Il catalogo corrente ha 69 risorse; identità JSON con il checkpoint 21: True, hash uguali: True. Aggiunte, rimozioni e modifiche sono documentate senza alterare conteggi già consegnati.

È stato inoltre recuperato il catalogo del checkpoint del 25 ottobre 2026 direttamente dall'audit pubblicato del lotto 19: coincidenza JSON True e coincidenza byte per byte True. Il confronto è nuovo, non soltanto ereditato dagli audit intermedi; nome del membro e SHA256 sono nel rapporto allegato.

I 249 Excel dati sono in 23 ZIP, per 210 paesi/territori anche storici e 34 aggregati statistici. I conteggi di ZIP e geografie sono distinti; non si tratta di un conteggio di Stati sovrani attuali. Le classificazioni ereditate sono tracciate per corrispondenze esatte, senza inferire livelli amministrativi.

Tutti gli Excel e ZIP consegnati sono strettamente sotto 29.000.000 byte. Il ZIP ufficiale fonte supera questo limite e non è duplicato negli allegati: l'audit ne conserva URL, dimensione, SHA256, intestazioni HTTP, metadati e dizionari; il file completo resta recuperabile dalla fonte indicata.

## Recupero preventivo e continuità

Prima di acquisire QCL sono stati recuperati dalla libreria tutti i 20 allegati del lotto 21. Diciotto sono confrontati con hash/byte dell'audit; l'audit è verificato contro la ricevuta, della quale sono confrontate tutte le 19 righe. Verificati CRC dei 13 ZIP e hash/byte di tutti i 274 Excel dati, senza dichiararne una nuova rilettura integrale delle celle.

Tutte le 40 parti del registro sono rilette: 3.655.792 identità, 45.330.287 osservazioni e 41.470.164 numerici. Le identità FAOSTAT sono ricalcolate dalle chiavi originali. La nuova memorizzazione interna è compressa reversibilmente; contenuti e tipi del registro e della fonte sono verificati, non sostituiti da inferenze.

Parte 1 copiata nell'indice 22 con XML identico byte per byte all'indice 21, SHA256 `b0512f0d7688578e2f3a55cd39f51ed2af1d1950ba4a24069e487dfa0004c791`. Parti 2–40 immutate; nuove appendici dal 41: 41 con 78.974 identità. Non si presume la futura disponibilità dei vecchi percorsi locali; occorre recuperare gli allegati pubblicati dalla libreria.

## Riconciliazione QCL e storico

Confrontate 4.154 coppie dimensionali candidate, corrispondenti a 4.154 serie QCL distinte, con periodi, numeri, testo originale, flag, note, campi originali e provenienza. Sono 204.701 periodi comuni, 14.637 differenze numeriche, 8.131 differenze di flag e 184.235 record uguali in tutti i campi originali comuni.

I confronti rigorosi di schema sono separati dalle differenze di contenuto, così come le differenze di presenza del campo Note dalle differenze testuali delle note. Le uguaglianze di codici non provano duplicati, le differenze di schema non provano fenomeni nuovi, e l'assenza di candidati esatti non equivale ad armonizzazione semantica fra schemi differenti.

Per 201 serie QCL tutti i record hanno già un corrispondente nei campi originali comuni; per 73 serie la coincidenza riguarda anche l'intero schema originale. Anche queste serie sono conservate nella pubblicazione QCL distinta, non dichiarate novità statistiche. I conteggi cumulativi riguardano record e identità per dataset, non osservazioni semanticamente deduplicate fra fonti.

QCL conservato integralmente come pubblicazione distinta della produzione agricola e zootecnica. I contenuti coincidenti con gli input dei dataset storici sono dichiarati sovrapposizioni, non fenomeni o serie semanticamente nuovi. Nessuna eliminazione basata sui soli codici, fusione o sostituzione retroattiva; conteggi riferiti a record e identità per dataset. I rapporti per coppia, le coperture esclusive, i campioni e la provenienza sono nell'audit. Lo storico non viene sostituito o modificato retroattivamente.

## QA nuova e storica

Tutti i campi CSV sono confrontati con lo staging e tutte le celle DATI nuove sono rilette ricostruendo i record originali. Il testo numerico è esatto, i numeri Excel sono confrontati con tolleranza assoluta e relativa 1e-14, senza riscalamento.

Verificati integralmente dizionari, appendici, riepiloghi, cache formule, SHA256, byte, CRC, stili e layout di 253 workbook e 1015 fogli. Le banche degli stili e l'intero styles.xml canonico coincidono con il modello 21 nuovamente recuperato; layout: margine A, titolo alla riga 2, intestazioni alla riga 3, dati dalla riga 4, D4 e griglia nascosta. Restano 16 colonne comuni e tutti i campi originali non già rappresentati.

La QA storica integrale è ereditata salvo il confronto mirato dei candidati, con ambito di scansione/ricostruzione esplicito. Le anteprime sono campionate e non una verifica visiva di tutte le celle; non si dichiara una nuova rilettura integrale dei DATI storici.

## Cumulativo e risorse residue

Lotti 1–22: 49.539.397 osservazioni, 3.734.766 identità per dataset, 5.635 Excel dati e 45.584.919 valori numerici. Registro in 41 parti; FAOSTAT 60/69, residue EA, FBS, FBSH, FDIQ, GLE, SCL, TCL, TI, TM.

FDIQ resta da acquisire con mappatura dedicata allo schema per indagini, senza inventare geografie o annualità: non è un'esclusione definitiva. Gli altri sette portali, data.europa.eu, UNdata, World Bank, OECD, Eurostat, IMF e WHO/GHO, non sono riverificati nel lotto 22; la raccolta integrale degli otto portali non è dichiarata conclusa.
