# How to build the UA Ruhr-Training catalog

## Background
The UA Ruhr-Training catalog has a special structure based on the [Moodle course “Research Data Management”](https://moodle.ruhr-uni-bochum.de/m/enrol/index.php?id=19338). It covers a small range of questions so researchers can get familiar with RDMO while learning about research data management in the course. The catalog's structure has to be adjusted manually after the automatic catalog creation. Sections have to be renamed and questions reordered as described below.

## Steps to reproduce
1. Import automatically generated training.xml in RDMO.
2. Create four new sections in the following order: RDM/FDM, Organization/Organisation, Documentation/Dokumentation, Archiving and Publishing/Archiv und Publikation
3. Add questions to sections as shown in the table:

| RDM                                                  | Organization                                                                       | Documentation                                      | Archiving and Publishing                                                      |
|------------------------------------------------------|------------------------------------------------------------------------------------|----------------------------------------------------|-------------------------------------------------------------------------------|
| general/topic-research_question/title                | content-classification/data-dataset/description                                    | content-classification/data-reuse/scenario         | storage-and-long-term-preservation/long-term-preservation-datasets/repository |
| rdm/funding-funder/name                              | technical-classification/data-formats/format                                       | metadata-and-referencing/metadata-dataset/scope    | data-usage/data-sharing-and-re-use-interoperability/abstract                  |
| general/funding-funder/title                         | content-classification/data-reproducibility/reproducibility                        | metadata-and-referencing/metadata-dataset/abstract | data-usage/data-sharing-and-re-use-publication/yesno                          |
| general/other-requirements-yesno/abstract            | technical-classification/data-versioning/strategy                                  |                                                    |                                                                               |
| general/other-requirements-yesno/yesno               | data-usage/data-storage-and-security-data_security/backups                         |                                                    |                                                                               |
| general/other-requirements-requirements/requirements | metadata-and-referencing/structure-granularity-and-referencing-structure/structure |                                                    |                                                                               |
