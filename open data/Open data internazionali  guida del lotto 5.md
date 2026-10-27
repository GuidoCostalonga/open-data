# Open data internazionali: lotto 5

Questo lotto aggiunge dati effettivi, non soltanto collegamenti, senza modificare o ripubblicare i precedenti Excel dati. La raccolta dei portali rimane parziale: nessun catalogo è equiparato all'acquisizione completa.

## Contenuto

- **Dataset nuovi:** 3.
- **Osservazioni nuove:** 1,957,425; valori numerici: 766,961.
- **Excel dati:** 77; paesi/economie/territori: 48; aggregati: 3.
- **Registro cumulativo:** 380,532 serie; 91,076 nuove. Nessuna intersezione delle nuove identità con quelle dei lotti precedenti.
- **Controlli:** confronto di ogni cella delle tabelle dati con il CSV normalizzato, valori numerici, record, SHA256, CRC degli archivi e immutabilità di 1182 precedenti Excel.
- **Dimensione:** ogni file Excel e ZIP inferiore a 29.000.000 byte.

## Uso del registro e dei file

Il registro cumulativo completo è ripartito in 4 file Excel, per rispettare il limite anche con la crescita delle serie. La prima parte è il foglio REGISTRO_SERIE dell'indice; le altre parti sono file Registro-cumulativo separati. Consultare REGISTRI nell'indice per l'elenco completo. La ripetizione delle sole identità nei registri cumulativi è intenzionale; le osservazioni già consegnate non sono replicate.

Gli ZIP contengono i dati e questa guida, non l'indice o le altre parti del registro: scaricare questi separatamente. Le parti di uno stesso paese possono trovarsi in ZIP diversi; il foglio FILE dell'indice indica tutti gli abbinamenti. Ogni tabella dati conserva le colonne comuni B:Q e, da R, gli ulteriori campi originali della fonte.

## Avvertenze

Tutti i periodi contenuti nelle risorse scaricate sono inclusi senza filtro temporale. Per FAOSTAT le righe del catalogo possono differire da quelle effettivamente presenti nello ZIP: il foglio DATASET_LOTTO e le righe DIZ_DATASET riportano l'acquisito; il catalogo non è usato per inventare o colmare osservazioni. Le anomalie di conteggio sono elencate in CONFRONTO_CATALOGO.

Il valore numerico non viene riscalato, neppure per percentuali o UNIT_MULT OCSE. Il testo del numero e i flag restano originali. Le celle mancanti restano vuote; non vengono stimate. Non sommare componenti e totali, rilevazioni diverse o aggregati sovrapposti. Aggregati, livelli rurale/urbano e raggruppamenti statistici non sono automaticamente regioni amministrative. I codici territoriali storici non sono armonizzati retroattivamente.

## Provenienza

- **OECD DSD_EAG_LSO_EA@DF_LSO_NEAC_DISTR_EA:** Adults' educational attainment distribution, by age group and gender; 966,852 righe, periodi 1981–2025. URL: https://sdmx.oecd.org/public/rest/data/OECD.EDU.IMEP,DSD_EAG_LSO_EA@DF_LSO_NEAC_DISTR_EA,1.0/all?dimensionAtObservation=AllDimensions&format=csvfilewithlabels
- **OECD DSD_EAG_LSO_EA@DF_LSO_NEAC_DISTR_GENDER:** Adults' gender distribution, by educational attainment level and age group; 954,294 righe, periodi 1981–2025. URL: https://sdmx.oecd.org/public/rest/data/OECD.EDU.IMEP,DSD_EAG_LSO_EA@DF_LSO_NEAC_DISTR_GENDER,1.0/all?dimensionAtObservation=AllDimensions&format=csvfilewithlabels
- **OECD DSD_EAG_UOE_NON_FIN_PERS@DF_UOE_NF_PERS_RAW_INST2:** Number of teacher aides; 36,279 righe, periodi 2013–2024. URL: https://sdmx.oecd.org/public/rest/data/OECD.EDU.IMEP,DSD_EAG_UOE_NON_FIN_PERS@DF_UOE_NF_PERS_RAW_INST2,1.1/all?dimensionAtObservation=AllDimensions&format=csvfilewithlabels
