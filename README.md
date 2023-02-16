# RDMO Catalog

![Tests](https://github.com/rdmorganiser/rdmo-catalog/actions/workflows/tests.yaml/badge.svg)

The repository holds XML files that can be imported into RDMO. They contain different kinds of information like for example the domain model, question catalogs or optionsets.

The files that are officially provided by the RDMO project are in the `rdmorganiser` folder. We recommend to import these files to be able to make use of the official domain model, options, tasks and conditions. *Note that parts of these data are required to import user content because RDMO user's question catalogs may refer to parts of the official data*.

Content shared by RDMO Users can be found under `shared`. There may be multiple files in a folder like for example conditions, options and questions. Files in the same folder belong together. All of them should be imported. Please pay attention to the order in which you import files. Question catalogs referring to other content should be imported at last.

Different scripts are located in `tools`. These are interesting for people maintaining this repo.

## Issues

If you encounter any problems with the questionaires, the domain model, or other content of this repository, please file an issue here: https://github.com/rdmorganiser/rdmo-catalog/issues.

For problems or bugs with the RDMO Software, please use the issues in the [rdmo](https://github.com/rdmorganiser/rdmo) repository: https://github.com/rdmorganiser/rdmo/issues. In order to file issues, you will need a GitHub account.

## Shared catalogs

| Coverage (funder, subject, geographical region) | File                                                                                                                                                                                                    | Last update |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| All questions (long)                            | [RDMO team](rdmorganiser/questions/rdmo.xml); [FoDaKo](shared/fodako/all_5.xml)                                                                                                                         | 2016        |
| All questions (short)                           | [RDMO team](rdmorganiser/questions/fhpshort.xml)                                                                                                                                                        | 2018        |
| DFG                                             | [FoDaKo](shared/fodako/dfg_5.xml)                                                                                                                                                                       | 11/2022     |
| DFG Biodiversity research                       | [FoDaKo](shared/fodako/biodiversity_dfg_5.xml)                                                                                                                                                          | 11/2022     |
| DFG Chemistry                                   | [FoDaKo](shared/fodako/chem_dfg_5.xml); [FDM Bayern eHumanities](shared/ub_fau_erlangen_nuernberg/dfg-chemie/dfg_Chemie.xml )                                                                           | 12/2022     |
| DFG 101 Ancient Cultures                        | [FoDaKo](shared/fodako/101_dfg_5.xml); [FDM Bayern eHumanities](shared/ub_fau_erlangen_nuernberg/dfg-alte-kulturen/dfg_alte_kulturen_fk101.xml)                                                         | 11/2022     |
| DFG 104 Spoken corpus                           | [FoDaKo](shared/fodako/spokencorpus_dfg_5.xml)                                                                                                                                                          | 11/2022     |
| DFG 104 Text corpus                             | [FoDaKo](shared/fodako/textcorpus_dfg_5.xml)                                                                                                                                                            | 11/2022     |
| DFG 105 Editions                                | [FoDaKo](shared/fodako/edition_dfg_5.xml); [FDM Bayern eHumanities](shared/ub_fau_erlangen_nuernberg/dfg-editionen/dfg_editions.xml)                                                                    | 11/2022     |
| DFG 106 Social & Cultural Anthropology [...]    | [FoDaKo](shared/fodako/106_dfg_5.xml); [FDM Bayern eHumanities](shared/ub_fau_erlangen_nuernberg/dfg-sozkulttheo/dfg_sozkulttheo_fk106.xml)                                                             | 11/2022     |
| DFG 109 Educational Research                    | [FoDaKo](shared/fodako/109_dfg_5.xml)                                                                                                                                                                   | 11/2022     |
| DFG 112 Economics                               | [FoDaKo](shared/fodako/112_dfg_5.xml)                                                                                                                                                                   | 11/2022     |
| Emissions in animal husbandry                   | [EmiMin](shared/EmiMin/publisso_terms4life_emiminV1_questions.xml); [EmiMin (lead)](shared/EmiMin/publisso_terms4life_emimin_lead_V1_questions.xml)                                                     |             |
| Hessen State                                    | [HeFDI](shared/HeFDI/4_hefdi_template_questions_1.4.xml)                                                                                                                                                |             |
| Horizon 2020                                    | [FDM Bayern eHumanities (catalog)](shared/ub_fau_erlangen_nuernberg/h2020-ehum/ehum_h2020_fragebogen.xml); [FDM Bayern eHumanities (view)](shared/ub_fau_erlangen_nuernberg/h2020-ehum/views_h2020.xml) |             |
| Horizon Europe                                  | [catalog](rdmorganiser/questions/horizon-europe.xml); [view](rdmorganiser/views/horizon-europe.xml)                                                                                                     | 12/2022     |
| Mathematics                                     | [DFG Excellence Cluster MATH+](shared/MATH+/mathplus_questions.xml)                                                                                                                                     | 11/2022     |
| Mechanical Engineering                          | [NFDI4Ing](shared/nfdi4ing/rdmo_mechanical_engineering/catalog_mb_20190124.xml)                                                                                                                         |             |
| Software Management Plan                        | [MPDL](shared/Max-Planck-Digital-Library/Software-Management-Plan/SMP-Questions.xml)                                                                                                                    | 12/2022             |
| VW Foundation - Science Europe                  | [FDM Bayern eHumanities](shared/ub_fau_erlangen_nuernberg/ScienceEurope_VW_Stiftung/catalog_VW_SE.xml)                                                                                                  |             |
| Swiss National Fund                             | [RDMO team](rdmorganiser/questions/snf.xml)                                                                                                                                                             | 2018        |
| DCC checklist                                   | [RDMO team](rdmorganiser/questions/dcc.xml)                                                                                                                                                             | 10/2018     |

29 catalogs shared
