# Open data internazionali: lotti 4–12

I lotti dal 4 al 12 sono acquisiti, prodotti in Excel e verificati. Insieme ai primi tre contengono **18,348,832 osservazioni** e **891,910 identità di serie**. Tutti gli Excel e gli ZIP sono inferiori a 29.000.000 byte.

La richiesta di acquisizione integrale di tutti gli otto portali **non è conclusa**. Non è attiva una prosecuzione in background. L'indice Stato complessivo distingue dati acquisiti, cataloghi consultati e risorse ancora mancanti. La coda dei cataloghi non è un archivio di osservazioni scaricate.

## Nuovi lotti

- **Lotto 4:** 12 dataset [FAOSTAT](https://www.fao.org/faostat), 1.845.766 osservazioni.
- **Lotto 5:** 3 flussi [OCSE SDMX](https://sdmx.oecd.org/public/rest/dataflow/all), 1.957.425 osservazioni.
- **Lotto 6:** 14 CSV del [Statistical Yearbook ONU](https://data.un.org/Search.aspx), 73.126 osservazioni.
- **Lotto 7:** 12 risorse CSV di [un dataset di Karlsruhe nel catalogo europeo](https://data.europa.eu/data/datasets/74561f6a-4783-4d70-b86a-008deec09441), 4.860 osservazioni uniche dopo l'accorpamento di 1.620 ripetizioni fra risorse.
- **Lotto 8:** 3 dataset del [dashboard climatico ufficiale FMI](https://climatedata.imf.org/), 97.868 osservazioni, comprese celle mancanti conservate dalla struttura originale.
- **Lotto 9:** 7 archivi [FAOSTAT](https://www.fao.org/faostat), 2,435,165 osservazioni; fertilizzanti, nutrienti, emissioni, allevamenti, bilanci non alimentari e aiuti alimentari.
- **Lotto 10:** 9 archivi [FAOSTAT](https://www.fao.org/faostat), 1,754,457 osservazioni; popolazione, occupazione, condizioni di vita rurali, sicurezza alimentare, emissioni da incendi, macchinari e commercio agricolo.
- **Lotto 11:** 3 archivi [FAOSTAT](https://www.fao.org/faostat), 1,943,725 osservazioni; indicatori delle emissioni, emissioni pre/post produzione agricola e disponibilità alimentare per nutrienti.
- **Lotto 12:** 2 archivi [FAOSTAT](https://www.fao.org/faostat), 2,143,812 osservazioni; indici della produzione agricola e indicatori storici da indagini sulle famiglie.

## Registro e controlli

La versione cumulativa più recente è quella del lotto 12: prima parte nel foglio REGISTRO_SERIE dell'indice e altre 8 parti nei file Registro-cumulativo. I registri dei lotti precedenti sono istantanee storiche, non raccolte aggiuntive di dati. L'identità SHA256 resta fonte canonica + database/dataset + tutte le dimensioni non temporali; le osservazioni aggiungono il periodo. Nessuna nuova serie interseca quelle dei lotti precedenti.

Ogni cella delle nuove tabelle dati è confrontata con lo staging normalizzato dai CSV originali; controlli aggiuntivi verificano valori, campi originali, conteggi, registri, hash, CRC e dimensioni. Gli Excel dei lotti precedenti restano immutati.

Le soglie riportate dalla fonte con < o > rimangono testo nella colonna H e non diventano valori puntuali: la colonna numerica G resta vuota. La popolazione può includere stime e proiezioni dell'editore, riconoscibili dalle denominazioni e dai flag originali. La presenza di periodi futuri nella fonte non li trasforma in dati osservati. I riepiloghi SDG e di genere scaricati per ispezione nel lotto 10 rimangono da acquisire, in attesa del controllo delle sovrapposizioni: non sono conteggiati fra i dati consegnati.

Nel lotto 11 le emissioni sono stime o indicatori della fonte, con gas, metodologie e unità conservati separatamente. SUA descrive la disponibilità alimentare per nutrienti, non il consumo individuale effettivamente osservato. Oltre al registro SHA256, il confronto esatto delle dimensioni codificate e delle unità fra i nuovi database e quelli FAOSTAT precedenti non ha rilevato candidati: non costituisce un confronto semantico fra codifiche differenti.

Nel lotto 12, QI comprende indici lordi e pro capite con base 2014-2016 = 100, non quantità fisiche o percentuali di crescita; Unit è vuoto nell'originale e la base è riportata nella denominazione Element. HS è un archivio storico cessato: i periodi e gli intervalli sono estratti dalla denominazione Survey originale, mantenendo i codici integralmente. Medie, mediane, deviazioni standard, numerosità e valute locali restano distinte, senza conversioni monetarie. Il confronto esatto aggiuntivo fra dimensioni codificate e unità dei database FAOSTAT non ha rilevato candidati, senza pretendere di confrontare semanticamente codifiche differenti.

## Limiti di copertura

I dati regionali amministrativi non sono disponibili per ogni paese. NUTS, aggregati sovranazionali e classificazioni rurale/urbano non vengono spacciati per regioni amministrative. I codici storici sono conservati, non armonizzati automaticamente.

Sono inclusi tutti i periodi presenti nelle risorse effettivamente scaricate. I CSV SYB ONU sono riepiloghi dell'editore e non sostituiscono l'intera storia dei datamart originari. Il vecchio collegamento di esportazione POP non ha restituito un CSV valido; quel datamart non è stato dichiarato acquisito.

I tre dataset FMI appartengono al dashboard climatico: non costituiscono l'acquisizione delle banche dati macroeconomiche del portale. data.europa.eu è stato usato come catalogo di provenienza delle risorse comunali; non è stato esaurito. Restano inoltre numerosi indicatori World Bank e OMS e dataset Eurostat, FAOSTAT e OCSE. L'indice riporta anche [il catalogo TOC Eurostat](https://ec.europa.eu/eurostat/api/dissemination/catalogue/toc/txt?lang=en) come sola coda di metadati.
