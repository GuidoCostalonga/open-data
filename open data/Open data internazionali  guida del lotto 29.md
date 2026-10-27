# Open data internazionali: guida al lotto 29

Il lotto acquisisce integralmente FAOSTAT TCL, “Trade: Crops and livestock products”, dal [file ufficiale normalizzato](https://bulks-faostat.fao.org/production/Trade_CropsLivestock_E_All_Data_(Normalized).zip). Sono conservate tutte le annualità e le aree originali; identità e conteggi per dataset non equivalgono a fenomeni semanticamente armonizzati.

## Contenuto e cumulativo

| Misura | Lotto 29 | Cumulativo lotti 1–29 |
|---|---:|---:|
| Righe / osservazioni contabili | 17.143.873 | 115.251.841 |
| Identità di serie per dataset | 485.098 | 8.753.520 |
| Excel dati | 484 | 7.736 |
| Valori numerici | 17.143.873 | 111.062.830 |

- **Copertura**: 1961–2024, 283 aree originali; non sono automaticamente altrettanti paesi.
- **Valori**: 0 righe non numeriche conservate senza imputare zeri e 3.856.231 zeri effettivi.
- **Flag**: X: 1.105.411; A: 11.949.993; E: 3.867.621; I: 220.848. Le qualificazioni originali restano distinte: stime e proiezioni non diventano automaticamente dati osservati.
- **Confezionamento**: 121 ZIP dati, 5 appendici (90–94) e sei supporti, per 132 allegati. Gli ZIP sono confezioni, non conteggi di paesi.

## Recupero preventivo e continuità

Prima della nuova fonte sono stati recuperati dalla libreria tutti i 102 allegati del lotto 28: byte e SHA256 verificati, CRC dei 93 ZIP dati e SHA256 dei 366 Excel interni confrontati con il manifest. Sono stati inoltre recuperati tutti i file originali delle 89 parti del registro, rileggendo tutti gli 11 campi e confrontando le relative impronte con gli audit pubblicati; 8.268.422 identità uniche, 98.107.968 righe e 93.918.957 numerici corrispondono al checkpoint.

La parte 1 resta nel foglio REGISTRO_SERIE dell’indice29, copiato byte per byte dall’indice28 nuovamente recuperato. Le parti 2–89 restano i file originali pubblicati e invariati; le nuove parti sono 90–94, per 94 parti complessive. Il piano di recupero nell’audit e l’indice elencano i riferimenti delle parti originali, senza presumere vecchi locali.

Le celle DATI storiche non sono state integralmente rilette nel lotto 29: la relativa QA contenutistica è ereditata, distinta dalle nuove verifiche di integrità, registro e modello. Tutte le celle DATI dei nuovi Excel sono state invece nuovamente rilette dagli Excel effettivamente contenuti negli ZIP.

L’ambiente nativo è stato ripristinato anche dopo la pubblicazione dei primi 111 ZIP. Lo stato è stato ricostruito dai 111 ack di pubblicazione, dai 444 record QA per-file e dai contatori persistiti, verificandone la coerenza e nuovamente lo SHA256 della fonte; i dati già consegnati non sono stati ripubblicati. La QA completa di quegli Excel era stata eseguita prima della loro pubblicazione e non viene presentata come una nuova rilettura dopo il ripristino; gli ultimi 40 Excel completano la stessa acquisizione, con QA integrale prima della pubblicazione. Evidenza in export_resume_after111_QA.json.

## Fedeltà alla fonte e confronto

Si conservano valore numerico e testo originale, unità anche vuote, tutti i codici e nomi, flag, note presenti e provenienza. I 14 campi originali sono rappresentati nelle 16 colonne comuni e nelle 8 aggiuntive; nessuna conversione monetaria o di unità, imputazione, aggregazione o saldo viene aggiunto dal progetto.

Importazioni ed esportazioni eventualmente presenti rimangono distinte per elemento originale. Non sono inventati partner assenti dallo schema e non sono scambiati ruoli originali; stime e altre qualificazioni della fonte mantengono i flag.

Il CSV TCL interlaccia aree e serie; una serie può ricomparire più avanti e non è considerata duplicata per questa ragione. Lo staging conserva l’ordine relativo originale per area e viene riletto integralmente per indicizzare le serie e verificare l’unicità serie-periodo, senza ordinare, aggregare o eliminare le righe DATI. Il primo tentativo di indicizzazione contigua è stato fermato prima di pubblicare o conteggiare dati; soltanto lo staging parziale nuovo è stato rilasciato e la ripartenza è documentata nell’audit.

Codifica verificata separatamente per ogni membro: utf-8. Ogni decodifica stretta seguita dalla ricodifica restituisce lo SHA256 dei byte originali; nessun carattere sostitutivo è stato usato.

I dizionari sono consegnati integralmente come forniti: Trade_CropsLivestock_E_AreaCodes.csv (283 righe); Trade_CropsLivestock_E_Elements.csv (10 righe); Trade_CropsLivestock_E_Flags.csv (4 righe); Trade_CropsLivestock_E_ItemCodes.csv (622 righe). Eventuali ripetizioni o dizionari con sole intestazioni restano tali, senza completamenti inventati; nomi e codici nei DATI rimangono comunque originali.

La chiave canonica comprende tutti i campi Code tranne Year Code, più Unit; l’identità è SHA256 di FAOSTAT|TCL|JSON canonico. Il confronto con tutte le 8.268.422 identità e chiavi dimensionali delle 89 parti recuperate rileva 0 intersezioni di identità, 4606 candidati dimensionali completi e 0 ripetizioni serie-periodo. Questo non dimostra un’armonizzazione semantica fra schemi diversi e non autorizza eliminazioni basate sui soli codici.

Tutte le 4.606 coppie candidate sono con CB. Sono stati recuperati nuovamente dalla libreria l’indice e gli otto ZIP originali del lotto9, verificando byte, SHA256, CRC e impronte di tutti i 289 Excel interni; sono state scansionate tutte le 127.558 righe DATI_CB e ricostruiti integralmente i record delle serie candidate, non gli altri DATI storici. Il confronto esaustivo trova 48.544 periodi comuni, 11.354 valori numerici diversi, 11.354 testi numerici diversi, 2.721 flag diversi e 1.413 note diverse; 159.334 record candidati sono in periodi presenti solo in TCL e 624 solo in CB. La provenienza è confrontata separatamente per URL e aggiornamento; evidenze per ogni coppia e campioni completi sono in reconciliation29.json.

historical_comparison.json conserva la rilevazione preliminare dei candidati, prima della riconciliazione. L’esito finale PASS è in historical_comparison_publication.json e reconciliation29.json; source_summary.json è passato a READY soltanto dopo il confronto dei contenuti.

TCL è conservato integralmente come pubblicazione del commercio distinta dal bilancio dei prodotti non alimentari CB. Le sovrapposizioni identiche (36.974 record originali completi) comprendono 233 serie TCL candidate interamente contenute nei record originali CB confrontati; URL e aggiornamento delle due pubblicazioni rimangono distinti. Anche queste serie sono dichiarate sovrapposizioni, non fenomeni semanticamente nuovi; conteggi e identità restano per dataset, nessuna fusione, sostituzione retroattiva o eliminazione su soli codici.

Paesi e territori, aggregati statistici e aree non classificate sono confezionati separatamente. Le classificazioni sono ereditate solo in caso di corrispondenza esatta di codice e nome con il manifest24 nuovamente recuperato nella catena degli audit; nessuna classificazione amministrativa viene inferita.

## Catalogo e copertura

Il nuovo confronto diretto del [catalogo ufficiale FAOSTAT](https://bulks-faostat.fao.org/production/datasets_E.json) è documentato in catalog_comparison.json rispetto al checkpoint28. La continuità con il checkpoint19 del 25 ottobre 2026 è ereditata dalla catena degli audit recuperati, non è dichiarata come nuovo confronto diretto con il file19; i conteggi già consegnati non vengono modificati retroattivamente.

Per TCL, il catalogo indica 17.143.873 righe; il CSV effettivo contiene 17.143.873, differenza 0. FAOSTAT passa a 67 risorse acquisite su 69 e restano SCL, TM; non sono esclusioni definitive.

Gli altri sette portali (data.europa.eu, UNdata, World Bank, OECD, Eurostat, IMF, WHO/GHO) non sono stati riverificati nel lotto 29. I relativi conteggi e la copertura rimangono esplicitamente ereditati.

## Formato, controlli e riproduzione

Ogni Excel e ZIP è strettamente inferiore a 29.000.000 byte. Restano margine A, titolo riga 2, intestazioni riga 3, dati riga 4, blocco D4, griglia nascosta e stili del modello pubblicato; nessuna riprogettazione di larghezze o stili.

L’audit conserva manifest e hash, prove di recupero, confronto catalogo, digest di tutti i campi originali, controlli fonte/staging e rilettura di tutte le nuove celle, dizionari, registro, stili, layout e formule ricalcolate con cache verificate. Le anteprime PIL sono viewport campionati ricostruiti dalle celle e dagli stili, non schermate Office né controllo visivo integrale; i contenuti lunghi possono essere troncati nel viewport dalle larghezze storiche, mentre le celle complete sono verificate.

Gli audit28 e27, nuovamente recuperati e verificati, non sono duplicati nel nuovo ZIP per il limite dimensionale: sono riferiti con identificativi, byte e SHA256. La riproduzione richiede recuperarli nuovamente dalla libreria; da audit27 provengono le dipendenze storiche dei sorgenti e da audit28 i manifest e le impronte del checkpoint. L’archivio ufficiale della nuova fonte è escluso dall’audit; URL, byte e SHA256 sono conservati e tutti i dati acquisiti sono distribuiti negli Excel.

La ricevuta elenca gli hash di tutti gli altri allegati, compreso l’audit, e viene emessa dopo la loro effettiva pubblicazione con i relativi identificativi. Il proprio identificativo e hash sono verificati separatamente dopo la pubblicazione, evitando ricorsioni crittografiche.
