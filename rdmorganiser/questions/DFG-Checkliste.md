# DFG-Checkliste
* Contact / Maintainer: RDMO community, rdmo-contact@listserv.dfn.de
* Version: 1.0
* License: CC0

# Scope
This catalog is the [checklist published by the DFG](https://www.dfg.de/research_data/checklist), supplemented by help texts and option sets.

# Import

## Files
* questions/DFG-Checkliste.xml

## Dependencies
RDMO standard domain and option sets required:
* domain/rdmo.xml
* options/rdmo.xml

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
