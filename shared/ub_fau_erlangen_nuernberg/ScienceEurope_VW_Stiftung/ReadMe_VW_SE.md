# Dokumentation und Lizenzinformationen zum DMP-Fragebogen zur VW-Stiftung / Science Europe

## Update (04/2024)
Dieser Fragenkatalog basiert auf der obsoleten Vorlage der VW-Stiftung und ist veraltet. 

## Allgemeines (02/2022)
Der Fragebogen wurde ursprünglich für Projektanträge der VW-Stiftung erstellt, die für „datenintensive“ Projekte einen DMP verlangt, der im Wesentlichen deckungsgleich mit dem Science Europe 
Fragenkatalog ist. Der Fragenkatalog catalog_VW_SE.xml nutzt viele Elemente des Fragenkatalogs des RDMO-Projektes und steht wo möglich (siehe unten) wie dieser unter einer CC0 1.0 Universell-Lizenz.

Der Aufbau folgt eng dem Fragenkatalog ‘Practical Guide to the International Alignment of Research Data Management’ (Extended Edition) von Science Europe  (https://www.scienceeurope.org/media/4brkxxe5/se_rdm_practical_guide_extended_final.pdf, Seiten 17-25), der unter einer CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/) veröffentlicht wurde. Die englischen Fragentexte und Teile der für die Hilfestellung verwendeten Texte sind direkt aus dem „Guide“ übernommen. Dabei wurde die Einteilung, ob bestimmte Informationen in einer oder mehreren Fragen abgefragt werden, an verschiedenen Stellen angepasst, um zu komplexe bzw. ausführliche Fragestellungen innerhalb einer einzelnen RDMO-Frage zu vermeiden. Diese Fragestellungen wurden dann meist als Fragenset dargestellt. 

## Erweiterung der Domäne (12/2021)
Es werden diese zusätzlichen Attribute verwendet:
* project/dataset/documentation
* project/dataset/documentation/where
Diese Attribute können direkt aus der domain_VW_SE.xml importiert werden. Falls eine Erweiterung der Domäne nicht gewünscht ist, können die Fragen auch ungenutzte Attributen, die etwa dem RDMO-Standard-Attribut project/dataset untergeordnet sind, zugewiesen werden. 

Für einige Fragen werden RDMO-Standard-Attribute verwendet, deren Zweck nicht ganz deckungsgleich mit den im Original-RDMO-Fragenkatalog zugewiesenen Themen sind. Hier sind insbesondere zu nennen:
* project/dataset/data_security/security_measures
wird für die Antwort auf die Frage nach Datenschutzrisiken und dem Umgang damit verwendet.
* project/dataset/sensitive_data/other
wird für die Frage nach ethischen Belangen und Verhaltensregeln verwendet
* project/dataset/sharing/explanation
wird für die Fragen, ab wann die Daten mit anderen geteilt werden, verwendet 
* project/dataset/metadata/responsible_person
wird für die Frage nach der für das Datenmanagement im Projekt zuständigen Person verwendet (also nicht nur für Metadaten)

Dies kann in Ansichten zu unpassenden Zuordnungen führen. In dem Fall sollten die Attribute im Fragenkatalog angepasst werden.
