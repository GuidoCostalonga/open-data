# Open data internazionali: lotto 11

Questo lotto aggiunge dati effettivi, non soltanto collegamenti, senza modificare o ripubblicare i precedenti Excel dati. La raccolta dei portali rimane parziale: nessun catalogo è equiparato all'acquisizione completa.

## Contenuto

- **Dataset nuovi:** 3.
- **Osservazioni nuove:** 1,943,725; valori numerici: 1,943,725.
- **Excel dati:** 287; paesi/economie/territori: 249; aggregati: 38.
- **Registro cumulativo:** 706,580 serie; 93,198 nuove. Nessuna intersezione delle nuove identità con quelle dei lotti precedenti.
- **Controlli:** confronto di ogni cella delle tabelle dati con il CSV normalizzato, valori numerici, record, SHA256, CRC degli archivi e immutabilità di 2387 precedenti Excel.
- **Dimensione:** ogni file Excel e ZIP inferiore a 29.000.000 byte.

## Uso del registro e dei file

Il registro cumulativo completo è ripartito in 8 file Excel, per rispettare il limite anche con la crescita delle serie. La prima parte è il foglio REGISTRO_SERIE dell'indice; le altre parti sono file Registro-cumulativo separati. Consultare REGISTRI nell'indice per l'elenco completo. La ripetizione delle sole identità nei registri cumulativi è intenzionale; le osservazioni già consegnate non sono replicate.

Gli ZIP contengono i dati e questa guida, non l'indice o le altre parti del registro: scaricare questi separatamente. Le parti di uno stesso paese possono trovarsi in ZIP diversi; il foglio FILE dell'indice indica tutti gli abbinamenti. Ogni tabella dati conserva le colonne comuni B:Q e, da R, gli ulteriori campi originali della fonte.

## Avvertenze

Tutti i periodi contenuti nelle risorse scaricate sono inclusi senza filtro temporale. Per FAOSTAT le righe del catalogo possono differire da quelle effettivamente presenti nello ZIP: il foglio DATASET_LOTTO e le righe DIZ_DATASET riportano l'acquisito; il catalogo non è usato per inventare o colmare osservazioni. Le anomalie di conteggio sono elencate in CONFRONTO_CATALOGO.

Il valore numerico non viene riscalato, neppure per percentuali o UNIT_MULT OCSE. Il testo del numero e i flag restano originali. Le soglie pubblicate con < o > sono conservate come testo in H; G resta vuota, senza trasformare un limite in valore puntuale. Le celle mancanti restano vuote; non vengono stimate. Non sommare componenti e totali, rilevazioni diverse o aggregati sovrapposti. Aggregati, livelli rurale/urbano e raggruppamenti statistici non sono automaticamente regioni amministrative. I codici territoriali storici non sono armonizzati retroattivamente.

La popolazione OA, se presente nel lotto, comprende stime e proiezioni pubblicate dall'editore, riconoscibili dai nomi e dai flag originali: periodi futuri non sono dati osservati. Gli intervalli pluriennali sono mantenuti esattamente come pubblicati, senza creare annualità aggiuntive.

## Provenienza

Le emissioni sono stime o indicatori dell'editore; CO2eq, gas, metodologie e unità restano separati. SUA descrive disponibilità alimentare, non consumo individuale effettivo. Il controllo aggiuntivo di identiche dimensioni codificate e unità tra database non rileva candidati; non equivale a un confronto semantico tra codifiche diverse.

- **FAOSTAT EM:** Climate Change: Agrifood systems emissions: Emissions indicators; 678,370 righe, periodi 1990–2023. URL: https://bulks-faostat.fao.org/production/Climate_change_Emissions_indicators_E_All_Data_(Normalized).zip
- **FAOSTAT GPP:** Climate Change: Agrifood systems emissions: Emissions from pre and post agricultural production; 522,216 righe, periodi 1990–2023. URL: https://bulks-faostat.fao.org/production/Emissions_Pre_Post_Production_E_All_Data_(Normalized).zip
- **FAOSTAT SUA:** Food and Diet: Availability (based on supply utilization accounts); 743,139 righe, periodi 2010–2023. URL: https://bulks-faostat.fao.org/production/Supply_Utilization_Accounts_Food_and_Diet_E_All_Data_(Normalized).zip
