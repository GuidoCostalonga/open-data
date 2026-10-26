# Commissione europea, DG REGIO: piattaforma aperta cohesiondata

File CSV scaricati il 26 ottobre 2026 dalla piattaforma dei dati aperti della politica di coesione della Commissione europea (`https://cohesiondata.ec.europa.eu/resource/<identificativo>.csv`), senza alcuna modifica, con la scheda di ciascun dataset (`<identificativo>.json`, da `https://cohesiondata.ec.europa.eu/api/views/<identificativo>.json`). I dataset sono stati individuati con la ricerca sul portale europeo dei dati aperti data.europa.eu, catalogo “esif” (DG REGIO).

Contenuto: indice di competitività regionale RCI 2.0 (edizioni 2016, 2019 e 2022 ricalcolate con la stessa metodologia), indice di progresso sociale EU-SPI (edizioni 2020 e 2024), indice europeo di qualità delle istituzioni EQI (2010, 2013, 2017, 2021, 2024), monitor regionale di genere 2021, emissioni di gas serra per abitante e intensità carbonica delle regioni 1990-2021 (stime del Centro comune di ricerca, JRC), pagamenti annuali dei fondi europei per regione 1989-2022 (ricostruiti e modellati), produzione e potenziale di energia rinnovabile da sole e vento per provincia (stima JRC pubblicata nel 2024).

Licenze: indicate nella scheda di ogni dataset (Creative Commons CC0 1.0, pubblico dominio o CC BY 4.0); per il dataset EQI la scheda non dichiara una licenza e valgono le condizioni generali di riutilizzo della piattaforma della Commissione europea, con citazione della fonte. Gli indicatori dell’Atlante dei dati sono selezioni di questi file: vedi `atlante/strumenti/estrai_regio.py`.

| Identificativo | Titolo (cohesiondata) | Ultimo aggiornamento della fonte | Righe | Licenza dichiarata | Indicatori dell’Atlante |
|---|---|---|---|---|---|
| `ngxn-bw8m` | EU RCI 2.0 - 2022: Time Evolution | 2023-05-10 | 11690 | Public Domain | 15 |
| `5nmd-5kax` | EU Regional Social Progress Index 2024 | 2024-05-17 | 4224 | Creative Commons 1.0 Universal (Public Domain Dedication) | 16 |
| `99vh-w4e7` | EU Social Progress Index 2020 | 2020-11-18 | 4208 | Public Domain | 16 |
| `eqnk-pu8x` | EU Quality of Government Time Evolution | 2025-03-16 | 4200 | non indicata nella scheda | 4 |
| `q6y9-dn7j` | 2021 EU Regional Gender Monitor | 2021-09-06 | 526 | Creative Commons 1.0 Universal (Public Domain Dedication) | 16 |
| `4bvr-jq77` | EU Regional GHG per capita 1990-2021 | 2023-09-29 | 8640 | Creative Commons 1.0 Universal (Public Domain Dedication) | 1 |
| `krps-v2iz` | EU Regional GHG - carbon intensity - 1990-2021 | 2023-09-29 | 8640 | Creative Commons 1.0 Universal (Public Domain Dedication) | 1 |
| `tc55-7ysv` | Historic EU payments annual timeseries - regionalised and modelled | 2024-03-07 | 41340 | Public Domain | 9 |
| `dau5-jiss` | UntappedPotentialRenewableEnergy | 2024-03-04 | 1161 | Creative Commons 1.0 Universal (Public Domain Dedication) | 5 |
