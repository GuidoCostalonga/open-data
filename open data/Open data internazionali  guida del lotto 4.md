# Open data internazionali: lotto 4

Questo lotto aggiunge dati effettivi, non soltanto collegamenti, senza modificare o ripubblicare i precedenti Excel dati. La raccolta dei portali rimane parziale: nessun catalogo è equiparato all'acquisizione completa.

## Contenuto

- **Dataset nuovi:** 12.
- **Osservazioni nuove:** 1,845,766; valori numerici: 1,713,368.
- **Excel dati:** 301; paesi/economie/territori: 263; aggregati: 38.
- **Registro cumulativo:** 289,456 serie; 93,206 nuove. Nessuna intersezione delle nuove identità con quelle dei lotti precedenti.
- **Controlli:** confronto di ogni cella delle tabelle dati con il CSV normalizzato, valori numerici, record, SHA256, CRC degli archivi e immutabilità di 881 precedenti Excel.
- **Dimensione:** ogni file Excel e ZIP inferiore a 29.000.000 byte.

## Uso del registro e dei file

Il registro cumulativo completo è ripartito in 3 file Excel, per rispettare il limite anche con la crescita delle serie. La prima parte è il foglio REGISTRO_SERIE dell'indice; le altre parti sono file Registro-cumulativo separati. Consultare REGISTRI nell'indice per l'elenco completo. La ripetizione delle sole identità nei registri cumulativi è intenzionale; le osservazioni già consegnate non sono replicate.

Gli ZIP contengono i dati e questa guida, non l'indice o le altre parti del registro: scaricare questi separatamente. Le parti di uno stesso paese possono trovarsi in ZIP diversi; il foglio FILE dell'indice indica tutti gli abbinamenti. Ogni tabella dati conserva le colonne comuni B:Q e, da R, gli ulteriori campi originali della fonte.

## Avvertenze

Tutti i periodi contenuti nelle risorse scaricate sono inclusi senza filtro temporale. Per FAOSTAT le righe del catalogo possono differire da quelle effettivamente presenti nello ZIP: il foglio DATASET_LOTTO e le righe DIZ_DATASET riportano l'acquisito; il catalogo non è usato per inventare o colmare osservazioni. Le anomalie di conteggio sono elencate in CONFRONTO_CATALOGO.

Il valore numerico non viene riscalato, neppure per percentuali o UNIT_MULT OCSE. Il testo del numero e i flag restano originali. Le celle mancanti restano vuote; non vengono stimate. Non sommare componenti e totali, rilevazioni diverse o aggregati sovrapposti. Aggregati, livelli rurale/urbano e raggruppamenti statistici non sono automaticamente regioni amministrative. I codici territoriali storici non sono armonizzati retroattivamente.

## Provenienza

- **FAOSTAT AF:** Agricultural Science and Technology: ASTI - Researchers; 3,800 righe, periodi 2004–2023. URL: https://bulks-faostat.fao.org/production/ASTI_Researchers_E_All_Data_(Normalized).zip
- **FAOSTAT BE:** Land, Inputs and Sustainability: Bioenergy; 128,457 righe, periodi 1990–2024. URL: https://bulks-faostat.fao.org/production/Environment_Bioenergy_E_All_Data_(Normalized).zip
- **FAOSTAT ET:** Land, Inputs and Sustainability: Temperature change on land; 590,512 righe, periodi 1961–2025. URL: https://bulks-faostat.fao.org/production/Environment_Temperature_change_E_All_Data_(Normalized).zip
- **FAOSTAT FOP:** Forestry: Pulp and paper capacities, survey; 79,270 righe, periodi 2020–2027. URL: https://bulks-faostat.fao.org/production/Forestry_Pulp_Paper_Survey_E_All_Data_(Normalized).zip
- **FAOSTAT GF:** Climate Change: Agrifood systems emissions: Emissions from Forests; 65,633 righe, periodi 1990–2025. URL: https://bulks-faostat.fao.org/production/Emissions_Land_Use_Forests_E_All_Data_(Normalized).zip
- **FAOSTAT GN:** Climate Change: Agrifood systems emissions: Emissions from Energy use in agriculture; 120,740 righe, periodi 1990–2023. URL: https://bulks-faostat.fao.org/production/Emissions_Agriculture_Energy_E_All_Data_(Normalized).zip
- **FAOSTAT GV:** Climate Change: Agrifood systems emissions: Emissions from Drained organic soils; 87,484 righe, periodi 1990–2024. URL: https://bulks-faostat.fao.org/production/Emissions_Drained_Organic_Soils_E_All_Data_(Normalized).zip
- **FAOSTAT LC:** Land, Inputs and Sustainability: Land Cover; 213,582 righe, periodi 1992–2024. URL: https://bulks-faostat.fao.org/production/Environment_LandCover_E_All_Data_(Normalized).zip
- **FAOSTAT MDDW:** Food and Diet: Diversity (MDD-W, Minimum Dietary Diversity for Women); 1,223 righe, periodi 1996–2024. URL: https://bulks-faostat.fao.org/production/Minimum_Dietary_Diversity_for_Women_(MDD-W)_Food_and_Diet_E_All_Data_(Normalized).zip
- **FAOSTAT RL:** Land, Inputs and Sustainability: Land Use; 421,850 righe, periodi 1961–2025. URL: https://bulks-faostat.fao.org/production/Inputs_LandUse_E_All_Data_(Normalized).zip
- **FAOSTAT RP:** Land, Inputs and Sustainability: Pesticides Use; 104,650 righe, periodi 1990–2024. URL: https://bulks-faostat.fao.org/production/Inputs_Pesticides_Use_E_All_Data_(Normalized).zip
- **FAOSTAT WCAD:** World Census of Agriculture: Structural data from agricultural censuses; 28,565 righe, periodi 1927–2023. URL: https://bulks-faostat.fao.org/production/World_Census_Agriculture_E_All_Data_(Normalized).zip
