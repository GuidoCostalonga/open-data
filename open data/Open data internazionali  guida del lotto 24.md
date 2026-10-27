# Open data internazionali: guida al lotto 24

Il lotto 24 acquisisce integralmente [FAOSTAT GLE, Climate Change: Agrifood systems emissions: Emissions from Livestock](https://bulks-faostat.fao.org/production/Emissions_livestock_E_All_Data_(Normalized).zip). Sono conservati 6.650.421 record, 6.650.421 valori numerici, 0 righe non numeriche e 116.190 identità per dataset; i conteggi non sono una deduplicazione semantica fra pubblicazioni.

## Fonte e valori

Gli estremi temporali sono 1961–2050, con aggiornamento fonte 2025-10-28T00:00:00, secondo il [pacchetto ufficiale GLE](https://bulks-faostat.fao.org/production/Emissions_livestock_E_All_Data_(Normalized).zip). Tutti i campi originali sono ricostruibili dagli Excel, comprese unità, testo numerico originale, codici, flag, note e provenienza.

Le annualità storiche della fonte sono 1961–2023; sono inoltre conservati 106.235 record di proiezione per il 2030 e altrettanti per il 2050, tutti con flag F. L'estremo 2050 non indica una copertura annuale continua fino a quella data: nessuna annualità intermedia assente viene inventata e le proiezioni non sono presentate come osservazioni.

I codici fonte 3050 (FAO TIER 1, 6.565.094 record) e 3051 (UNFCCC, 85.327 record) rimangono distinti nella chiave dimensionale e nelle colonne originali. I nomi e i codici sono mantenuti come pubblicati, senza mescolare le provenienze o dedurre equivalenza dei contenuti.

Nessuna conversione monetaria o di unità, aggregazione o armonizzazione semantica non dimostrata. Mancanti e testo non numerico non diventano zeri; gli zeri effettivi sono conservati. Stime e proiezioni mantengono i flag e non diventano automaticamente dati osservati.

I flag originali e i rispettivi conteggi sono A: 111.450 righe, «Official figure»; E: 6.311.649 righe, «Estimated value»; F: 212.470 righe, «Forecast value»; I: 4.140 righe, «Value imputed by a receiving agency»; X: 10.712 righe, «Figure from external organization», secondo il [dizionario originale nel pacchetto FAOSTAT](https://bulks-faostat.fao.org/production/Emissions_livestock_E_All_Data_(Normalized).zip). Le qualificazioni della fonte sono conservate senza nuove imputazioni e senza classificare automaticamente valori numerici, stime o proiezioni come osservati.

Nel solo lotto 24 è corretta una classificazione archivistica ereditata: “Sub-Saharan Africa”, codice FAOSTAT 420 e codice M49 originale '202, è collocata fra gli aggregati statistici, non fra i paesi. La [tabella ufficiale UNSD M49](https://unstats.un.org/unsd/methodology/m49/overview/) riporta 202 come Sub-region Code e Sub-Saharan Africa come Sub-region Name: non si inferisce un livello amministrativo. Risultano 211 geografie archiviate come paesi/territori e 39 aggregati statistici. Nessun dato, codice, valore, flag, annualità o identità cambia; il foglio DATI di questo file rimane identico byte per byte. File e conteggi storici non sono modificati retroattivamente.

Il [catalogo ufficiale FAOSTAT](https://bulks-faostat.fao.org/production/datasets_E.json) dichiara 6.941.916 righe; il CSV ne contiene 6.650.421, scostamento -291.495. Il confronto corrente rileva 69 risorse, 0 aggiunte, 0 rimozioni e 0 modifiche rispetto al catalogo pubblicato nel lotto 23, senza modificare retroattivamente conteggi consegnati.

Il catalogo del checkpoint del 25 ottobre 2026 è riletto dalla copia conservata nell'audit del lotto 23 appena recuperato. Coincidenza byte per byte con quello corrente: True. SHA256 e provenienza sono documentati nell'audit.

Il catalogo corrente è richiesto con URL di verifica univoco e intestazioni no-cache. La fonte GLE è acquisita integralmente soltanto dopo il controllo preventivo del recupero; URL, HTTP, byte, SHA256 e CRC sono conservati nell'audit.

Una seconda lettura integrale dello ZIP fonte, trasmessa direttamente al calcolo SHA256 senza conservarne una copia aggiuntiva, conferma gli stessi byte con una nuova richiesta no-cache. È una sola riverifica dello scostamento catalogo/CSV, non una nuova acquisizione conteggiata.

## Allegati e continuità

Sono consegnati 250 Excel dati in 38 ZIP, per 211 paesi/territori anche storici e 39 aggregati statistici. Gli ZIP sono contenitori, non conteggi di paesi. Classificazioni e codici archivistici riportano le singole evidenze, ricavate da nomi esatti già pubblicati o da codici ISO3 espliciti nei dizionari. I codici geografici originali, inclusi gli M49 se presenti, restano conservati senza convertirli fra schemi o usarli per inferire regioni amministrative.

Ogni Excel e ZIP consegnato è strettamente inferiore a 29.000.000 byte. Il pacchetto ZIP ufficiale supera il limite e non è duplicato negli allegati: audit con URL, SHA256, byte, metadati, HTTP e dizionari originali; tutti i dati sono negli Excel.

Prima di scaricare GLE sono stati nuovamente recuperati e verificati tutti i 38 allegati pubblicati del lotto 23. Trentasei sono confrontati con hash e byte dell'audit; l'audit è verificato contro la ricevuta, confrontata in tutte le 37 righe, senza hash autoriferito. Verificati i CRC dei 28 ZIP e hash/byte di tutti i 213 Excel dati, non una nuova rilettura delle loro celle.

Tutte le 45 parti del registro sono rilette e ricostruite dai file pubblicati: 4.108.436 identità uniche, 54.359.894 osservazioni e 50.405.416 numerici. Tutti gli undici campi originali sono riletti e verificati; le identità FAOSTAT sono ricalcolate dalle chiavi originali. È stato costruito un nuovo indice compatto con identità binarie reversibili, hash dimensionali e localizzatori esatti di parte e riga nei file pubblicati verificati, senza presumere validi i vecchi database locali o scartare i contenuti originali. Dopo il confronto di tutte le 116.190 identità nuove, concluso senza candidati, il solo indice temporaneo nuovo è stato rilasciato per liberare spazio: prova e SHA256 sono nell'audit, mentre tutti i file originali verificati rimangono conservati.

Parte 1 copiata nell'indice 24 con XML identico byte per byte all'indice 23, SHA256 `b0512f0d7688578e2f3a55cd39f51ed2af1d1950ba4a24069e487dfa0004c791`. Parti 2–45 immutate; appendici nuove dal 46: 46 con 100.000 identità, 47 con 16.190 identità. Tutti i file storici originali restano intatti. I file di lavoro nuovi sono in un'area temporanea in memoria per non cancellare dati precedenti; la futura continuità richiede sempre nuovo recupero dalla libreria.

## Confronto e QA

Confronto con tutte le 45 parti del registro: 0 intersezioni di identità e 0 coppie con dimensioni codificate e unità esatte. Non equivale a un'armonizzazione semantica fra schemi differenti; conteggi per pubblicazione, non fenomeni nuovi. Le ripetizioni serie-periodo interne sono 0. Non si eliminano dati soltanto per corrispondenza di codici; coperture e identità per dataset non provano novità statistica.

Tutti i campi CSV sono confrontati con lo staging e tutte le celle DATI nuove sono rilette dai membri effettivi degli ZIP consegnati, ricostruendo ogni record originale. Testo numerico esatto, confronto numerico Excel con tolleranza assoluta e relativa 1e-14, senza riscalamento.

Verificati integralmente dizionari, appendici, riepiloghi, cache delle formule, SHA256, byte, CRC, stili e layout di 255 workbook e 1021 fogli. L'intero styles.xml canonico coincide con il modello del lotto 23 nuovamente recuperato; margine A, titolo riga 2, intestazioni riga 3, dati da riga 4, D4 e griglia nascosta. Restano 16 colonne comuni e tutti i campi originali non già rappresentati.

La QA storica integrale dei DATI è ereditata, non nuovamente eseguita. Le anteprime sono campionate, non una verifica visiva di tutte le celle; le precedenti riconciliazioni QCL e FO sono ereditate e distinguibili dai nuovi controlli.

## Cumulativo e residui

Lotti 1–24: 61.010.315 osservazioni, 4.224.626 identità per dataset, 6.098 Excel dati e 57.055.837 valori numerici. Registro in 47 parti; FAOSTAT 62/69, sette residue: EA, FBSH, FDIQ, SCL, TCL, TI, TM.

FDIQ resta da acquisire con mappatura dedicata allo schema per indagini, senza inventare geografie o annualità: non è un'esclusione definitiva. Gli altri sette portali, data.europa.eu, UNdata, World Bank, OECD, Eurostat, IMF e WHO/GHO, non sono riverificati nel lotto 24; copertura ereditata e progetto complessivo non dichiarato concluso.
