library(xml2); library(stringr); library(magrittr); library(tidyverse)
# setwd("C:/Users/MYPATH")    # enter path

rm(list=ls())
Dateiname <- "PRONTO/rdmo-questions.xml"

# Liste_fr <- Liste_it <- xml_find_all(read_xml(Dateiname),'.//*[@lang="de"]')
Dokument <- read_xml(Dateiname)
Liste_de <- xml_find_all(Dokument,'.//*[@lang="de"]')
Liste_en <- xml_find_all(Dokument,'.//*[@lang="en"]')
Liste_fr <- xml_find_all(Dokument,'.//*[@lang="fr"]')
Liste_it <- xml_find_all(Dokument,'.//*[@lang="it"]')

##########################
# nuova tabella traduzione

# Etiketten <- c(); for(x in Liste_de) Etiketten %<>% append(.,xml_text(xml_child(xml_parent(x),"key")))
DE <- data.frame( Pfad = str_replace(xml_path(Liste_de),"\\[\\d*\\]\\Z","") , de = xml_text(Liste_de) )
EN <- data.frame( Pfad = str_replace(xml_path(Liste_en),"\\[\\d*\\]\\Z","") , en = xml_text(Liste_en) )
FR <- data.frame( Pfad = str_replace(xml_path(Liste_fr),"\\[\\d*\\]\\Z","") , fr = xml_text(Liste_fr) )
IT <- data.frame( Pfad = str_replace(xml_path(Liste_it),"\\[\\d*\\]\\Z","") , it = xml_text(Liste_it) )

Übersetzung <- DE %>% 
  full_join(EN,"Pfad") %>% 
  full_join(FR,"Pfad") %>% 
  full_join(IT,"Pfad")

fix(Übersetzung)
write_tsv(Übersetzung,"Traduzione00.tsv",na="", quote_escape="none")

##########################
# aggiornamento traduzione

Übersetzung <- read_tsv("PRONTO/rdmo-questions-localisation.tsv") 
Übersetzung %<>% .[match(.$Pfad,DE$Pfad),]

xml_set_attr(Liste_de,"lang","de")
xml_set_attr(Liste_en,"lang","en")
xml_set_attr(Liste_fr,"lang","fr")
xml_set_attr(Liste_it,"lang","it")
xml_set_text(Liste_de,Übersetzung$de)
xml_set_text(Liste_en,Übersetzung$en)
xml_set_text(Liste_fr,Übersetzung$fr)
xml_set_text(Liste_it,Übersetzung$it)

xml_remove(xml_find_all(Dokument,'.//*[@lang="fr"]'))
xml_remove(xml_find_all(Dokument,'.//*[@lang="it"]'))
for(.k in seq_along(Liste_de)) xml_add_sibling( Liste_de[[.k]],Liste_it[[.k]] )
for(.k in seq_along(Liste_de)) xml_add_sibling( Liste_de[[.k]],Liste_fr[[.k]] )

write_xml(Dokument,"rdmo-questions.xml")
