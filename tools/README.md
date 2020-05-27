# Tools 

## Comparing rdmo domain files 
`python3 compare_domains.py` compares two rdmo domains. Two files must be present at execution of the script: `domain.xml` and `rdmo.xml`.
After a successful run the results will be available in three files `deleted.xml`, `changed.xml`, and `added.xml`.  

## Comparing rdmo question files 
`rdmo_catalog_compare.py` will compare rdmo question files. As input two files must be present `rdmo_questions.xml` and `rdmo_catalog_latest_commit.xml`.  
The output 'questions_differences' will print all question uris. If differences are detected they are printed on the question text and help texts level.   

## Catalog Generation
### Quick Guide
- implement changes regarding content and presentation to `all_questions.xml`
  - be sure, that all references to the domain, option sets and conditions are correct as well
- provide catalog information and composition within `cat_member.yaml`
- run `python3 auto_catalog_creation.py`

### Detailed Guide
#### Catalogs
In RDMO, catalogs are based on shallow structured XML-Files. Each file can only contain one complete catalog. Catalogs must be separated by having individual values for the path elements, uri attributes and the `catalog > key` element. The catalog is structured by definition of parent elements (e.g. `question A` has a defined parent `question set B`). The content and the order of the catalog is defined within each direct child of the root element `rdmo`, i.e. `section`, `questionset` and `question`. Since maintaining repetitive content is labour intense and prone to errors this step was automated. 

For automatic generation, the content of all catalogs and the information about catalog composition is kept in tools/all_questions.xml and tools/cat_member.yaml, respectively. The latter additionally provides the catalog name and the value of the `catalog > key` element to automatically separate the catalog for RDMO. 

#### Questions
##### editing content and structure
Question elements save their content in sub-elements shown below. 

| sub-element     | function |
|----------------|:----------:|
| text lang="en" | english question text |
| text lang="de" | german question text  |
| help lang="en" | english help text     |
| help lang="en" | german help text      |

These elements can be easily changed as they are not referenced by any other element. Information regarding the sequence of questions is kept in the following elements.

| sub-element     | function |
|----------------|:----------|
| questionset | refers to the parent element which in turn refers to its parent and so on |
| order | defines the numerical position at which the question is displayed  |
| path | a row of keys referring to the parent structure including the questions key sub-element, separated by "/" |
| key | the individual questions key, separating the questions from its sibling elements in the same question set |
| uri (attribute of the question)| the sum of `uri_prefix` + `path` |

Be careful changing one of these as they reference each other and changes must be applied consistently. Lastly there are the sub-elements for the answer which will be given by the user.

| sub-element     | function |
|----------------|:----------|
| attribute | (mandatory) |
| widget_type | (mandatory) sets the input method for the user |
| value_type | (mandatory) sets the value type of the input |
| maximum | (optional) needs to be set depending on the `widget_type` |
| minimum | " |
| step | " |
| unit | " |
| optionset | " |
| condition | " |

The elements `attribute`, `optionset` and `condition` refer to elements in the respective files, e.g. rdmorganiser/conditions/rdmo.xml. If a new question is added with one or more of these, they need to be created in the respective files as well. They are organised very similar to question elements.

##### limits of this approach
The solution to maintaining the content of all catalogs in what is essentially one big catalog file comes along with limitations. **It is not possible to keep two different versions of the same question**, since currently there is no unique, independent identifier within the data model of RDMO. As a workaround, it is possible to add a new question in both, the tools/all_questions.xml and the cat_member.yaml files with new, unique values for `key`, `path` and `uri`.

#### Catalog Content Information
The content information of all catalogs is saved in the tools/cat_member.yaml file. When this data is imported into python it is represented as a dictionary of dictionaries, except for the very first entry in the file which contains a list of keys and names for each catalog. 

```
catalogs:                                          # first dictionary entry, information about catalogs
- - ua_ruhr                                        # start of the list, key of the first catalog
  - UA Ruhr                                        # name of the first catalog (english)
  - UA Ruhr                                        # name of the first catalog (german)
- - consultation                                   # key of the second catalog
  - UA Ruhr-Consultation                           # name of the second catalog (english)
  - UA Ruhr-Beratung                               # name of the second catalog (german)
ua_ruhr/general/topic-research_question/title:     # second dictionary entry, question identifier `path`
  ua_ruhr: true                                    # first sub-dictionary entry, determines content of the catalog
  consultation: true                               # second sub-dictionary entry

```

For every question there has to be a corresponding entry in this file with information about **every catalog**. Otherwise the python script will throw a key error. However, this file does **not** need to be sorted in any way, except for the listed information at the top. 

#### Automatic Generation
The file tools/automatic_catalog_creation.py will use the provided information above to generate all catalogs and saves them with their respective names at the rdmorganiser/questions/ directory. The script uses **python 3.X** syntax and can be run simply from the command line via `python automatic_catalog_creation.py`.

Here are some important assumptions and choices made by the script.

- two external libraries are installed on the system the script is supposed to run on
  - a) [LXML](https://lxml.de/)
  - b) [PyYAML](https://pyyaml.org/)
- the provided information is in the same directory as the script
- there is an existing output directory relative to the script in  ../rdmorganiser/questions/
- for every question in all_questions.xml there is an entry in cat_member.yaml
- there is no sorting of questions needed in either of the above-mentioned files
- there are only unique paths and URI values in both files
- each entry for a question in the yaml file has information about **all** catalogs that are mentioned at the top of the file
- both files are valid XML and YAML, respectively
- the only namespace is "http://purl.org/dc/elements/1.1/"
- the script will **overwrite** every existing catalog in the output directory that matches a catalog name


A detailed explanation about how these files work can be found in [the wiki of this repository](https://github.com/FDM-UARuhr/rdmo-catalog-uaruhr/wiki/UA-Ruhr-Catalog-Creation).
