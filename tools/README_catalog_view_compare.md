# Automatic comparison between catalog and view

### Background
`auto_catalog_view.R` creates a function to check which attributes of the general UA Ruhr catalog appear in a specified view and catalog. Output is a csv table as follows:

| attribute | inView | inCatalog |
| --------- | ------ | --------- |
|           |        |           |

### Requirements
- installation of [R](https://cran.r-project.org) (version 4.0.2 or higher)
- installation of R packages (see Step 3)

### Steps to reproduce
1. open commandline and change directory to the R bin folder
2. type `R`
3. if necessary: install required packages via `install.packages(c("yaml", "stringr", "XML"))`
4. change R working directory with `setwd("path/to/rdmo_uaruhr/rdmo-catalog-rub/auto_catalog_view")` (only forward slashes!)
5. execute script with `source("auto_catalog_view.R")`
6. use function `compare(catalogName, viewName, path=getwd())`. A csv file will be saved in the working directory by default or in another directory specified by `path`. Prints "Done" when finished.
    - Examples:
        - `compare("proposal", "horizon2020")` (path not specified)
        - `compare("archive", "bielefeld", "C:/Users")` (path specified)
    - possible values for `catalogName`: archive, consultation, dcc, fhpshort, horizon2020, proposal, rdmo, snf, ua_ruhr
    - possible values for `viewName`: bielefeld, BMBF, citec, dmponline, dmptool, erc, horizon2020, snf

### Files in project folder
- `auto_catalog_view.R`: R script which creates function to compare catalog and view
- `views\demo-views.xml`: all views exported from rdmo-demo
- `questions`: contains all catalogs as single xml files, originates from project on [Github](https://github.com/FDM-UARuhr/rdmo-catalog-uaruhr/tree/master/rdmorganiser/questions)
- `domain\rdmo.xml`: contains all attributes, originates from project on [Github](https://github.com/FDM-UARuhr/rdmo-catalog-uaruhr/tree/master/rdmorganiser/domain)
