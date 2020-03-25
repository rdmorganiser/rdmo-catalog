# RDMO Catalog

The repository holds XML files that can be imported into RDMO. They contain different kinds of information like for example the domain model, question catalogs or optionsets.

The files that are officially provided by the RDMO project are in the `rdmorganiser` folder. We recommend to import these files to be able to make use of the official domain model, options, tasks and conditions. _Note that parts of these data are required to import user content because RDMO user's question catalogs may refer to parts of the official data_.

Content shared by RDMO Users can be found under `shared`. There may be multiple files in a folder like for example conditions, options and questions. Files in the same folder belong together. All of them should be imported. Please pay attention to the order in which you import files. Question catalogs referring to other content should be imported at last.

In `sanitizer` is a tool that is used to automatically replace the default URI in XML files. It is rather uninteresting for the average RDMO user but of relevance for the project and therefore included here.
