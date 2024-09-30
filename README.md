# RDMO Catalog

![Tests](https://github.com/rdmorganiser/rdmo-catalog/actions/workflows/tests.yaml/badge.svg)

This repository contains all content objects (catalogs, attributes, options, conditions, views, tasks) to be used with the DMP software [RDMO](https://github.com/rdmorganiser/rdmo).

The main branch [master-rdmo2.x](https://github.com/rdmorganiser/rdmo-catalog/tree/master-rdmo2.x) contains material structured according to the recommended data model 2.0.0+. It is at the latest state and will be updated over time.

The legacy branch [master-rdmo1.x](https://github.com/rdmorganiser/rdmo-catalog/tree/master-rdmo1.x) contains material structured according to the previous data model 1.6.0+. It is frozen at the state of April 2024 und will be not updated any more.

The content officially curated by the [RDMO Consortium](https://rdmorganiser.github.io/Community/) is in the [`rdmorganiser`](./rdmorganiser) folder. We recommend to import these files to be able to make use of the official domain model, options, tasks and conditions. *Note that parts of these data are required to import user content because RDMO user's question catalogs may refer to parts of the official data*.

Content shared by RDMO Users can be found under [`shared`](./shared). There may be multiple files in a folder like for example conditions, options and questions. Files in the same folder belong together: all of them should be imported.

Please pay attention to the order in which you import files. Question catalogs referring to other content should be imported at last. See the following section for details.

Different scripts are located in [`tools`](./tools). These are interesting for people maintaining this repo.

# How to install content

The RDMO content objects (catalogs, attributes, options, conditions, views, tasks) depend on each other, as shown in the [documentation](https://rdmo.readthedocs.io/en/latest/management/data-model.html).

In particular, the installation of question catalogues requires the newest version of attributes, optionsets and conditions.

Therefore we suggest this sequence to install content in a RDMO instance:

## Via the RDMO web interface

Management --> Attributes  --> Import <chosen_domain_file>.xml  
Management --> Conditions  --> Import <chosen_conditions_file>.xml  
Management --> Option sets --> Import <chosen_options_file>.xml  
Management --> Conditions  --> Import <chosen_conditions_file>.xml  # yes, again  
Management --> Questions   --> Import <chosen_catalog_file>.xml  
Management --> Tasks       --> Import <chosen_task_file>.xml  
Management --> Views       --> Import <chosen_view_file>.xml  

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

|Subject/Coverage     |Catalog                                                 |View|Last update|Creators   |
|---------------------|--------------------------------------------------------|----|-----------|-----------|
|All questions (long) |[catalog](rdmorganiser/questions/questions-rdmo.xml)    |    |2024-09|RDMO team      |
|All questions (short)|[catalog](rdmorganiser/questions/questions-fhpshort.xml)|    |2020-08|FHP / RDMO team|
|DCC checklist        |[catalog](rdmorganiser/questions/questions-dcc.xml)     |    |2018-10|RDMO team      |
|DFG checklist |[catalog](rdmorganiser/questions/questions-DFG-Checkliste.xml)|[view](rdmorganiser/views/view-dfg-checkliste.xml)|2023-11|RDMO team|
|Horizon Europe|[catalog](rdmorganiser/questions/questions-horizon-europe.xml)|[view](rdmorganiser/views/view-horizon-europe.xml)|2022-12|RDMO team|
|Software Management Plan|[catalog](rdmorganiser/questions/questions-smp.xml)|[view (FAIR4RS)](rdmorganiser/views/view-FAIR4RSview.xml)|2023-11|MPDL / RDMO team|
|Swiss National Fund|[catalog](rdmorganiser/questions/questions-snf.xml)|[view](rdmorganiser/views/snf.xml)|2020-08|RDMO team|
|Bielefeld            |          |[view](rdmorganiser/views/view-bielefeld.xml)     |2019-01|RDMO team      |
|CITEC                |          |[view](rdmorganiser/views/view-citec.xml)         |2019-01|RDMO team      |
|Costs                |          |[view](rdmorganiser/views/view-costs.xml)         |2022-08|RDMO team      |
|DMPonline            |          |[view](rdmorganiser/views/view-dmponline.xml)     |2019-01|RDMO team      |
|DMPtool              |          |[view](rdmorganiser/views/view-dmptool.xml)       |2019-01|RDMO team      |
|Horizon 2020         |          |[view](rdmorganiser/views/view-horizon2020.xml)   |2019-01|RDMO team      |
|All variables        |          |[view](rdmorganiser/views/view-variable_check.xml)|2022-12|RDMO team      |

## Other content provided by the user community

|Subject/Coverage         |Catalog                                        |View|Last update |Creators  |
|-------------------------|-----------------------------------------------|----|------------|----------|
|All questions (RDMO+DFG) |[catalog](shared/fodako/all_5.xml)             |    |2022-03|FoDaKo         |
|BLE                      |[catalog](shared/BLE_JKI/)  |[view](shared/BLE_JKI/)|2023-10|Julius-Kühn-Institut|
|DFG checklist            |[catalog](shared/fodako/dfg_5.xml)             |    |2022-03|FoDaKo         |
|DFG Biodiversity research|[catalog](shared/fodako/biodiversity_dfg_5.xml)|    |2022-03|FoDaKo         |
|DFG Chemistry            |[catalog](shared/fodako/chem_dfg_5.xml)        |    |2022-03|FoDaKo         |
|DFG Chemistry|[catalog](shared/ub_fau_erlangen_nuernberg/dfg-chemie/dfg_Chemie.xml)||2023-08|FDM Bayern eHumanities|
|DFG Chemistry            |[catalog](shared/nfdi4chem)                    |    |2024-06|NFDI4Chem      |
|DFG Engineering          |[catalog](shared/nfdi4ing)                     |    |2024-09|NFDI4Ing       |
|DFG Physics  |[catalog](shared/ub_fau_erlangen_nuernberg/dfg-physik/dfg_Physik.xml)||2023-08|FDM Bayern eHumanities|
|DFG 101 Ancient Cultures |[catalog](shared/ub_fau_erlangen_nuernberg/dfg-alte-kulturen/dfg_alte_kulturen_fk101.xml)||2020-09|FDM Bayern eHumanities|
|DFG 101 Ancient Cultures |[catalog](shared/fodako/101_dfg_5.xml)         |    |2022-03|FoDaKo|
|DFG 104 Spoken corpus    |[catalog](shared/fodako/spokencorpus_dfg_5.xml)|    |2022-03|FoDaKo|
|DFG 104 Text corpus      |[catalog](shared/fodako/textcorpus_dfg_5.xml)  |    |2022-03|FoDaKo|
|DFG 105 Editions         |[catalog](shared/fodako/edition_dfg_5.xml)     |    |2022-03|FoDaKo|
|DFG 105 Editions|[catalog](shared/ub_fau_erlangen_nuernberg/dfg-editionen/dfg_editions.xml)||2020-09|FDM Bayern eHumanities|
|DFG 106 Social & Cultural Anthropology|[catalog](shared/ub_fau_erlangen_nuernberg/dfg-sozkulttheo/dfg_sozkulttheo_fk106.xml)||2020-09|FDM Bayern eHumanities|
|DFG 106 Social & Cultural Anthropology|[catalog](shared/fodako/106_dfg_5.xml)||2022-03|FoDaKo|
|DFG 109 Educational Research          |[catalog](shared/fodako/109_dfg_5.xml)||2022-03|FoDaKo|
|DFG 112 Economics |[catalog](shared/fodako/112_dfg_5.xml)                    ||2022-03|FoDaKo|
|ERC grants        |[catalog](shared/ub_fau_erlangen_nuernberg/erc-grants/erc.xml)|[view](shared/ub_fau_erlangen_nuernberg/erc-grants/ERC_views.xml)|2023-08|FDM Bayern eHumanities|
|Emissions in animal husbandry|[catalog 1](shared/EmiMin/publisso_terms4life_emiminV1_questions.xml)<br />[catalog 2](shared/EmiMin/publisso_terms4life_emimin_lead_V1_questions.xml)||2021-04|EmiMin|
|European Partnership on Metrology|[catalog](shared/metrology-rdm/epm-questions.xml)|[view](shared/metrology-rdm/epm-view-table.xml)|2023-10|TC-IM 1449|
|Hessen State      |[catalog](shared/HeFDI/4_hefdi_template_questions_1.4.xml)||2020-07|HeFDI|
|Horizon 2020      |[catalog](shared/ub_fau_erlangen_nuernberg/h2020-ehum/ehum_h2020_fragebogen.xml)|[view](shared/ub_fau_erlangen_nuernberg/h2020-ehum/views_h2020.xml)|2020-09|FDM Bayern eHumanities|
|Mathematics       |[catalog](shared/MATH+/mathplus_questions.xml)            ||2022-11|DFG Excellence Cluster MATH+|
|Research data policy generator|[catalog](shared/FDNext/)                     ||2024-03|FDNext  |
|VW Foundation - Science Europe|[catalog](shared/ub_fau_erlangen_nuernberg/ScienceEurope_VW_Stiftung/catalog_VW_SE.xml)||2021-04|FDM Bayern eHumanities|

Total: 35 catalogs, 15 views
