# Open data internazionali: guida al lotto 31

Il lotto acquisisce integralmente FAOSTAT TM, “Trade: Detailed trade matrix”, dal [file ufficiale normalizzato](https://bulks-faostat.fao.org/production/Trade_DetailedTradeMatrix_E_All_Data_(Normalized).zip). Il [catalogo ufficiale](https://bulks-faostat.fao.org/production/datasets_E.json) e i nuovi dati sono stati recuperati soltanto dopo il completamento del controllo preventivo degli allegati e dell’intero registro.

## Acquisizione e cumulativo

| Misura | Lotto 31 | Cumulativo lotti 1–31 |
|---|---:|---:|
| Righe / osservazioni contabili | 52.410.630 | 179.277.683 |
| Identità di serie per dataset | 6.640.547 | 16.374.947 |
| Excel dati | 1160 | 9256 |
| Valori numerici | 52.410.630 | 175.054.696 |

Le annualità effettive sono 1986–2024, con 195 dichiaranti originali. Il numero di dichiaranti e il numero di ZIP non sono automaticamente conteggi di paesi.

- **Valori**: 0 righe non numeriche conservate senza imputare zeri e 6.461.758 zeri effettivi conservati.
- **Flag**: A: 51.748.350; X: 140.150; E: 336.136; I: 185.994. Stime, imputazioni e proiezioni conservano i flag della fonte e non diventano automaticamente osservazioni.
- **Confezionamento**: 290 ZIP dati (paesi-e-territori: 289; aree-non-classificate: 1), 67 nuove appendici e sei supporti, per 363 allegati complessivi.

## Recupero preventivo

Sono stati nuovamente recuperati dalla libreria tutti i 107 allegati pubblicati del lotto 30. Per ciascuno sono stati confrontati byte e SHA256 con ricevuta e manifest pubblicati; per i 91 ZIP dati sono stati verificati anche CRC e hash dei 360 Excel interni.

I file originali delle 104 parti del registro sono stati recuperati e tutti gli 11 campi riletti. Conteggi, impronte dei campi decodificati e identità sono coerenti con gli audit pubblicati: 9.734.400 identità uniche, 126.867.053 righe e 122.644.066 numerici.

La parte 1 nel foglio REGISTRO_SERIE dell’indice31 è XML byte-identico all’indice30 appena recuperato. Le parti 2–104 restano gli originali pubblicati, invariati; le nuove appendici sono 105–171, per 171 parti complessive.

Le celle DATI storiche non sono state integralmente rilette nel lotto31. La relativa QA contenutistica resta ereditata e distinta dai nuovi controlli su manifest, hash, CRC, registro e modello; anche il CRC dei sette ZIP di continuità del lotto14 resta ereditato, mentre le singole parti originali del registro sono state nuovamente recuperate e verificate.

Eventuali eliminazioni di cache di lavoro derivate sono documentate con byte e SHA256 nei relativi verbali. Non sono modificati gli originali pubblicati e nessun vecchio file locale viene usato come prova del nuovo recupero.

## Fedeltà e ruoli bilaterali

Sono conservati tutti i 16 campi originali nelle 16 colonne comuni e nelle 10 colonne aggiuntive. Il valore numerico è separato dal testo originale; unità, codici, denominazioni, note presenti, flag, provenienza e tutte le annualità restano fedeli alla fonte, senza conversioni, imputazioni o aggregazioni aggiuntive.

Le prime due colonne comuni identificano il dichiarante originale. Tutti i partner, con codici, M49 e denominazioni originali, rimangono nelle colonne aggiuntive e nel foglio TERRITORI, con ruolo distinto; i ruoli non vengono scambiati e importazioni ed esportazioni non sono trasformate in saldi.

La classificazione di archivio distingue paesi/territori, aggregati statistici e dichiaranti non classificati. Le classificazioni ereditate sono utilizzate soltanto per corrispondenze esatte di codice originale e denominazione col manifest24 recuperato nella catena degli audit, senza inferenze amministrative sui dichiaranti o sui partner.

L’identità SHA256 è qualificata per dataset e JSON canonico di tutti i campi Code tranne Year Code, più Unit. Il confronto con tutte le 9.734.400 identità e chiavi dimensionali complete delle 104 parti ha trovato 0 intersezioni di identità, 0 coppie candidate dimensionali e 0 ripetizioni serie-periodo.

Non sono presenti candidati con la stessa chiave dimensionale completa. Questo non esclude sovrapposizioni concettuali fra schemi differenti e non costituisce un’armonizzazione semantica o una verifica di unicità dei fenomeni fra dataset.

L’ordine relativo originale delle righe entro ciascun dichiarante è conservato. Lo staging viene riletto integralmente confrontando le impronte di tutti i campi originali e verificando l’unicità serie-periodo senza presumere contiguità delle serie.

La codifica dei membri è utf-8. Decodifica stretta e ricodifica restituiscono gli stessi SHA256 dei byte originali, senza caratteri sostitutivi; i dizionari originali sono consegnati integralmente, comprese eventuali ripetizioni e tabelle con sole intestazioni.

## Catalogo e copertura

Il confronto diretto col catalogo del lotto30 risulta byte-identico ed è dettagliato in catalog_comparison.json. Per TM il catalogo indica 52.410.630 righe e il CSV ne contiene 52.410.630, con differenza 0; nessun conteggio già consegnato viene alterato retroattivamente.

La continuità col checkpoint19 del 25 ottobre 2026 è ereditata dalla catena degli audit recuperati e non viene presentata come un nuovo confronto diretto col file19. FAOSTAT raggiunge tutte le 69 risorse del catalogo verificato, senza risorse residue in quel catalogo.

Gli altri sette portali, data.europa.eu, UNdata, World Bank, OECD, Eurostat, IMF e WHO/GHO, non sono stati riverificati nel lotto31. La loro copertura rimane ereditata e non viene dichiarata completa.

## Formato, QA e riproduzione

Ogni Excel e ZIP è strettamente inferiore a 29.000.000 byte. Restano margine A, titolo riga2, intestazioni riga3, dati dalla riga4, blocco D4, griglia nascosta, larghezze e stili del modello pubblicato.

La QA rilegge tutte le 1.362.676.380 nuove celle DATI dagli Excel realmente contenuti negli ZIP e confronta i campi originali, dizionari, registro e riepiloghi. CRC, SHA256, stili e layout sono verificati; le formule dello stato cumulativo sono ricalcolate e le cache controllate, lasciando invariate le righe dei lotti precedenti e degli altri sette portali.

Le anteprime PIL sono viewport campionati delle celle e degli stili nativi, non schermate Office o revisione visiva integrale. Le larghezze storiche possono troncare contenuti nel viewport, mentre le celle complete sono verificate automaticamente.

L’audit contiene manifest, prove e codice, con dipendenze verso gli audit30,29,28,27 identificati da UUID, byte e SHA256 e recuperati nuovamente. Per riprodurre il lavoro occorre recuperarli dalla libreria, senza presumere vecchi file locali; la fonte ZIP non è duplicata nell’audit, ma URL, byte, hash e impronte dei campi sono conservati e tutti i dati acquisiti sono negli Excel allegati.

La ricevuta finale elenca gli hash degli altri allegati e i relativi identificativi effettivi dopo la pubblicazione. Il proprio identificativo e hash vengono verificati separatamente per evitare ricorsioni; il manifest preparato prima dell’ultima pubblicazione non viene impropriamente dichiarato come prova autonoma della pubblicazione completa.
