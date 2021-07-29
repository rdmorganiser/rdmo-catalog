# load packages
library(yaml)
library(stringr)
library(XML)

compare <- function(catalogName, viewName, path=getwd()) {
  views <- xmlTreeParse("rdmorganiser/views/rdmo.xml") #import views
  for(i in 1:length(views$doc$children$rdmo)) { #find specified view
    rawView <- as.character(unlist(views$doc$children$rdmo[i]))
    if(str_detect(rawView[8], viewName)) {
      view <- paste0(rawView, collapse = "") #creates character with length=1 (important for later if-condition)
    }
  }
  catalog <- xmlTreeParse(paste0("rdmorganiser/questions/", catalogName, ".xml")) #import specified catalog
  catalog <- paste0(as.character(catalog), collapse = "") #creates character with length=1
  attributes <- xmlTreeParse("rdmorganiser/domain/rdmo.xml") #import attributes
  attribute <- character() 
  for(i in 1:length(attributes$doc$children$rdmo)) { #filter xml file to list all attributes
    a <- data.frame(unlist(attributes$doc$children$rdmo[i]$attribute[[3]]))
    attribute <- c(attribute, a[3,] )
  }
  catalog_view_table <- data.frame(attribute = attribute, inView = character(length=length(attribute)), inCatalog = character(length=length(attribute))) #create final table
  for(i in 1:nrow(catalog_view_table)) { #check which attributes appear in view
    if(str_detect(view, paste0("'", catalog_view_table$attribute[i], "'"))) {  #'' important to find the whole attribute
      catalog_view_table$inView[i] <- "yes"
    }
    else {
      catalog_view_table$inView[i] <- "no"
    } 
  } 
  for(i in 1:nrow(catalog_view_table)) { #check which attributes appear in catalog
    if(str_detect(catalog, paste0('"https://rdmorganiser.github.io/terms/domain/', catalog_view_table$attribute[i], '"'))) { #"" important to find the whole attribute
      catalog_view_table$inCatalog[i] <- "yes"
    }
    else {
      catalog_view_table$inCatalog[i] <- "no"
    } 
  }
  write.csv2(catalog_view_table, paste0(path, "/", catalogName, "-", viewName, ".csv"), row.names = F) #export dataframe as csv table (saved in working directory or specified path)
  print("Done")
}
