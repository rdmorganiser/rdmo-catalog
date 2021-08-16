# Automatic comparison between catalog and view

### Background
`catalog_view_compare.R` creates a function to check which attributes appear in a specified view and catalog. Output is a csv table as follows:

| attribute | inView | inCatalog |
| --------- | ------ | --------- |
|           |        |           |

### Requirements
- installation of [R](https://cran.r-project.org) (version 4.0.2 or higher!)
- installation of R packages (see Step 3)

### Steps to reproduce
1. open commandline and change directory to the R bin folder
2. type `R`
3. if necessary: install required packages via `install.packages(c("yaml", "stringr", "XML"))`
4. change R working directory to your local path to rdmo-catalog-uaruhr with `setwd("path/to/rdmo-catalog-uaruhr")` (only forward slashes allowed)
5. execute script with `source("tools/catalog_view_compare.R")`
6. use function `compare(catalogName, viewName, path=getwd())`. A csv file will be saved in the working directory by default or in another directory specified by `path`. Prints "Done" when finished.
    - Examples:
        - `compare("proposal", "horizon2020")` (path not specified)
        - `compare("archive", "bielefeld", "C:/Users")` (path specified)
    - possible values for `catalogName`: file name of any xml file in folder [_rdmorganiser/questions_](https://github.com/FDM-UARuhr/rdmo-catalog-uaruhr/tree/master/rdmorganiser/questions) without extension e.g. archive, consultation, training, horizon2020 
    - possible values for `viewName`: either the name of a view which [rdmo.xml](https://github.com/FDM-UARuhr/rdmo-catalog-uaruhr/blob/master/rdmorganiser/views/rdmo.xml) contains (bielefeld, BMBF, citec, dmponline, dmptool, horizon2020, snf) or any other file name of an xml file in folder [_rdmorganiser/views_](https://github.com/FDM-UARuhr/rdmo-catalog-uaruhr/tree/master/rdmorganiser/views) without extension e.g. erc
