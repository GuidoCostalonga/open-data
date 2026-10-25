# Open data internazionali: lotto 9

Questo lotto aggiunge dati effettivi, non soltanto collegamenti, senza modificare o ripubblicare i precedenti Excel dati. La raccolta dei portali rimane parziale: nessun catalogo è equiparato all'acquisizione completa.

## Contenuto

- **Dataset nuovi:** 7.
- **Osservazioni nuove:** 2,435,165; valori numerici: 2,433,757.
- **Excel dati:** 289; paesi/economie/territori: 219; aggregati: 70.
- **Registro cumulativo:** 470,679 serie; 70,895 nuove. Nessuna intersezione delle nuove identità con quelle dei lotti precedenti.
- **Controlli:** confronto di ogni cella delle tabelle dati con il CSV normalizzato, valori numerici, record, SHA256, CRC degli archivi e immutabilità di 1773 precedenti Excel.
- **Dimensione:** ogni file Excel e ZIP inferiore a 29.000.000 byte.

## Uso del registro e dei file

Il registro cumulativo completo è ripartito in 5 file Excel, per rispettare il limite anche con la crescita delle serie. La prima parte è il foglio REGISTRO_SERIE dell'indice; le altre parti sono file Registro-cumulativo separati. Consultare REGISTRI nell'indice per l'elenco completo. La ripetizione delle sole identità nei registri cumulativi è intenzionale; le osservazioni già consegnate non sono replicate.

Gli ZIP contengono i dati e questa guida, non l'indice o le altre parti del registro: scaricare questi separatamente. Le parti di uno stesso paese possono trovarsi in ZIP diversi; il foglio FILE dell'indice indica tutti gli abbinamenti. Ogni tabella dati conserva le colonne comuni B:Q e, da R, gli ulteriori campi originali della fonte.

## Avvertenze

Tutti i periodi contenuti nelle risorse scaricate sono inclusi senza filtro temporale. Per FAOSTAT le righe del catalogo possono differire da quelle effettivamente presenti nello ZIP: il foglio DATASET_LOTTO e le righe DIZ_DATASET riportano l'acquisito; il catalogo non è usato per inventare o colmare osservazioni. Le anomalie di conteggio sono elencate in CONFRONTO_CATALOGO.

Il valore numerico non viene riscalato, neppure per percentuali o UNIT_MULT OCSE. Il testo del numero e i flag restano originali. Le celle mancanti restano vuote; non vengono stimate. Non sommare componenti e totali, rilevazioni diverse o aggregati sovrapposti. Aggregati, livelli rurale/urbano e raggruppamenti statistici non sono automaticamente regioni amministrative. I codici territoriali storici non sono armonizzati retroattivamente.

## Provenienza

- **FAOSTAT CB:** Food Balances: Commodity Balances (non-food) (2010-); 127,558 righe, periodi 2010–2023. URL: https://bulks-faostat.fao.org/production/CommodityBalances_(non-food)_(2010-)_E_All_Data_(Normalized).zip
- **FAOSTAT EI:** Climate Change: Agrifood systems emissions: Emissions intensities; 409,511 righe, periodi 1961–2023. URL: https://bulks-faostat.fao.org/production/Environment_Emissions_intensities_E_All_Data_(Normalized).zip
- **FAOSTAT EK:** Land, Inputs and Sustainability: Livestock Patterns; 470,577 righe, periodi 1961–2023. URL: https://bulks-faostat.fao.org/production/Environment_LivestockPatterns_E_All_Data_(Normalized).zip
- **FAOSTAT ESB:** Land, Inputs and Sustainability: Cropland Nutrient Balance; 827,796 righe, periodi 1961–2023. URL: https://bulks-faostat.fao.org/production/Environment_Cropland_nutrient_budget_E_All_Data_(Normalized).zip
- **FAOSTAT FA:** Discontinued archives and data series: Food Aid Shipments (WFP); 31,114 righe, periodi 1988–2016. URL: https://bulks-faostat.fao.org/production/Food_Aid_Shipments_WFP_E_All_Data_(Normalized).zip
- **FAOSTAT RFB:** Land, Inputs and Sustainability: Fertilizers by Product; 312,305 righe, periodi 2002–2024. URL: https://bulks-faostat.fao.org/production/Inputs_FertilizersProduct_E_All_Data_(Normalized).zip
- **FAOSTAT RFN:** Land, Inputs and Sustainability: Fertilizers by Nutrient; 256,304 righe, periodi 1961–2024. URL: https://bulks-faostat.fao.org/production/Inputs_FertilizersNutrient_E_All_Data_(Normalized).zip
