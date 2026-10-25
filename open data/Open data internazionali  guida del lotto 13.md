# Open data internazionali: lotto 13

Questo lotto aggiunge dati effettivi, non soltanto collegamenti, senza modificare o ripubblicare i precedenti Excel dati. La raccolta dei portali rimane parziale: nessun catalogo è equiparato all'acquisizione completa.

## Contenuto

- **Dataset nuovi:** 3.
- **Osservazioni nuove:** 1,184,439; valori numerici: 1,183,561.
- **Excel dati:** 243; paesi/economie/territori: 190; aggregati: 40.
- **Registro cumulativo:** 2,062,358 serie; 1,170,448 nuove. Nessuna intersezione delle nuove identità con quelle dei lotti precedenti.
- **Controlli:** confronto di ogni cella delle tabelle dati con il CSV normalizzato, valori numerici, record, SHA256, CRC degli archivi e immutabilità di 2909 precedenti Excel.
- **Dimensione:** ogni file Excel e ZIP inferiore a 29.000.000 byte.

## Uso del registro e dei file

Il registro cumulativo completo è ripartito in 21 file Excel, per rispettare il limite anche con la crescita delle serie. La prima parte è il foglio REGISTRO_SERIE dell'indice; le altre parti sono file Registro-cumulativo separati. Consultare REGISTRI nell'indice per l'elenco completo. La ripetizione delle sole identità nei registri cumulativi è intenzionale; le osservazioni già consegnate non sono replicate.

Gli ZIP contengono i dati e questa guida, non l'indice o le altre parti del registro: scaricare questi separatamente. Le parti di uno stesso paese possono trovarsi in ZIP diversi; il foglio FILE dell'indice indica tutti gli abbinamenti. Ogni tabella dati conserva le colonne comuni B:Q e, da R, gli ulteriori campi originali della fonte.

## Avvertenze

Tutti i periodi contenuti nelle risorse scaricate sono inclusi senza filtro temporale. Per FAOSTAT le righe del catalogo possono differire da quelle effettivamente presenti nello ZIP: il foglio DATASET_LOTTO e le righe DIZ_DATASET riportano l'acquisito; il catalogo non è usato per inventare o colmare osservazioni. Le anomalie di conteggio sono elencate in CONFRONTO_CATALOGO.

Il valore numerico non viene riscalato, neppure per percentuali o UNIT_MULT OCSE. Il testo del numero e i flag restano originali. Le soglie pubblicate con < o > sono conservate come testo in H; G resta vuota, senza trasformare un limite in valore puntuale. Le celle mancanti restano vuote; non vengono stimate. Non sommare componenti e totali, rilevazioni diverse o aggregati sovrapposti. Aggregati, livelli rurale/urbano e raggruppamenti statistici non sono automaticamente regioni amministrative. I codici territoriali storici non sono armonizzati retroattivamente.

La popolazione OA, se presente nel lotto, comprende stime e proiezioni pubblicate dall'editore, riconoscibili dai nomi e dai flag originali: periodi futuri non sono dati osservati. Gli intervalli pluriennali sono mantenuti esattamente come pubblicati, senza creare annualità aggiuntive.

## Provenienza

HCES contiene stime di consumo/apporto apparente da indagini sui consumi e sulle spese delle famiglie, non assunzioni individuali misurate direttamente. Survey Code, anno Survey, Geographic Level, Food Group, Indicator, Element e Note restano originali. DISAGG_HCES elenca i livelli presenti in ogni file: nazionale, urbano/rurale e quintili non sono regioni amministrative; altre suddivisioni territoriali sono conservate senza certificazione automatica della natura amministrativa o armonizzazione storica. CAHD mantiene distinti costi, prevalenze, numerosità, valute locali, Int$ PPP e Release. AE mantiene distinti indicatori, categorie di costo, istituzioni, valute, PPP e prezzi costanti della fonte; nessuna conversione propria. Il confronto esatto aggiuntivo delle dimensioni codificate e unità FAOSTAT non rileva candidati, senza equivalere a un controllo semantico fra codifiche differenti.

- **FAOSTAT AE:** Agricultural Science and Technology: ASTI - Expenditures; 7,789 righe, periodi 2004–2023. URL: https://bulks-faostat.fao.org/production/ASTI_Expenditures_E_All_Data_(Normalized).zip
- **FAOSTAT CAHD:** Cost and Affordability of a Healthy Diet: Cost and Affordability of a Healthy Diet (CoAHD); 10,320 righe, periodi 2017–2025. URL: https://bulks-faostat.fao.org/production/Cost_Affordability_Healthy_Diet_(CoAHD)_E_All_Data_(Normalized).zip
- **FAOSTAT HCES:** Food and Diet: Apparent intake (based on household consumption and expenditure surveys); 1,166,330 righe, periodi 2010–2024. URL: https://bulks-faostat.fao.org/production/Household_Consumption_and_Expenditure_Surveys_Food_and_Diet_E_All_Data_(Normalized).zip
