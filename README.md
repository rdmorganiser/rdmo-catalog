# RDMO Catalog

The repository holds XML files that can be imported into RDMO. They contain different kinds of information like for example the domain model, question catalogs or optionsets.

The files that are officially provided by the RDMO project are in the `rdmorganiser` folder. We recommend to import these files to be able to make use of the official domain model, options, tasks and conditions. _Note that parts of these data are required to import user content because RDMO user's question catalogs may refer to parts of the official data_.

Content shared by RDMO Users can be found under `shared`. There may be multiple files in a folder like for example conditions, options and questions. Files in the same folder belong together. All of them should be imported. Please pay attention to the order in which you import files. Question catalogs referring to other content should be imported at last.

Different scripts are located in `tools`. These are interesting for people maintaining this repo.


## Shared catalogs

|Title|File|
|---|---|
|All questions|shared/fodako/catalog_all.xml|
|DFG grants (scientific editions in litary studies)|shared/ub_fau_erlangen_nuernberg/DFG_Editionen/DFG_editions.xml|
|DFG|shared/fodako/catalog_dfg.xml|
|Economics + DFG|shared/fodako/catalog_economics_dfg.xml|
|Educational Sci. + DFG|shared/fodako/catalog_edu_dfg.xml|
|Horizon 2020 Grants|shared/ub_fau_erlangen_nuernberg/eHum_H2020/eHum_H2020_Fragebogen.xml|
|RDMO Mechanical Engineering V0.1 - 28.03.2019|shared/nfdi4ing/rdmo_mechanical_engineering/catalog_mb_20190124.xml|
|Sociology + DFG|shared/fodako/catalog_ratswd_dfg.xml|

8 catalogs shared


## Issues

If you encounter any problems with the questionaires, the domain model, or other content of this repository, please file an issue here: https://github.com/rdmorganiser/rdmo-catalog/issues. For problems or bugs with the RDMO Software, please use the issues in the [rdmo](https://github.com/rdmorganiser/rdmo) repository: https://github.com/rdmorganiser/rdmo/issues. In order to file issues, you will need a GitHub account.
