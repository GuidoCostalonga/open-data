# Open data internazionali: guida al lotto 23

Il lotto 23 acquisisce integralmente [FAOSTAT FBS, Food Balances: Food Balances (2010-)](https://bulks-faostat.fao.org/production/FoodBalanceSheets_E_All_Data_(Normalized).zip). Sono conservati 4.820.497 record, 4.820.497 valori numerici, 0 righe non numeriche e 373.670 identità per dataset; i conteggi non sono una deduplicazione semantica fra pubblicazioni.

## Fonte e valori

Gli estremi temporali sono 2010–2023, con aggiornamento fonte 2025-10-28T00:00:00, secondo il [pacchetto ufficiale FBS](https://bulks-faostat.fao.org/production/FoodBalanceSheets_E_All_Data_(Normalized).zip). Tutti i campi originali sono ricostruibili dagli Excel, comprese unità, testo numerico originale, codici, flag, note e provenienza.

Nessuna conversione monetaria o di unità, aggregazione o armonizzazione semantica non dimostrata. Mancanti e testo non numerico non diventano zeri; gli zeri effettivi sono conservati. Stime e proiezioni mantengono i flag e non diventano automaticamente dati osservati.

I flag originali sono E su 2.618.688 righe, I su 2.198.908 e X su 2.901. Il [dizionario originale nel pacchetto FAOSTAT](https://bulks-faostat.fao.org/production/FoodBalanceSheets_E_All_Data_(Normalized).zip) definisce rispettivamente “Estimated value”, “Value imputed by a receiving agency” e “Figure from external organization”; queste qualificazioni sono conservate, senza nuove imputazioni e senza classificare automaticamente X come osservato.

Il [catalogo ufficiale FAOSTAT](https://bulks-faostat.fao.org/production/datasets_E.json) dichiara 5.878.736 righe; il CSV ne contiene 4.820.497, scostamento -1.058.239. Il confronto corrente rileva 69 risorse, 0 aggiunte, 0 rimozioni e 0 modifiche rispetto al catalogo pubblicato nel lotto 22, senza modificare retroattivamente conteggi consegnati.

Il catalogo del checkpoint del 25 ottobre 2026 è nuovamente letto dall'audit pubblicato del lotto 19. Coincidenza JSON con quello corrente: True; coincidenza byte per byte: True. SHA256 e provenienza sono documentati nell'audit.

Catalogo e ZIP FBS sono stati inoltre riscaricati integralmente con richieste no-cache e URL di verifica univoci: entrambe le risposte sono “Miss from cloudfront”, con byte e SHA256 identici ai primi download. È una riverifica della freschezza e dello scostamento catalogo/CSV, non una seconda acquisizione conteggiata.

## Allegati e continuità

Sono consegnati 213 Excel dati in 28 ZIP, per 179 paesi/territori anche storici e 34 aggregati statistici. Gli ZIP sono contenitori, non conteggi di paesi. Le classificazioni e i codici archivistici sono ereditati dal lotto 22 per corrispondenza esatta del nome originale, con evidenze esplicite; i codici M49 della fonte sono conservati senza convertirli in ISO3 o inferire regioni amministrative.

Ogni Excel e ZIP consegnato è strettamente inferiore a 29.000.000 byte. Il pacchetto ZIP ufficiale supera il limite e non è duplicato negli allegati: audit con URL, SHA256, byte, metadati, HTTP e dizionari originali; tutti i dati sono negli Excel.

Prima di scaricare FBS sono stati nuovamente recuperati e verificati tutti i 30 allegati pubblicati del lotto 22. Ventotto sono confrontati con hash e byte dell'audit; l'audit è verificato contro la ricevuta, confrontata in tutte le 29 righe, senza hash autoriferito. Verificati i CRC dei 23 ZIP e hash/byte di tutti i 249 Excel dati, non una nuova rilettura delle loro celle.

Tutte le 41 parti del registro sono rilette e ricostruite dai file pubblicati: 3.734.766 identità uniche, 49.539.397 osservazioni e 45.584.919 numerici. Le identità FAOSTAT sono ricalcolate dalle chiavi originali; compressione interna reversibile verificata per record, senza presumere validi i vecchi database locali.

Parte 1 copiata nell'indice 23 con XML identico byte per byte all'indice 22, SHA256 `b0512f0d7688578e2f3a55cd39f51ed2af1d1950ba4a24069e487dfa0004c791`. Parti 2–41 immutate; appendici nuove dal 42: 42 con 100.000 identità, 43 con 100.000 identità, 44 con 100.000 identità, 45 con 73.670 identità. Tutti i file storici originali restano intatti. I file di lavoro nuovi sono in un'area temporanea in memoria per non cancellare dati precedenti; la futura continuità richiede sempre nuovo recupero dalla libreria.

## Confronto e QA

Confronto con tutte le 41 parti del registro: 0 intersezioni di identità e 0 coppie con dimensioni codificate e unità esatte. Non equivale a un'armonizzazione semantica fra schemi differenti; conteggi per pubblicazione, non fenomeni nuovi. Le ripetizioni serie-periodo interne sono 0. Non si eliminano dati soltanto per corrispondenza di codici; coperture e identità per dataset non provano novità statistica.

Tutti i campi CSV sono confrontati con lo staging e tutte le celle DATI nuove sono rilette dai membri effettivi degli ZIP consegnati, ricostruendo ogni record originale. Testo numerico esatto, confronto numerico Excel con tolleranza assoluta e relativa 1e-14, senza riscalamento.

Verificati integralmente dizionari, appendici, riepiloghi, cache delle formule, SHA256, byte, CRC, stili e layout di 220 workbook e 874 fogli. L'intero styles.xml canonico coincide con il modello del lotto 22 nuovamente recuperato; margine A, titolo riga 2, intestazioni riga 3, dati da riga 4, D4 e griglia nascosta. Restano 16 colonne comuni e tutti i campi originali non già rappresentati.

La QA storica integrale dei DATI è ereditata, non nuovamente eseguita. Le anteprime sono campionate, non una verifica visiva di tutte le celle; le precedenti riconciliazioni QCL e FO sono ereditate e distinguibili dai nuovi controlli.

## Cumulativo e residui

Lotti 1–23: 54.359.894 osservazioni, 4.108.436 identità per dataset, 5.848 Excel dati e 50.405.416 valori numerici. Registro in 45 parti; FAOSTAT 61/69, otto residue: EA, FBSH, FDIQ, GLE, SCL, TCL, TI, TM.

FDIQ resta da acquisire con mappatura dedicata allo schema per indagini, senza inventare geografie o annualità: non è un'esclusione definitiva. Gli altri sette portali, data.europa.eu, UNdata, World Bank, OECD, Eurostat, IMF e WHO/GHO, non sono riverificati nel lotto 23; copertura ereditata e progetto complessivo non dichiarato concluso.
