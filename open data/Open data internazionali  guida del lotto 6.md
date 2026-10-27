# Open data internazionali: lotto 6

Questo lotto aggiunge dati effettivi, non soltanto collegamenti, senza modificare o ripubblicare i precedenti Excel dati. La raccolta dei portali rimane parziale: nessun catalogo è equiparato all'acquisizione completa.

## Contenuto

- **Dataset nuovi:** 14.
- **Osservazioni nuove:** 73,126; valori numerici: 73,126.
- **Excel dati:** 294; paesi/economie/territori: 256; aggregati: 38.
- **Registro cumulativo:** 396,734 serie; 16,202 nuove. Nessuna intersezione delle nuove identità con quelle dei lotti precedenti.
- **Controlli:** confronto di ogni cella delle tabelle dati con il CSV normalizzato, valori numerici, record, SHA256, CRC degli archivi e immutabilità di 1259 precedenti Excel.
- **Dimensione:** ogni file Excel e ZIP inferiore a 29.000.000 byte.

## Uso del registro e dei file

Il registro cumulativo completo è ripartito in 4 file Excel, per rispettare il limite anche con la crescita delle serie. La prima parte è il foglio REGISTRO_SERIE dell'indice; le altre parti sono file Registro-cumulativo separati. Consultare REGISTRI nell'indice per l'elenco completo. La ripetizione delle sole identità nei registri cumulativi è intenzionale; le osservazioni già consegnate non sono replicate.

Gli ZIP contengono i dati e questa guida, non l'indice o le altre parti del registro: scaricare questi separatamente. Le parti di uno stesso paese possono trovarsi in ZIP diversi; il foglio FILE dell'indice indica tutti gli abbinamenti. Ogni tabella dati conserva le colonne comuni B:Q e, da R, gli ulteriori campi originali della fonte.

## Avvertenze

Tutti i periodi contenuti nelle risorse scaricate sono inclusi senza filtro temporale. Per FAOSTAT le righe del catalogo possono differire da quelle effettivamente presenti nello ZIP: il foglio DATASET_LOTTO e le righe DIZ_DATASET riportano l'acquisito; il catalogo non è usato per inventare o colmare osservazioni. Le anomalie di conteggio sono elencate in CONFRONTO_CATALOGO.

Il valore numerico non viene riscalato, neppure per percentuali o UNIT_MULT OCSE. Il testo del numero e i flag restano originali. Le celle mancanti restano vuote; non vengono stimate. Non sommare componenti e totali, rilevazioni diverse o aggregati sovrapposti. Aggregati, livelli rurale/urbano e raggruppamenti statistici non sono automaticamente regioni amministrative. I codici territoriali storici non sono armonizzati retroattivamente.

## Provenienza

- **UNSD_SYB SYB_1:** Population, density and surface area; 7,727 righe, periodi 2010–2025. URL: https://data.un.org/_Docs/SYB/CSV/SYB68_1_202511_Population, Surface Area and Density.csv
- **UNSD_SYB SYB_327:** International migrants and refugees; 6,966 righe, periodi 2005–2024. URL: https://data.un.org/_Docs/SYB/CSV/SYB68_327_202511_International Migrants and Refugees.csv
- **UNSD_SYB SYB_246:** Population growth and indicators of fertility and mortality; 7,161 righe, periodi 2010–2025. URL: https://data.un.org/_Docs/SYB/CSV/SYB68_246_202511_Population Growth, Fertility and Mortality Indicators.csv
- **UNSD_SYB SYB_253:** Population and rates of growth in urban areas and capital cities; 4,165 righe, periodi 2001–2018. URL: https://data.un.org/_Docs/SYB/CSV/SYB61_253_Population Growth Rates in Urban areas and Capital cities.csv
- **UNSD_SYB SYB_309:** Enrollment in primary, lower secondary and upper secondary education levels; 7,934 righe, periodi 2000–2023. URL: https://data.un.org/_Docs/SYB/CSV/SYB68_309_202511_Education.csv
- **UNSD_SYB SYB_323:** Teaching staff at the primary, lower secondary and upper secondary levels; 3,685 righe, periodi 2000–2024. URL: https://data.un.org/_Docs/SYB/CSV/SYB68_323_202511_Teaching Staff in education.csv
- **UNSD_SYB SYB_263:** Production, trade and supply of energy; 8,700 righe, periodi 1995–2022. URL: https://data.un.org/_Docs/SYB/CSV/SYB68_263_202511_Production, Trade and Supply of Energy.csv
- **UNSD_SYB SYB_328:** Intentional homicides and other crimes; 6,046 righe, periodi 2000–2023. URL: https://data.un.org/_Docs/SYB/CSV/SYB68_328_202511_Intentional homicides and other crimes.csv
- **UNSD_SYB SYB_317:** Proportion of seats held by women in national parliament; 1,952 righe, periodi 2000–2025. URL: https://data.un.org/_Docs/SYB/CSV/SYB68_317_202511_Seats held by women in Parliament.csv
- **UNSD_SYB SYB_319:** Ratio of girls to boys in primary, lower secondary and upper secondary education; 3,347 righe, periodi 1995–2023. URL: https://data.un.org/_Docs/SYB/CSV/SYB68_319_202511_Ratio of girls to boys in education.csv
- **UNSD_SYB SYB_310:** CO2 emission estimates; 3,488 righe, periodi 1975–2022. URL: https://data.un.org/_Docs/SYB/CSV/SYB68_310_202511_Carbon Dioxide Emission Estimates.csv
- **UNSD_SYB SYB_315:** Water supply and sanitation services; 3,519 righe, periodi 2008–2024. URL: https://data.un.org/_Docs/SYB/CSV/SYB68_315_202511_Water and Sanitation Services.csv
- **UNSD_SYB SYB_313:** Threatened species; 6,916 righe, periodi 2004–2024. URL: https://data.un.org/_Docs/SYB/CSV/SYB68_313_202511_Threatened Species.csv
- **UNSD_SYB SYB_314:** Internet Usage; 1,520 righe, periodi 2005–2023. URL: https://data.un.org/_Docs/SYB/CSV/SYB68_314_202511_Internet Usage.csv
