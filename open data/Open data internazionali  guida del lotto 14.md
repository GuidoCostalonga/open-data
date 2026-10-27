# Open data internazionali: lotto 14

Il lotto 14 aggiunge cinque risorse FAOSTAT alle raccolte precedenti, dopo il recupero e la verifica integrale dei lotti 1–13. La raccolta complessiva degli otto portali resta parziale: questo documento distingue dati effettivamente consegnati, registri di continuità e risorse ancora da acquisire.

## Risultati e continuità

| Misura | Lotti 1–13 verificati | Lotto 14 | Cumulativo 1–14 |
|---|---:|---:|---:|
| Osservazioni, comprese righe con valori mancanti o testuali | 19.533.271 | 2.067.929 | 21.601.200 |
| Identità di serie | 2.062.358 | 117.971 | 2.180.329 |
| Excel dati | 3.152 | 325 | 3.477 |

I 325 nuovi Excel sono distribuiti in sette ZIP per paesi, economie e territori originali, anche storici, e due ZIP per aggregati statistici. I primi contengono 261 Excel e i secondi 64; questi numeri non equivalgono a 261 Stati attuali e 64 regioni amministrative.

Il recupero iniziale non conteneva tutti gli allegati storici. Sono stati scaricati individualmente 27 allegati mancanti, quindi verificati tutti i 3.152 Excel dati contro gli indici dei rispettivi lotti, i conteggi, le dimensioni e gli SHA256, insieme all’integrità CRC degli archivi ZIP.

## Risorse aggiunte

| Codice | Risorsa originale e provenienza | Righe effettive | Identità | Periodi presenti |
|---|---|---:|---:|---|
| GCE | [Emissions from Crops](https://bulks-faostat.fao.org/production/Emissions_crops_E_All_Data_(Normalized).zip) | 766.730 | 14.320 | 1961–2050 |
| RA | [Fertilizers archive](https://bulks-faostat.fao.org/production/Inputs_FertilizersArchive_E_All_Data_(Normalized).zip) | 178.192 | 9.539 | 1961–2001 |
| RY | [Machinery Archive](https://bulks-faostat.fao.org/production/Investment_MachineryArchive_E_All_Data_(Normalized).zip) | 328.932 | 7.999 | 1961–2005 |
| SDGB | [SDG Indicators](https://bulks-faostat.fao.org/production/SDG_BulkDownloads_E_All_Data_(Normalized).zip) | 478.304 | 53.262 | 1974–2026 |
| SXS | [Suite of Gender Indicators](https://bulks-faostat.fao.org/production/Suite_of_gender_indicators_E_All_Data_(Normalized).zip) | 315.771 | 32.851 | 2000–2025 |

I periodi sono quelli effettivamente contenuti nei CSV scaricati il 25 ottobre 2026. Le annualità future del file GCE sono mantenute con dimensioni, descrizioni e flag originali e non sono presentate come rilevazioni già osservate; RA e RY sono archivi storici dismessi, non aggiornamenti delle serie correnti.

Per GCE, il [catalogo ufficiale FAOSTAT](https://bulks-faostat.fao.org/production/datasets_E.json) dichiara 729.955 righe, mentre il CSV acquisito ne contiene 766.730: lo scostamento di 36.775 righe è documentato nel foglio `CONFRONTO_CATALOGO`. Non sono state eliminate righe per far coincidere il CSV con il catalogo, né sono state inventate osservazioni mancanti.

## File e registro cumulativo

- **Indice del lotto 14:** `Open-data-internazionali_Indice-lotto-14.xlsx` contiene il manifest degli Excel e dei rispettivi ZIP, i dataset acquisiti, i territori, gli hash, il confronto con il catalogo, la coda FAOSTAT aggiornata e la prima parte del registro nel foglio `REGISTRO_SERIE`.
- **Stato complessivo:** `Open-data-internazionali_Stato-complessivo-lotti-01-14.xlsx` riporta i totali per lotto e per ciascuno degli otto portali, i limiti della copertura e lo stato delle risorse FAOSTAT.
- **Dizionari:** `Lotto-14_Dizionari-originali-FAOSTAT.xlsx` conserva tutti i dizionari ufficiali presenti nei cinque archivi, inclusi flag, elementi, prodotti, fonti, sesso, età, attività e livelli geografici.
- **Nuova appendice del registro:** `Lotto-14_Registro-cumulativo_parte-22.xlsx` contiene le 117.971 nuove identità. È un’appendice cumulativa e non una sostituzione delle parti storiche.
- **Verifica e manifest:** `Lotto-14_Manifest-e-verifica.zip` contiene i manifest leggibili automaticamente, il verbale dei controlli, gli hash dei file e la documentazione del recupero storico.

Il registro completo del lotto 14 è composto da 22 parti. La parte 1 è nel nuovo indice; le parti 2–21 restano i file originali immutati del lotto 13 e sono ripubblicate nei seguenti ZIP di continuità; la parte 22 è il nuovo Excel separato.

| ZIP di continuità | File Excel storici contenuti |
|---|---|
| `Registro-cumulativo_lotto-14_parti-02-04.zip` | Parti 02, 03, 04 |
| `Registro-cumulativo_lotto-14_parti-05-07.zip` | Parti 05, 06, 07 |
| `Registro-cumulativo_lotto-14_parti-08-10.zip` | Parti 08, 09, 10 |
| `Registro-cumulativo_lotto-14_parti-11-13.zip` | Parti 11, 12, 13 |
| `Registro-cumulativo_lotto-14_parti-14-16.zip` | Parti 14, 15, 16 |
| `Registro-cumulativo_lotto-14_parti-17-19.zip` | Parti 17, 18, 19 |
| `Registro-cumulativo_lotto-14_parti-20-21.zip` | Parti 20, 21 |

Gli Excel estratti da questi sette ZIP conservano i nomi `Lotto-13_Registro-cumulativo_parte-NN.xlsx` richiamati dall’indice. Sono copie byte per byte dei registri già pubblicati: non sono nuovi dati e non incrementano i conteggi delle osservazioni, delle identità o degli Excel dati.

## Conservazione e controlli

- **Schema:** gli Excel dati mantengono le 16 colonne comuni dei lotti precedenti, seguite dai campi originali aggiuntivi. Le intestazioni sono alla riga 3, i dati iniziano dalla riga 4 e gli schemi dei fogli `FILE`, `DATASET_LOTTO`, `REGISTRO_SERIE`, `REGISTRI`, `CONFRONTO_CATALOGO` e `CATALOGO_DATI` sono mantenuti.
- **Valori:** la colonna numerica è affiancata dal numero originale in testo. Soglie, valori testuali e assenze non sono convertiti in valori puntuali o in zero; i 2.067.929 record comprendono 1.738.770 valori numerici.
- **Unità e provenienza:** nessuna conversione monetaria o di unità, nessuna stima propria e nessuna sostituzione dei flag. Descrizioni, note, URL, aggiornamenti dichiarati dalla fonte e tutte le annualità disponibili restano conservati.
- **Identità:** SHA256 della stringa `FAOSTAT|dataset|JSON_canonico_dimensioni`, con chiavi ordinate, separatori JSON compatti e dimensioni codificate non temporali, comprese le unità. Nessuna nuova identità interseca le 2.062.358 identità precedenti e nessuna osservazione ripete la stessa coppia serie-periodo nei cinque nuovi dataset.
- **Confronto fra dataset:** il confronto esatto di tutte le dimensioni codificate e delle unità, ignorando il namespace del dataset, non ha rilevato candidati fra le nuove serie e quelle FAOSTAT precedenti. Questo controllo non pretende di armonizzare semanticamente classificazioni o codici differenti: risorse con provenienza e dimensioni diverse rimangono distinguibili.
- **Geografia:** aggregati statistici separati dai paesi e territori originali. Nessuna nuova regione amministrativa è dichiarata acquisita nel lotto 14; i livelli nazionale, urbano/rurale e altre disaggregazioni SXS restano dimensioni della fonte, senza attribuzioni amministrative dedotte.
- **Rilettura:** tutti i campi dei 325 Excel dati sono riletti e confrontati con lo staging derivato dai CSV. I testi originali sono confrontati carattere per carattere; la rappresentazione numerica è verificata separatamente, conservando comunque il testo numerico esatto.
- **Archivi e dimensioni:** verificati conteggi, identità, somme, SHA256, CRC, tutti i registri e le copie storiche. Ogni Excel e ogni ZIP consegnato è strettamente inferiore a 29.000.000 byte.

## Ripresa successiva e copertura residua

Il catalogo FAOSTAT consultato comprende 69 risorse: 41 risultano acquisite nei lotti 1–14 e 28 restano marcate `Da acquisire`. Gli altri sette portali mantengono la copertura dei lotti precedenti, che è ancora parziale; non sono stati riverificati o dichiarati esauriti in questa esecuzione.

Per riprendere occorre recuperare i file pubblicati e verificare tutte le 22 parti del registro, non soltanto le 100.000 identità nel foglio dell’indice. Non si deve presumere che i vecchi percorsi locali o i CSV di lavoro siano accessibili: usare indice, nove ZIP dati, sette ZIP di continuità, parte 22 e manifest pubblicati come riferimenti di recupero.

La consegna del lotto 14 non attiva un processo in background. I dati già consegnati dei lotti 1–13 restano immutati e sono stati verificati, non duplicati nei nuovi ZIP dati.
