# Open data internazionali: lotto 8

Questo lotto aggiunge dati effettivi, non soltanto collegamenti, senza modificare o ripubblicare i precedenti Excel dati. La raccolta dei portali rimane parziale: nessun catalogo è equiparato all'acquisizione completa.

## Contenuto

- **Dataset nuovi:** 3.
- **Osservazioni nuove:** 97,868; valori numerici: 31,364.
- **Excel dati:** 219; paesi/economie/territori: 218; aggregati: 1.
- **Registro cumulativo:** 399,784 serie; 2,726 nuove. Nessuna intersezione delle nuove identità con quelle dei lotti precedenti.
- **Controlli:** confronto di ogni cella delle tabelle dati con il CSV normalizzato, valori numerici, record, SHA256, CRC degli archivi e immutabilità di 1554 precedenti Excel.
- **Dimensione:** ogni file Excel e ZIP inferiore a 29.000.000 byte.

## Uso del registro e dei file

Il registro cumulativo completo è ripartito in 4 file Excel, per rispettare il limite anche con la crescita delle serie. La prima parte è il foglio REGISTRO_SERIE dell'indice; le altre parti sono file Registro-cumulativo separati. Consultare REGISTRI nell'indice per l'elenco completo. La ripetizione delle sole identità nei registri cumulativi è intenzionale; le osservazioni già consegnate non sono replicate.

Gli ZIP contengono i dati e questa guida, non l'indice o le altre parti del registro: scaricare questi separatamente. Le parti di uno stesso paese possono trovarsi in ZIP diversi; il foglio FILE dell'indice indica tutti gli abbinamenti. Ogni tabella dati conserva le colonne comuni B:Q e, da R, gli ulteriori campi originali della fonte.

## Avvertenze

Tutti i periodi contenuti nelle risorse scaricate sono inclusi senza filtro temporale. Per FAOSTAT le righe del catalogo possono differire da quelle effettivamente presenti nello ZIP: il foglio DATASET_LOTTO e le righe DIZ_DATASET riportano l'acquisito; il catalogo non è usato per inventare o colmare osservazioni. Le anomalie di conteggio sono elencate in CONFRONTO_CATALOGO.

Il valore numerico non viene riscalato, neppure per percentuali o UNIT_MULT OCSE. Il testo del numero e i flag restano originali. Le celle mancanti restano vuote; non vengono stimate. Non sommare componenti e totali, rilevazioni diverse o aggregati sovrapposti. Aggregati, livelli rurale/urbano e raggruppamenti statistici non sono automaticamente regioni amministrative. I codici territoriali storici non sono armonizzati retroattivamente.

## Provenienza

- **IMF_CLIMATE 7cae02f84ed547fbbd6210d90da19879:** Climate-driven INFORM Risk; 7,520 righe, periodi 2013–2022. URL: https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Indicator_11_3_Physical_Risks__Index_for_Risk_Management/FeatureServer/0/query?f=json&where=1%3D1&outFields=*&returnGeometry=false
- **IMF_CLIMATE 9c3764c0efcc4c71934ab3988f219e0e:** Atmospheric CO₂ Concentrations; 1,608 righe, periodi 1958M03–2025M08. URL: https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Indicator_3_2_Climate_Indicators_Monthly_Atmospheric_Carbon_Dioxide_concentrations/FeatureServer/0/query?f=json&where=1%3D1&outFields=*&returnGeometry=false
- **IMF_CLIMATE b13b69ee0dde43a99c811f592af4e821:** Climate-related Disasters Frequency; 88,740 righe, periodi 1980–2024. URL: https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Indicator_11_1_Physical_Risks_Climate_related_disasters_frequency/FeatureServer/0/query?f=json&where=1%3D1&outFields=*&returnGeometry=false
