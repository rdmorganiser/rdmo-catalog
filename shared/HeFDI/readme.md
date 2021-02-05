# Über den HeFDI-RDMO-Fragenkatalog
## Ziel und Zweck
Der HeFDI-RDMO-Fragenkatalog wurde vom HeFDI-Projekt [Hessische Forschungsdateninfrastrukturen](http://www.hefdi.de) entwickelt. Der Fragenkatalog dient den forschungsnahen Servicestellen für Forschungsdaten in HeFDI als strukturierter Interviewleitfaden, mit dem Belange und Bedarfe der Forschenden abgefragt werden können. Der Katalog ist so einsteigerfreundlich gehalten, dass er auch von Forschenden ohne tiefere FDM-Kenntnisse als Vorbereitung einer ausführlichen Beratung ausgefüllt werden kann. Alternativ kann der Katalog auch gemeinsam mit den Beratenden der Servicestellen ausgefüllt werden.  
Auf Grundlage der gegeben Antworten können die Servicestellen etwaige Handlungs-, Schulungs-, oder Informationsbedarfe erkennen und bedarfsgerecht beantworten.

Der Katalog besteht dazu aus einem übersichtlichen Set an Fragen mit umfangreichen Auswahloptionen, beispielsweise zu Dateiformaten. Bedingungen stellen sicher, dass Forschende nur die für sie relevanten Fragen beantworten müssen. Der Katalog ist auf Deutsch und Englisch verfügbar.
## Einrichtung des Fragenkatalogs
Als Voraussetzung müssen die vom RDMO-Projekt bereitgestellten Standard-Attribute und -Optionen in die eigene RDMO-Instanz importiert worden sein. Diese können unter https://github.com/rdmorganiser/rdmo-catalog/tree/master/rdmorganiser heruntergeladen werden.

Der HeFDI-Fragenkatalog benötigt darüber hinaus zusätzliche Attribute, Optionen und Bedingungen, die sich in den Dateien hefdi_template_domain.xml, hefdi_template_options.xml und hefdi_template_conditions.xml befinden.

Vor dem Import in RDMO müssen in der Datei hefdi_template_options.xml die Optionen des Optionensets "https<span></span>://hefdi.de/terms/options/hefdi_template_optionenset_fachbereich" angepasst werden. Die beiden Optionen des Optionensets beginnen in [Zeile 10](2_hefdi_template_options_1.4.xml#L10) bzw. [Zeile 21](2_hefdi_template_options_1.4.xml#L21) und enthalten die Beispiel-Fachbereiche “Law and Economics” sowie “History and Social Sciences” als Platzhalter. Diese müssen durch die gewünschten Organisationseinheiten der eigenen Institution ersetzt werden. Einträge für weitere Organisationseinheiten können angelegt werden, indem hinter die bestehenden Einträge weitere &lt;option>-Elemente mit demselben Aufbau eingefügt werden. Dabei ist zu beachten, dass für jede neue Option ein neuer Key vergeben werden muss:<br>
&lt;option
dc:uri=”[...]/hefdi_template_option_fachbereich2”>  
&nbsp; &lt;key>hefdi_template_option_fachbereich2&lt;/key>  
&nbsp; &lt;path>[...]/hefdi_template_option_fachbereich2&lt;/path>  
Alternativ können die Fachbereiche nach dem Import im Managementbereich unter “Options” angepasst und ergänzt werden.

Die oben genannten Dateien müssen vor dem Import des eigentlichen HeFDI-Fragenkatalogs (hefdi_template_questions.xml) in der folgenden Reihenfolge in die eigene RDMO-Instanz importiert werden:

1) [hefdi_template_domain.xml](1_hefdi_template_domain_1.4.xml)
2) [hefdi_template_options.xml](2_hefdi_template_options_1.4.xml)
3) [hefdi_template_conditions.xml](3_hefdi_template_conditions_1.4.xml)  

Erst danach kann der HeFDI-Fragenkatalog ([hefdi_template_questions.xml](4_hefdi_template_questions_1.4.xml)) störungsfrei importiert werden. Wird dieser versehentlich zuerst importiert, werden die Optionen und Bedingungen nicht verknüpft und der Katalog funktioniert nicht richtig. In diesem Fall hilft es, den HeFDI-Fragenkatalog zu löschen und, nach dem Import der oben genannten Dateien, neu zu importieren.

## Entstehung, Weiterverwendung, Kontakt
Der Katalog ist im Rahmen von [HeFDI (Hessische Forschungsdateninfrastrukturen)](https://www.hefdi.de) entstanden und wird bedarfsgerecht weiterentwickelt.
Der Katalog steht unter der Lizenz [CC0](https://creativecommons.org/publicdomain/zero/1.0/) zur freien Verfügung.
Bei Fragen und Anmerkungen wenden Sie sich bitte an rdmo@ulb.tu-darmstadt.de.

# Aufbau des Fragenkatalogs
## Allgemeine Angaben
#### Projektbeteiligte
*Handelt es sich bei Ihrem Forschungsvorhaben um ein Projekt mehrerer Beteiligter oder arbeiten Sie allein an einem Forschungsvorhaben?*
#### Allgemeine Angaben
*Name des Projekts*  
*Kennung des Projekts*  
*Verantwortliche/r Leiter/in*  
*Wissenschaftsbereich entsprechend der DFG-Fachsystematik*  
*Beteiligte Fachbereiche der Einrichtung*
#### Zuständigkeiten im Verlauf des Projekts
*Wer ist für das konkrete Forschungsdatenmanagement im Projektverlauf zuständig, insbesondere in Bezug auf die Speicherung und Sicherung der Forschungsdaten?*  
*Wer ist nach Abschluss des Projekts für die Daten zuständig?*
## Digitale Daten
#### Nutzung digitaler Daten
*Werden bereits existierende digitale Daten verwendet?*  
*Falls ja: Woher stammen die bereits existierenden Daten?*
#### Art der digitalen Daten
*Mit welchen digitalen Daten wird im Vorhaben gearbeitet?*
#### Dateiformate
*Welche Dateiformate werden verwendet? In einem weiteren Schritt können Sie die ausgewählten Dateiformate spezifizieren.*
#### Qualitätssicherung
*Nach welchen Vorgaben wird eine formale und inhaltliche Qualitätssicherung bei der Datenerhebung und -verarbeitung gewährleistet?*
#### Sicherung der Daten (Backup)
*Wie oft werden die erhobenen Daten gesichert (Backup)?*  
*Wie werden die erhobenen Daten gesichert (Backup)?*
#### Sicherung sensibler Daten
*Welche Maßnahmen werden zum Schutz sensibler Daten getroffen, z.B. personenbezogene Daten oder Daten aus Industriekooperationen?*
## Metadaten und Dokumentation
#### Dokumentation der Daten
*Wie werden die Daten im Forschungsvorhaben während der Planung, Erfassung, Verarbeitung und Auswertung dokumentiert?*  
*Wie werden die Metadaten erzeugt und gespeichert?*
## Sicherung, Archivierung und Veröffentlichung
#### Hard- und Software-Infrastruktur
*Auf welcher Hardware speichern Sie Ihre Daten und Metadaten im laufenden Vorhaben?*  
*Welche Software-Infrastruktur wird für das Daten- und Metadatenmanagement im laufenden Vorhaben genutzt?*
#### Speicherkapazitäten zur Durchführung
*Wieviel Speicherkapazitäten (in TB) werden voraussichtlich zur Durchführung des Vorhabens benötigt?*  
*Wieviel Speicherkapazitäten (in TB) werden voraussichtlich zur langfristigen Archivierung benötigt?*
#### Kriterien zur Archivierung
*Was sind die Kriterien für die Auswahl der zu archivierenden Forschungsdaten?*  
*Aus welchen Verarbeitungsstufen wählen Sie Daten zur Archivierung aus?*
#### Langzeitarchivierung
*Wo werden die Forschungsdaten langzeitarchiviert?*    
*Zu welchem Zeitpunkt werden die Forschungsdaten an ein sicheres Archiv zur Langzeitarchivierung verlagert?*
#### Urheberrechte
*Wer hat ggf. Urheberrechte an den im Projekt entstandenen Daten (falls diese dem Urheberrecht unterliegen)?*  
*Wer hat ggf. Nutzungsrechte an den im Projekt entstandenen Daten?*
#### Veröffentlichung
*Mit welchen externen Personen werden die Daten geteilt?*  
*Welche Metadaten werden mit den normalen Daten veröffentlicht, um diese auffindbar, interpretierbar und damit potentiell nachnutzbar zu machen?*
#### Kosten des Datenmanagements
*Wie hoch sind die geschätzten Kosten für das Datenmanagement und die Datenarchivierung und aus welchen Mitteln werden sie bezahlt?*
