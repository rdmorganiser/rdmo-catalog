# RDMO Catalog

![Tests](https://github.com/rdmorganiser/rdmo-catalog/actions/workflows/tests.yaml/badge.svg)

This repository contains all content objects (catalogs, attributes, options, conditions, views, tasks) to be used with the DMP software [RDMO](https://github.com/rdmorganiser/rdmo).

The main branch [master-rdmo2.x](https://github.com/rdmorganiser/rdmo-catalog/tree/master-rdmo2.x) contains material structured according to the recommended data model 2.0.0+. It is at the latest state and will be updated over time.

The legacy branch [master-rdmo1.x](https://github.com/rdmorganiser/rdmo-catalog/tree/master-rdmo1.x) contains material structured according to the previous data model 1.6.0+. It is frozen at the state of April 2024 und will be not updated any more.

The content officially curated by the [RDMO Consortium](https://rdmorganiser.github.io/Community/) is in the [`rdmorganiser`](./rdmorganiser) folder. We recommend to import these files to be able to make use of the official domain model, options, tasks and conditions. *Note that parts of these data are required also to import user-generated content, because RDMO user-generated question catalogs may refer to parts of the official data*.

Content shared by RDMO users can be found under [`shared`](./shared). It can be organised as a single file ("full XML export") or as a collection of multiple files containing additional conditions, options and questions. Files in the same folder belong together: all of them should be imported.

Please pay attention to the order in which you import files. Question catalogs referring to other content should be imported at last. See the following section for details.

Different scripts are located in [`tools`](./tools). These are interesting for people maintaining this repo.

# How to install content

The RDMO content objects (catalogs, attributes, options, conditions, views, tasks) depend on each other, as shown in the [documentation](https://rdmo.readthedocs.io/en/latest/management/data-model.html).

In particular, the installation of question catalogues requires the newest version of attributes, optionsets and conditions.

Therefore we suggest this sequence to install content in a RDMO instance:

## Via the RDMO web interface

Management --> Attributes  --> Import `<chosen_domain_file>.xml`  
Management --> Conditions  --> Import `<chosen_conditions_file>.xml`  
Management --> Option sets --> Import `<chosen_options_file>.xml`  
Management --> Conditions  --> Import `<chosen_conditions_file>.xml`  # yes, again  
Management --> Questions   --> Import `<chosen_catalog_file>.xml`  
Management --> Tasks       --> Import `<chosen_task_file>.xml`  
Management --> Views       --> Import `<chosen_view_file>.xml`  

REMARK: If the chosen catalog is available as a **full XML**, it already includes the necessary attributes, conditions and options.

## Via a Python script

```python
./manage.py import /path/to/domain/<chosen_domain_file>.xml
./manage.py import /path/to/conditions/<chosen_conditions_file>.xml
./manage.py import /path/to/options/<chosen_options_file>.xml
./manage.py import /path/to/conditions/<chosen_conditions_file>.xml  # yes, again
./manage.py import /path/to/questions/<chosen_catalog_file>.xml
./manage.py import /path/to/tasks>/<chosen_task_file>.xml
./manage.py import /path/to/views>/<chosen_view_file>.xml
```

Use the same order when importing over the RDMO web interface.

Please note that the master branch will only work with the latest version of RDMO. If you need the xml files for an older version, please browse the releases or contact us.

To indent the XML files use:

```bash
for f in *.xml; do xmllint --format $f > /tmp/$f; mv /tmp/$f $f; done
```

## Issues

If you encounter any problems with the questionnaires, the domain model, or other content of this repository, please file an issue here: https://github.com/rdmorganiser/rdmo-catalog/issues.

For problems or bugs with the RDMO Software, please use the issues in the [rdmo](https://github.com/rdmorganiser/rdmo) repository: https://github.com/rdmorganiser/rdmo/issues. In order to file issues, you will need a GitHub account.

## Content curated by the RDMO team

|Subject/Coverage        |Catalog                  |View                |Last update|Creators        |
|------------------------|-------------------------|--------------------|-----------|----------------|
|All questions (long)    |[catalog][questions-rdmo]|                    |    2024-09|RDMO team       |
|All questions (short)   |[catalog][questions-fhp] |                    |    2020-08|FHP / RDMO team |
|DCC checklist           |[catalog][questions-dcc] |                    |    2018-10|RDMO team       |
|DFG checklist           |[catalog][questions-dfg]|[view][view-dfg]     |    2023-11|RDMO team       |
|Horizon Europe          |[catalog][questions-heu]|[view][view-heu]     |    2022-12|RDMO team       |
|Software Management Plan|[catalog][questions-smp]|[view][view-smp](FAIR4RS)|2023-11|MPDL / RDMO team|
|Swiss National Fund     |[catalog][questions-snf]|[view][view-snf]         |2020-08|RDMO team       |
|Bielefeld               |                        |[view][view-bielefeld]   |2019-01|RDMO team       |
|CITEC                   |                        |[view][view-citec]       |2019-01|RDMO team       |
|Costs                   |                        |[view][view-costs]       |2022-08|RDMO team       |
|DMPonline               |                        |[view][view-dmponline]   |2019-01|RDMO team       |
|DMPtool                 |                        |[view][view-dmptool]     |2019-01|RDMO team       |
|Horizon 2020            |                        |[view][view-h2020]       |2019-01|RDMO team       |
|All variables           |                        |[view][view-varcheck]    |2022-12|RDMO team       |

## Other content provided by the user community

|Subject/Coverage        |Catalog                    |View  |Last update |Creators              |
|------------------------|---------------------------|------|------------|----------------------|
|All questions (RDMO+DFG)|[catalog](shared/fodako)   |           |2022-03|FoDaKo                |
|BLE                     |[catalog][BLE]             |[view][BLE]|2023-10|Julius-Kühn-Institut  |
|DFG Chemistry           |[catalog][CHE]             |           |2023-08|FDM Bayern eHumanities|
|DFG Chemistry           |[catalog](shared/nfdi4chem)|           |2024-06|NFDI4Chem             |
|DFG Engineering         |[catalog](shared/nfdi4ing) |           |2024-09|NFDI4Ing              |
|DFG Physics             |[catalog][PHY]             |           |2023-08|FDM Bayern eHumanities|
|DFG 101 Ancient Cultures|[catalog][AKU]             |           |2020-09|FDM Bayern eHumanities|
|DFG 105 Editions        |[catalog][EDI]             |           |2020-09|FDM Bayern eHumanities|
|DFG 106 Social & Cultural Anthropology|[catalog][SKT]  |        |2020-09|FDM Bayern eHumanities|
|Emissions in animal husbandry|[2 catalogs](shared/EmiMin)|      |2021-04|EmiMin                |
|ERC grants                       |[catalog][ERC]    |[view][ERC]|2023-08|FDM Bayern eHumanities|
|European Partnership on Metrology|[catalog][EPM]    |[view][EPM]|2023-10|TC-IM 1449            |
|Hessen State                |[catalog](shared/HeFDI)|           |2020-07|HeFDI                 |
|Horizon 2020                |[catalog][EHU]         |[view][EHU]|2020-09|FDM Bayern eHumanities|
|Mathematics                 |[catalog](shared/MATH+)|     |2022-11|DFG Excellence Cluster MATH+|
|Quality Assurance Tool for data    |[catalog](shared/Mathmet-QAT)||2025-01|Mathmet / TC-IM 1449|
|Quality Assurance Tool for software|[catalog](shared/Mathmet-QAT)||2025-01|Mathmet / TC-IM 1449|
|Research data policy generator     |[catalog](shared/FDNext)|   |2024-03|FDNext                |
|VW Foundation - Science Europe     |[catalog][SEU]          |   |2021-04|FDM Bayern eHumanities|

Total: 27 catalogs, 15 views


[AKU]: shared/ub_fau_erlangen_nuernberg/dfg-alte-kulturen/
[CHE]: shared/ub_fau_erlangen_nuernberg/dfg-chemie/
[PHY]: shared/ub_fau_erlangen_nuernberg/dfg-physik/
[EDI]: shared/ub_fau_erlangen_nuernberg/dfg-editionen/
[SKT]: shared/ub_fau_erlangen_nuernberg/dfg-sozkulttheo/
[ERC]: shared/ub_fau_erlangen_nuernberg/erc-grants/
[EHU]: shared/ub_fau_erlangen_nuernberg/h2020-ehum/
[SEU]: shared/ub_fau_erlangen_nuernberg/ScienceEurope_VW_Stiftung/
[EPM]: shared/metrology-rdm/
[BLE]: shared/BLE_JKI/
[questions-rdmo]:           rdmorganiser/questions/questions-rdmo.xml
[questions-fhp]:       rdmorganiser/questions/questions-fhpshort.xml
[questions-dcc]:            rdmorganiser/questions/questions-dcc.xml
[questions-dfg]: rdmorganiser/questions/questions-DFG-Checkliste.xml
[questions-heu]: rdmorganiser/questions/questions-horizon-europe.xml
[questions-smp]:            rdmorganiser/questions/questions-smp.xml
[questions-snf]:            rdmorganiser/questions/questions-snf.xml
[view-dfg]:      rdmorganiser/views/view-dfg-checkliste.xml
[view-heu]:      rdmorganiser/views/view-horizon-europe.xml
[view-smp]:                 rdmorganiser/views/view-FAIR4RSview.xml
[view-snf]:                 rdmorganiser/views/view-snf.xml
[view-bielefeld]:           rdmorganiser/views/view-bielefeld.xml
[view-citec]:               rdmorganiser/views/view-citec.xml
[view-costs]:               rdmorganiser/views/view-costs.xml
[view-dmponline]:           rdmorganiser/views/view-dmponline.xml
[view-dmptool]:             rdmorganiser/views/view-dmptool.xml
[view-h2020]:         rdmorganiser/views/view-horizon2020.xml
[view-varcheck]:      rdmorganiser/views/view-variable_check.xml
