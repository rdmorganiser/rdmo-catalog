# DFG-Checkliste
* Contact / Maintainer: RDMO community, rdmo-contact@listserv.dfn.de
* Version: 1.0
* License: CC0

# Changes from 2026-03-30
There are now two versions of the xml file. Depending on your RDMO system, you should chose the appropriate one:
* **DFG-Checkliste_greater_RDMO-Vers.2** for import in RDMO systems with versions greater than 2.0
* **DFG-Checkliste_greater_RDMO-Vers.2** for import in RDMO systems with versions lower than 2.0

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

## Necessary instution-specific adjustments
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
