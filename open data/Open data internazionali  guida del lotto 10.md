# Open data internazionali: lotto 10

Questo lotto aggiunge dati effettivi, non soltanto collegamenti, senza modificare o ripubblicare i precedenti Excel dati. La raccolta dei portali rimane parziale: nessun catalogo è equiparato all'acquisizione completa.

## Contenuto

- **Dataset nuovi:** 9.
- **Osservazioni nuove:** 1,754,457; valori numerici: 1,697,238.
- **Excel dati:** 325; paesi/economie/territori: 251; aggregati: 74.
- **Registro cumulativo:** 613,382 serie; 142,703 nuove. Nessuna intersezione delle nuove identità con quelle dei lotti precedenti.
- **Controlli:** confronto di ogni cella delle tabelle dati con il CSV normalizzato, valori numerici, record, SHA256, CRC degli archivi e immutabilità di 2062 precedenti Excel.
- **Dimensione:** ogni file Excel e ZIP inferiore a 29.000.000 byte.

## Uso del registro e dei file

Il registro cumulativo completo è ripartito in 7 file Excel, per rispettare il limite anche con la crescita delle serie. La prima parte è il foglio REGISTRO_SERIE dell'indice; le altre parti sono file Registro-cumulativo separati. Consultare REGISTRI nell'indice per l'elenco completo. La ripetizione delle sole identità nei registri cumulativi è intenzionale; le osservazioni già consegnate non sono replicate.

Gli ZIP contengono i dati e questa guida, non l'indice o le altre parti del registro: scaricare questi separatamente. Le parti di uno stesso paese possono trovarsi in ZIP diversi; il foglio FILE dell'indice indica tutti gli abbinamenti. Ogni tabella dati conserva le colonne comuni B:Q e, da R, gli ulteriori campi originali della fonte.

## Avvertenze

Tutti i periodi contenuti nelle risorse scaricate sono inclusi senza filtro temporale. Per FAOSTAT le righe del catalogo possono differire da quelle effettivamente presenti nello ZIP: il foglio DATASET_LOTTO e le righe DIZ_DATASET riportano l'acquisito; il catalogo non è usato per inventare o colmare osservazioni. Le anomalie di conteggio sono elencate in CONFRONTO_CATALOGO.

Il valore numerico non viene riscalato, neppure per percentuali o UNIT_MULT OCSE. Il testo del numero e i flag restano originali. Le soglie pubblicate con < o > sono conservate come testo in H; G resta vuota, senza trasformare un limite in valore puntuale. Le celle mancanti restano vuote; non vengono stimate. Non sommare componenti e totali, rilevazioni diverse o aggregati sovrapposti. Aggregati, livelli rurale/urbano e raggruppamenti statistici non sono automaticamente regioni amministrative. I codici territoriali storici non sono armonizzati retroattivamente.

La popolazione OA, se presente nel lotto, comprende stime e proiezioni pubblicate dall'editore, riconoscibili dai nomi e dai flag originali: periodi futuri non sono dati osservati. Gli intervalli pluriennali sono mantenuti esattamente come pubblicati, senza creare annualità aggiuntive.

## Provenienza

- **FAOSTAT FS:** Food Security and Nutrition: Suite of Food Security Indicators; 287,735 righe, periodi 2000–2025. URL: https://bulks-faostat.fao.org/production/Food_Security_Data_E_All_Data_(Normalized).zip
- **FAOSTAT GI:** Climate Change: Agrifood systems emissions: Emissions from Fires; 428,347 righe, periodi 1990–2024. URL: https://bulks-faostat.fao.org/production/Emissions_Land_Use_Fires_E_All_Data_(Normalized).zip
- **FAOSTAT OA:** Population and Employment: Annual population; 168,405 righe, periodi 1950–2100. URL: https://bulks-faostat.fao.org/production/Population_E_All_Data_(Normalized).zip
- **FAOSTAT OEA:** Population and Employment: Employment Indicators: Agriculture and agrifood systems; 256,389 righe, periodi 1947–2025. URL: https://bulks-faostat.fao.org/production/Employment_Indicators_Agriculture_E_All_Data_(Normalized).zip
- **FAOSTAT OER:** Population and Employment: Employment Indicators: Rural; 113,187 righe, periodi 1952–2025. URL: https://bulks-faostat.fao.org/production/Employment_Indicators_Rural_E_All_Data_(Normalized).zip
- **FAOSTAT RLIS:** Rural Livelihoods: Rural Livelihoods Indicators; 38,918 righe, periodi 2004–2022. URL: https://bulks-faostat.fao.org/production/Rural_Livelihoods_Indicators_E_All_Data_(Normalized).zip
- **FAOSTAT RM:** Discontinued archives and data series: Machinery; 146,834 righe, periodi 1961–2009. URL: https://bulks-faostat.fao.org/production/Investment_Machinery_E_All_Data_(Normalized).zip
- **FAOSTAT RT:** Land, Inputs and Sustainability: Pesticides Trade; 198,348 righe, periodi 1961–2024. URL: https://bulks-faostat.fao.org/production/Inputs_Pesticides_Trade_E_All_Data_(Normalized).zip
- **FAOSTAT TCLI:** Trade: Crops and livestock products indicators; 116,294 righe, periodi 2010–2024. URL: https://bulks-faostat.fao.org/production/Trade_CropsLivestockIndicators_E_All_Data_(Normalized).zip
