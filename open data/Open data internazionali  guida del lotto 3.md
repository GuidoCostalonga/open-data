# Open data internazionali: lotto 3

Il terzo lotto è complementare ai primi due: non ne modifica i file e non ne ripubblica le osservazioni. Il progetto degli otto portali resta parziale; la presenza di un catalogo o di una serie nel registro non implica che siano stati scaricati tutti i dati del portale.

## Contenuto e organizzazione

- **Nuovi dati:** 20 indicatori OMS/GHO e due dataset Eurostat sul mercato del lavoro regionale; tutte le annualità e disaggregazioni restituite, senza filtri temporali.
- **Excel dati:** 346, per 219 paesi/economie e 90 aggregati distinti.
- **OMS/GHO:** 377,801 righe, di cui 376,235 con numero.
- **Eurostat:** 2,102,026 righe, di cui 1,390,882 con numero; 36 paesi/economie oltre agli aggregati.
- **Registro:** 110,691 nuove serie e 196,250 serie cumulative dei tre lotti, comprese quelle con sole righe nulle.
- **Limite:** tutti gli Excel e ZIP inferiori a 29.000.000 byte. File dati più grande: 3,772,691 byte.

Aprire l'indice separato `Open-data-internazionali_Indice-lotto-03.xlsx`, foglio `FILE`, per individuare gli archivi e le eventuali parti. Ogni ZIP contiene questa guida e i soli nuovi Excel dati; l'indice non è ripetuto negli ZIP per limitarne le dimensioni. Scaricare tutte le parti di un paese. Il dettaglio territoriale è filtrabile dentro i file nazionali, non un file autonomo per ogni regione.

## Fonte e dimensioni

I dati sanitari sono acquisiti direttamente dall'[API OMS/GHO](https://www.who.int/data/gho/info/gho-odata-api). La colonna `Value` originale, i valori numerici, gli intervalli `Low`/`High`, i commenti, le date, gli ID e tutte le dimensioni restano disponibili. L'API non espone un campo unità autonomo in queste risposte: usare il nome esatto dell'indicatore, senza interpretare la colonna unità vuota come assenza di unità. I cataloghi dei codici OMS sono inclusi nell'indice e nei dizionari pertinenti dei file.

I dataset Eurostat sono [disoccupazione per istruzione e regione NUTS 2](https://ec.europa.eu/eurostat/databrowser/view/lfst_r_lfu3rt/default/table) e [occupazione per regione NUTS 2](https://ec.europa.eu/eurostat/databrowser/view/lfst_r_lfe2emprt/default/table?lang=en). Sesso, età, istruzione, unità, frequenza e stati sono conservati, con etichette originali e JSON completo delle dimensioni. Solo le celle senza numero e senza stato sono omesse.

## Controllo cumulativo delle duplicazioni

Identità di serie: fonte + database/dataset + tutte le dimensioni originali non temporali, con SHA256 della chiave canonica. È stata verificata l'assenza di intersezioni con le 85,559 serie dei lotti 1 e 2. Per l'OMS la chiave comprende tipo e codice geografico, dimensioni di disaggregazione, fonte secondaria e tipo temporale; la chiave dell'osservazione aggiunge periodo e date di inizio/fine. Per Eurostat comprende tutte le dimensioni tranne il tempo.

Il registro cumulativo contiene identità, lotto e conteggi, non i valori del passato. Identica tematica o uguaglianza numerica non bastano a stabilire equivalenza: dati OMS e Banca Mondiale restano distinti e non vanno fusi automaticamente.

## Geografie, valori e limiti

Paesi/economie e aggregati sono separati. Le regioni OMS sono raggruppamenti sovranazionali e non suddivisioni amministrative; i loro dati non devono essere sommati ai paesi componenti. I codici Eurostat NUTS sono statistici, possono cambiare nel tempo e non sono sempre equivalenti a regioni amministrative. Nessuna armonizzazione retroattiva dei confini o dei codici è stata effettuata.

Conservate le scale numeriche originali, senza imputazioni, conversioni di unità o interpolazioni. Un valore percentuale di 35 resta 35, non 0,35; un nullo non diventa zero. Non sommare tassi, medie, totali e componenti, periodi diversi o livelli geografici sovrapposti. Dati stimati, modellizzati, provvisori e discontinuità restano quelli della fonte.

## Copertura cumulativa e residua

Acquisiti finora 150 indicatori WDI, sette dataset Eurostat e 20 indicatori OMS/GHO, non l'interezza di questi portali. Rimangono ulteriori raccolte in tali fonti e le acquisizioni dirette da [data.europa.eu](https://data.europa.eu/), [UNdata](https://data.un.org/), [OCSE](https://www.oecd.org/en/data/datasets/oecd-DE.html), [FMI](https://data.imf.org/) e [FAOSTAT](https://www.fao.org/faostat). Il dettaglio subnazionale raccolto resta limitato ai dataset Eurostat, non a tutte le regioni del mondo.

## Verifiche e provenienza

Acquisizione: 2026-10-24T22:02:24Z / 2026-10-24T22:12:47Z. I download paginati sono riuniti seguendo tutti i collegamenti successivi e verificando il conteggio OData quando disponibile. Tutte le righe sono state rilette dagli Excel e confrontate con identità, periodo e numero originale; controllate unità, disaggregazioni, stati e JSON. Per OMS controllati anche gli estremi numerici degli intervalli e gli ID.

Verificati null, conteggi, integrità ZIP, SHA256, assenza di formule/celle di errore e dimensioni. I 535 Excel dati già consegnati nei lotti 1 e 2 risultano invariati. Confronto numerico con tolleranza relativa/assoluta di 1e-14 per la rappresentazione Excel; testo originale del numero conservato a fianco. Consultare termini e condizioni delle singole fonti: non viene attribuita una licenza unica alla consegna.
