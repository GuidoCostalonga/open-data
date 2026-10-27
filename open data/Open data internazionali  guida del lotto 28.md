# Open data internazionali: guida al lotto 28

Il lotto acquisisce integralmente FAOSTAT FBSH, “Food Balances: Food Balances (-2013, old methodology and population)”, dal [file ufficiale normalizzato](https://bulks-faostat.fao.org/production/FoodBalanceSheetsHistoric_E_All_Data_(Normalized).zip). La vecchia metodologia e popolazione restano esplicitamente distinte dalle altre risorse. Il registro prosegue dalla parte 87 senza modificare le 86 parti precedenti; identità per dataset e dimensioni originali non equivalgono a fenomeni semanticamente armonizzati.

## Contenuto e cumulativo

| Misura | Lotto 28 | Cumulativo lotti 1–28 |
|---|---:|---:|
| Righe / osservazioni in senso contabile | 11.479.903 | 98.107.968 |
| Identità di serie per dataset | 238.418 | 8.268.422 |
| Excel dati | 366 | 7252 |
| Valori numerici | 11.479.903 | 93.918.957 |

- **Copertura FBSH**: annualità 1961–2013, 217 aree originali, 0 righe non numeriche e 3.682.298 zeri effettivi conservati.
- **Flag**: X: 8339; E: 7.073.159; I: 4.398.405. Il dizionario originale è consegnato; stime e altre qualificazioni della fonte non diventano automaticamente dati osservati.
- **Confezionamento**: 93 ZIP dati, 3 appendici del registro (87–89) e sei allegati di supporto, per 102 allegati. I numeri degli ZIP non sono numeri di paesi.

## Recupero preventivo e controlli distinti

Prima di scaricare FBSH sono stati nuovamente recuperati e verificati tutti i 94 allegati del lotto 27, a partire da ricevuta e audit: byte e SHA256, CRC degli 85 ZIP dati e SHA256 dei 335 Excel interni. Tutti gli 11 campi delle 86 parti del registro sono stati riletti e confrontati con le impronte dei campi già pubblicate; sono state nuovamente verificate 8.030.004 identità uniche e i conteggi di registro di 86.628.065 righe e 82.439.054 valori numerici.

Le celle DATI storiche non sono state integralmente rilette nel lotto 28. La QA contenutistica storica è esplicitamente ereditata; i nuovi controlli riguardano integrità, manifest, registro e modello recuperati, mentre tutti i dati FBSH prodotti sono nuovamente riletti cella per cella dagli Excel realmente contenuti negli ZIP.

## Fedeltà alla fonte

Si conservano valore numerico e testo originale, unità anche vuote, tutti i codici ed etichette, flag e provenienza. Tutte le 13 colonne originali sono rappresentate nelle 16 colonne comuni e nelle sette colonne originali aggiuntive, senza conversioni, saldi o aggregazioni aggiuntive.

Prodotti ed elementi dei bilanci alimentari restano distinti per tutti i codici e le etichette originali. Le misure già calcolate dalla fonte restano tali; il progetto non calcola saldi, aggregazioni o conversioni aggiuntive e non inventa partner assenti dallo schema.

Il CSV storico normalizzato e alcuni dizionari non sono UTF-8. Una decodifica stretta Latin-1 conserva tutti i caratteri presenti ed è equivalente a Windows-1252 per i byte effettivamente contenuti in tali file; la ri-codifica restituisce lo stesso SHA256 dei byte originali. Gli altri membri usano la codifica verificata individualmente. Non sono stati usati caratteri sostitutivi; le prove per ciascun membro sono in source_encoding_check.json.

La fonte FBSH contiene tre dizionari originali: AreaCodes, Flags e ItemCodes; non fornisce un file Elements separato. ItemCodes contiene soltanto le intestazioni originali “Item Code”, “CPC Code”, “Item”, senza righe dati: il foglio rimane vuoto, non viene popolato artificialmente e il suo CPC Code non sostituisce la colonna Item Code (FBS) dei DATI. Le ripetizioni presenti in AreaCodes sono conservate. Codici e nomi di prodotti ed elementi restano integralmente presenti nei dati originali consegnati.

Le classificazioni territoriali sono ereditate solo in caso di corrispondenza esatta di codice originale e nome con il manifest24 nuovamente recuperato nella catena degli audit. Aggregati statistici e paesi restano distinti; gli altri casi sono esplicitamente non classificati, senza inferire regioni amministrative.

## Identità e continuità

La chiave canonica comprende tutti i campi Code tranne Year Code, più Unit; l’identità è SHA256 di FAOSTAT|FBSH|JSON canonico. Il confronto ha usato tutte le 8.030.004 identità e chiavi dimensionali storiche recuperate: 0 intersezioni di identità, 199.080 candidati di chiave dimensionale completa e 0 ripetizioni serie-periodo. Le eventuali riconciliazioni di contenuto sono documentate nell’audit prima dell’inclusione.

Questo non dimostra equivalenza o distinzione semantica fra schemi diversi. Nessuna riga viene eliminata sulla base di una sola corrispondenza di codici; eventuali confronti futuri devono considerare anche periodi, valori, flag e provenienza.

Tutte le 199.080 coppie sono state riconciliate con FBS. Il file FBS ora scaricato, 54.840.802 byte con SHA256 26200855ed5da3d0805e34219124e241d0e0bc6959d0995ebc77a10dd84cbaf1, coincide con la fonte consegnata nel lotto 23: sono state nuovamente lette tutte le sue 4.820.497 righe CSV, senza dichiarare una nuova rilettura dei vecchi Excel DATI.

Sulle coppie candidate risultano 786.005 punti serie-periodo sovrapposti, 277.689 con valore numerico identico e 179.302 con tutti i 13 campi comuni identici. I punti FBSH non presenti in FBS sono 8.889.769; 0 serie FBSH candidate hanno tutti i propri punti contenuti e identici nei campi comuni di FBS. La colonna Note di FBS, assente in FBSH, non viene inventata nella fonte storica.

La decisione è conservare integralmente FBSH con la qualificazione esplicita “old methodology and population” e la distinta provenienza. Le sovrapposizioni identiche non vengono cancellate né presentate come nuovi fenomeni armonizzati: cumulativi e identità restano conteggi per dataset. Il CSV nell’audit documenta ogni coppia, periodi comuni/esclusivi, uguaglianze di valori numerici e testo, flag, etichette e tutti i campi comuni.

La parte 1 è nel foglio REGISTRO_SERIE dell’indice28, copiato byte per byte dall’indice27. Le parti 2–86 restano i file originali pubblicati e invariati; le nuove appendici sono le parti 87–89. L’indice elenca tutti i puntamenti; l’audit contiene l’intero piano di recupero e gli identificativi effettivi.

## Catalogo e risorse residue

Il nuovo confronto diretto del [catalogo ufficiale FAOSTAT](https://bulks-faostat.fao.org/production/datasets_E.json) lo trova byte-identico al checkpoint del lotto 27. La continuità con il checkpoint del lotto 19 del 25 ottobre 2026 è ereditata dalla catena documentata negli audit precedenti recuperati, non presentata come un nuovo confronto diretto con un file del lotto19. Mantiene 69 risorse; per FBSH indica 11.479.903 righe, rispetto a 11.479.903 righe effettive nel CSV, differenza 0.

La copertura FAOSTAT passa a 66 risorse acquisite su 69. Restano SCL, TCL e TM; non sono esclusioni definitive e non sono conteggiate come acquisite.

I portali data.europa.eu, UNdata, World Bank, OECD, Eurostat, IMF e WHO/GHO non sono stati riverificati nel lotto 28. I relativi conteggi sono ereditati e nessun conteggio già consegnato viene alterato retroattivamente.

## Formato e audit

Ogni Excel e ZIP è strettamente inferiore a 29.000.000 byte. Restano margine A, titolo alla riga 2, intestazioni alla riga 3, dati dalla riga 4, blocco D4, griglia nascosta e stili del modello pubblicato.

L’audit comprende manifest, SHA256, controlli del recupero preventivo, confronto con il catalogo, digest dei 13 campi originali, controlli fonte/staging, confronto di tutte le celle nuove, dizionari, registro, formule e codice riproducibile. Le anteprime sono ricostruzioni PIL di viewport campionati da celle e stili nativi, non schermate Office né una rilettura visiva integrale.

Per rispettare il limite, l’audit27 verificato non viene duplicato nel nuovo ZIP: restano registrati identificativo libreria, byte e SHA256 e l’originale pubblicato non viene modificato. La riproduzione del codice recupera da quell’audit le dipendenze storiche; il nuovo audit conserva le prove complete dei controlli effettuati nel lotto28 e l’evidenza per tutte le coppie candidate.

Lo ZIP ufficiale FBSH è escluso dall’audit perché da solo supera il limite degli allegati; URL, dimensione e SHA256 sono documentati. I dati contenuti sono integralmente distribuiti negli Excel dei ZIP consegnati.

La ricevuta SHA256 elenca tutti gli allegati eccetto sé stessa, inclusa l’impronta dell’audit. La propria impronta è verificata separatamente dopo la pubblicazione, evitando un riferimento crittografico ricorsivo.
