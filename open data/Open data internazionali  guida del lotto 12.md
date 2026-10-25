# Open data internazionali: lotto 12

Questo lotto aggiunge dati effettivi, non soltanto collegamenti, senza modificare o ripubblicare i precedenti Excel dati. La raccolta dei portali rimane parziale: nessun catalogo è equiparato all'acquisizione completa.

## Contenuto

- **Dataset nuovi:** 2.
- **Osservazioni nuove:** 2,143,812; valori numerici: 2,143,812.
- **Excel dati:** 235; paesi/economie/territori: 201; aggregati: 34.
- **Registro cumulativo:** 891,910 serie; 185,330 nuove. Nessuna intersezione delle nuove identità con quelle dei lotti precedenti.
- **Controlli:** confronto di ogni cella delle tabelle dati con il CSV normalizzato, valori numerici, record, SHA256, CRC degli archivi e immutabilità di 2674 precedenti Excel.
- **Dimensione:** ogni file Excel e ZIP inferiore a 29.000.000 byte.

## Uso del registro e dei file

Il registro cumulativo completo è ripartito in 9 file Excel, per rispettare il limite anche con la crescita delle serie. La prima parte è il foglio REGISTRO_SERIE dell'indice; le altre parti sono file Registro-cumulativo separati. Consultare REGISTRI nell'indice per l'elenco completo. La ripetizione delle sole identità nei registri cumulativi è intenzionale; le osservazioni già consegnate non sono replicate.

Gli ZIP contengono i dati e questa guida, non l'indice o le altre parti del registro: scaricare questi separatamente. Le parti di uno stesso paese possono trovarsi in ZIP diversi; il foglio FILE dell'indice indica tutti gli abbinamenti. Ogni tabella dati conserva le colonne comuni B:Q e, da R, gli ulteriori campi originali della fonte.

## Avvertenze

Tutti i periodi contenuti nelle risorse scaricate sono inclusi senza filtro temporale. Per FAOSTAT le righe del catalogo possono differire da quelle effettivamente presenti nello ZIP: il foglio DATASET_LOTTO e le righe DIZ_DATASET riportano l'acquisito; il catalogo non è usato per inventare o colmare osservazioni. Le anomalie di conteggio sono elencate in CONFRONTO_CATALOGO.

Il valore numerico non viene riscalato, neppure per percentuali o UNIT_MULT OCSE. Il testo del numero e i flag restano originali. Le soglie pubblicate con < o > sono conservate come testo in H; G resta vuota, senza trasformare un limite in valore puntuale. Le celle mancanti restano vuote; non vengono stimate. Non sommare componenti e totali, rilevazioni diverse o aggregati sovrapposti. Aggregati, livelli rurale/urbano e raggruppamenti statistici non sono automaticamente regioni amministrative. I codici territoriali storici non sono armonizzati retroattivamente.

La popolazione OA, se presente nel lotto, comprende stime e proiezioni pubblicate dall'editore, riconoscibili dai nomi e dai flag originali: periodi futuri non sono dati osservati. Gli intervalli pluriennali sono mantenuti esattamente come pubblicati, senza creare annualità aggiuntive.

## Provenienza

QI comprende indici lordi e pro capite con base 2014-2016 = 100: non sono quantità fisiche o percentuali di crescita. Unit è vuoto nella fonte; la base è nella denominazione Element originale. HS è un archivio storico cessato: periodi e intervalli sono estratti letteralmente dalla denominazione Survey e confrontati con il codice, che resta conservato integralmente. Medie, mediane, deviazioni standard, numerosità e valute locali restano distinte, senza conversioni monetarie. Il confronto esatto delle dimensioni codificate e unità tra database FAOSTAT non rileva candidati; non è un confronto semantico tra codifiche diverse.

- **FAOSTAT HS:** Discontinued archives and data series: Indicators from Household Surveys (gender, area, socioeconomics); 148,620 righe, periodi 1992-1993–2009. URL: https://bulks-faostat.fao.org/production/Indicators_from_Household_Surveys_E_All_Data_(Normalized).zip
- **FAOSTAT QI:** Production: Production Indices; 1,995,192 righe, periodi 1961–2024. URL: https://bulks-faostat.fao.org/production/Production_Indices_E_All_Data_(Normalized).zip
