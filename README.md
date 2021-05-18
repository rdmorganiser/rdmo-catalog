# RDMO Catalog

The repository holds XML files that can be imported into RDMO. They contain different kinds of information like for example the domain model, question catalogs or optionsets.

The files that are officially provided by the RDMO project are in the `rdmorganiser` folder. We recommend to import these files to be able to make use of the official domain model, options, tasks and conditions. _Note that parts of these data are required to import user content because RDMO user's question catalogs may refer to parts of the official data_.

Content shared by RDMO Users can be found under `shared`. There may be multiple files in a folder like for example conditions, options and questions. Files in the same folder belong together. All of them should be imported. Please pay attention to the order in which you import files. Question catalogs referring to other content should be imported at last.

Different scripts are located in `tools`. These are interesting for people maintaining this repo.


## Issues

If you encounter any problems with the questionaires, the domain model, or other content of this repository, please file an issue here: https://github.com/rdmorganiser/rdmo-catalog/issues. For problems or bugs with the RDMO Software, please use the issues in the [rdmo](https://github.com/rdmorganiser/rdmo) repository: https://github.com/rdmorganiser/rdmo/issues. In order to file issues, you will need a GitHub account.


## Shared catalogs

|Title|File|
|---|---|
|All questions|shared/fodako/all.xml|
|DFG 101 Ancient Cultures|shared/fodako/101_dfg.xml|
|DFG 104 Spoken corpus|shared/fodako/spokencorpus_dfg.xml|
|DFG 104 Text corpus|shared/fodako/textcorpus_dfg.xml|
|DFG 105 Edition|shared/fodako/edition_dfg.xml|
|DFG 106  	Social and Cultural Anthropology, Non-Europ. Cultures, Jewish Studies, Religious Studies|shared/fodako/106_dfg.xml|
|DFG 109 Educational Research|shared/fodako/edu_dfg.xml|
|DFG 111 Social Sciences|shared/fodako/ratswd_dfg.xml|
|DFG 112 Economics|shared/fodako/economics_dfg.xml|
|DFG Biodiversity research|shared/fodako/biodiversity_dfg.xml|
|DFG grants (Ancient Cultures, Review Board 101)|shared/ub_fau_erlangen_nuernberg/dfg-alte-kulturen/dfg_alte_kulturen_fk101.xml|
|DFG grants (scientific editions in litary studies)|shared/ub_fau_erlangen_nuernberg/dfg-editionen/dfg_editions.xml|
|DFG grants (sozial &amp; cultural anthropology, Judaic studies, religious studies)|shared/ub_fau_erlangen_nuernberg/dfg-sozkulttheo/dfg_sozkulttheo_fk106.xml|
|DFG|shared/fodako/dfg.xml|
|EmiMin lead V1.0|shared/EmiMin/publisso_terms4life_emimin_lead_V1_questions.xml|
|EmiMin V1.0|shared/EmiMin/publisso_terms4life_emiminV1_questions.xml|
|HeFDI DMP|shared/HeFDI/4_hefdi_template_questions_1.4.xml|
|Horizon 2020 Grants|shared/ub_fau_erlangen_nuernberg/h2020-ehum/ehum_h2020_fragebogen.xml|
|RDMO Mechanical Engineering V0.1 - 28.03.2019|shared/nfdi4ing/rdmo_mechanical_engineering/catalog_mb_20190124.xml|
||shared/ub_fau_erlangen_nuernberg/h2020-ehum/views_h2020.xml|
|VW Foundation - Science Europe Research Data Management Plan|shared/ub_fau_erlangen_nuernberg/ScienceEurope_VW_Stiftung/catalog_VW_SE.xml|

21 catalogs shared
