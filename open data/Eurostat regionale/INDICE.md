# Eurostat, statistiche regionali (API di diffusione)

File TSV compressi scaricati il 26 ottobre 2026 dall’API pubblica di Eurostat (`https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/<codice>?format=TSV&compressed=true`), senza alcuna modifica. Ogni file contiene l’intero dataset per tutti i territori NUTS disponibili (paesi, macroregioni, regioni, province) e tutti gli anni pubblicati. La cartella `codelist/` contiene le liste di codici delle dimensioni usate (etichette ufficiali in inglese) e `toc.txt` è l’indice di Eurostat con le date di aggiornamento.

Licenza: dati Eurostat riutilizzabili con citazione della fonte (© Unione europea, Eurostat). Gli indicatori dell’Atlante dei dati sono selezioni di questi file: vedi `atlante/strumenti/estrai_eurostat_api.py`.

| Codice | Titolo (Eurostat) | Ultimo aggiornamento della fonte | Indicatori dell’Atlante |
|---|---|---|---|
| `agr_r_milkpr` | Production of cow's milk on farms by NUTS 2 region | 2025-12-01 | 1 |
| `apro_cpshr` | Crop production in EU standard humidity by NUTS 2 region | 2026-09-08 | 8 |
| `apro_mt_ls_r` | Animal populations by NUTS 2 region | 2026-09-29 | 5 |
| `bd_size_r` | Business demography by size class and NUTS 3 region | 2026-03-13 | 7 |
| `crim_gen_reg` | Police-recorded offences by NUTS 3 region | 2026-06-29 | 6 |
| `cult_emp_reg` | Cultural employment by NUTS 2 region | 2025-09-02 | 1 |
| `demo_r_find2` | Fertility indicators by NUTS 2 region | 2026-09-30 | 2 |
| `demo_r_gind3` | Population change - Demographic balance and crude rates at regional level (NUTS 3) | 2026-07-21 | 6 |
| `demo_r_minfind` | Infant mortality rates by NUTS 2 region | 2026-10-07 | 1 |
| `demo_r_mlifexp` | Life expectancy by age, sex and NUTS 2 region | 2026-06-01 | 4 |
| `demo_r_pjanind3` | Population structure indicators by NUTS 3 region | 2026-07-10 | 7 |
| `edat_lfse_04` | Population in private households by educational attainment level and NUTS 2 region | 2026-09-10 | 4 |
| `edat_lfse_16` | Early leavers from education and training by NUTS 2 region | 2026-09-10 | 3 |
| `edat_lfse_22` | Young persons neither in employment nor in education and training by NUTS 2 region (NEET rates) | 2026-09-10 | 3 |
| `hlth_cd_asdr2` | Causes of death - standardised death rate by NUTS 2 region of residence | 2026-06-08 | 15 |
| `hlth_rs_bdsrg2` | Available beds in hospitals by NUTS 2 region | 2026-07-13 | 1 |
| `hlth_rs_physreg` | Physicians by NUTS 2 region | 2026-07-13 | 1 |
| `hlth_silc_08_r` | Self-reported unmet needs for medical examination by main reason declared and NUTS 2 region | 2026-10-20 | 1 |
| `hrst_st_rcat` | Human resources in science and technology (HRST) by category and NUTS 2 region | 2026-09-10 | 2 |
| `htec_emp_reg2` | Employed persons in technology and knowledge-intensive sectors by NACE Rev. 2 activity and NUTS 2 region (2008-2026) | 2026-09-10 | 2 |
| `ilc_di11_r` | Income quintile share ratio S80/S20 by NUTS 2 region | 2026-10-20 | 1 |
| `ilc_li41` | At-risk-of-poverty rate by NUTS 2 region | 2026-10-20 | 1 |
| `ilc_lvhl21n` | Persons living in households with very low work intensity by NUTS 2 region (population aged 0 to 64 years) | 2026-10-20 | 1 |
| `ilc_lvho04n` | Average number of rooms per person by NUTS 2 region | 2026-10-20 | 1 |
| `ilc_lvho07_r` | Housing cost overburden rate by NUTS 2 region | 2026-10-20 | 1 |
| `ilc_mdes01_r` | Inability to keep home adequately warm by NUTS 2 region | 2026-10-20 | 1 |
| `ilc_mdsd18` | Severe material and social deprivation by NUTS 2 region | 2026-10-20 | 1 |
| `ilc_peps11n` | Persons at risk of poverty or social exclusion by NUTS 2 region | 2026-10-20 | 1 |
| `isoc_r_blt12_i` | Individuals who ordered goods or services over the internet for private use | 2026-04-17 | 1 |
| `isoc_r_gov_i` | Individuals who used the internet for interaction with public authorities | 2026-04-17 | 1 |
| `isoc_r_iacc_h` | Households with access to the internet at home | 2026-06-25 | 1 |
| `isoc_r_iuse_i` | Individuals who used the internet, frequency of use and activities | 2026-04-17 | 3 |
| `lan_lcv_art` | Land covered by artificial surfaces by NUTS 2 region | 2025-07-24 | 2 |
| `lan_lcv_fao` | Land cover for FAO Forest categories by NUTS 2 region | 2025-07-25 | 1 |
| `lan_use_ovw` | Land use overview by NUTS 2 region | 2025-07-25 | 2 |
| `lfst_r_lfe2emprt` | Employment rates by NUTS 2 region | 2026-09-10 | 6 |
| `lfst_r_lfp2actrt` | Labour force participation rates by NUTS 2 region | 2026-09-10 | 2 |
| `lfst_r_lfu2ltu` | Persons in long-term unemployment (12 months or more) by educational attainment level and NUTS 2 region | 2026-09-10 | 1 |
| `lfst_r_lfu3rt` | Unemployment rates by educational attainment level and NUTS 2 region | 2026-09-10 | 4 |
| `nama_10r_2gfcf` | Gross fixed capital formation by NUTS 2 region for total economy and general government | 2026-03-26 | 1 |
| `nama_10r_2gvagr` | Gross domestic product (GDP) and Gross value added (GVA) in volume by NUTS 2 region | 2026-03-23 | 1 |
| `nama_10r_2hhinc` | Income of households by NUTS 2 region | 2026-05-20 | 2 |
| `nama_10r_2nlp` | Nominal Labour productivity by NUTS 2 region | 2026-06-26 | 2 |
| `nama_10r_3empers` | Employment (thousand persons) by NUTS 3 region | 2026-07-31 | 7 |
| `nama_10r_3gdp` | Gross domestic product (GDP) at current market prices by NUTS 3 region | 2026-02-10 | 4 |
| `nrg_chddr2_a` | Cooling and heating degree days by NUTS 3 region - annual data | 2026-05-08 | 2 |
| `pat_ep_rtot` | Patent applications to the EPO by priority year by NUTS 3 region (1977-2012) | 2016-04-29 | 1 |
| `rd_e_gerdreg` | GERD by sector of performance and NUTS 2 region | 2026-09-29 | 3 |
| `rd_p_persreg` | R&D personnel and researchers by sector of performance, sex and NUTS 2 region | 2026-09-29 | 2 |
| `reg_area3` | Area by NUTS 3 region | 2026-01-22 | 1 |
| `tour_cap_nuts2` | Establishments, bedrooms and bed-places in tourist accommodation, by NUTS 2 region | 2026-10-12 | 1 |
| `tour_ce_oan3` | Guest nights spent at short-stay accommodation offered via online platforms by NUTS 3 region | 2026-09-22 | 1 |
| `tour_occ_arn2` | Arrivals at tourist accommodation establishments by NUTS 2 region | 2026-10-12 | 1 |
| `tour_occ_nin2` | Nights spent at tourist accommodation establishments by NUTS 3 region | 2026-10-20 | 3 |
| `tran_r_acci` | Victims in road accidents by NUTS 2 region | 2026-08-31 | 3 |
| `tran_r_avpa_nm` | Air transport of passengers by NUTS 2 region | 2026-05-11 | 1 |
| `tran_r_elvehst` | Stock of electric vehicles by category and NUTS 2 region | 2026-08-31 | 2 |
| `tran_r_mapa_nm` | Maritime transport of passengers by NUTS 2 region | 2026-03-15 | 1 |
| `tran_r_net` | Road, rail and navigable inland waterways networks by NUTS 2 region | 2026-09-24 | 4 |
| `tran_r_vehst` | Stock of vehicles by category and NUTS 2 region | 2026-08-31 | 2 |
| `tran_sf_roadnu` | Road accidents by NUTS 3 region | 2026-08-25 | 2 |
| `trng_lfse_04` | Participation rate in education and training (last 4 weeks) by NUTS 2 region | 2026-09-10 | 1 |

Totale: 62 dataset, 160 indicatori.
