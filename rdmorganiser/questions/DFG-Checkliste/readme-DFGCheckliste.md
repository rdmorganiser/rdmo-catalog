# DFG-Checkliste
* Contact / Maintainer: RDMO community, rdmo-contact@listserv.dfn.de
* Version: 1.1
* License: CC0

# Changes from 2026-03-30
There are now two versions of the xml file. The default file to be used is **questions-DFGCheckliste-simple.xml**, which is also maintained on the long term. For RDMO _software_ versions between 2.0 and 2.5 excluded, it is recommended to use **questions-DFGCheckliste-fullexport.xml** which contains also the needed attributes, options and conditions.

# Changes from 2023-06-60
* Attribute "https://rdmorganiser.github.io/terms/domain/project/dataset/curation/responsible_person/name" added to question "Who is responsible for curating the data after the end of the project?"

# Scope
This catalog is the [checklist published by the DFG](https://www.dfg.de/research_data/checklist), supplemented by help texts and option sets.

# Import

## Files
* questions/questions-DFGCheckliste-simple.xml
OR:
* questions/questions-DFGCheckliste-fullexport.xml


## Dependencies
RDMO standard domain and option sets required:
* domain/attributes.xml
* options/optionsets.xml

## Necessary institution-specific adjustments
Several questions or linked optionsets of the catalog need institution-specific adjustements after import:
* https://rdmorganiser.github.io/terms/questions/DFG-Checkliste/data_description/data_content
* https://rdmorganiser.github.io/terms/questions/DFG-Checkliste/rights/publication_restrictions/publication_limitations
* https://rdmorganiser.github.io/terms/questions/DFG-Checkliste/exchange_access/reuse/reuse_when
* https://rdmorganiser.github.io/terms/questions/DFG-Checkliste/responsibilities/resources/datahandling_resources

## Installation
Installing the DFG-checkliste to your rdmo instance from the command line you need to 
```
./manage.py import /path/to/domain/rdmo.xml
./manage.py import /path/to/conditions/rdmo.xml  # yes, again
./manage.py import /path/to/options/rdmo.xml
./manage.py import /path/to/conditions/rdmo.xml  # yes, again
./manage.py import /path/to/questions/DFG-Checkliste.xml
./manage.py import /path/to/tasks/rdmo.xml
./manage.py import /path/to/views/rdmo.xml
```
