# Über den Forschungsdaten-Policy-Generator (FDNext)

# 1. Ziel und Zweck
Forschungsdaten-Policies für Forschungsprojekte finden – insbesondere in Verbundprojekten – immer größere Verbreitung. Um FDM-Verantwortliche in Forschungsprojekten bei der Erstellung einer projektinternen Forschungsdaten-Policy zu unterstützen, wurde der Forschungsdaten-Policy-Generator entwickelt. Der Forschungsdaten-Policy-Generator richtet sich in erster Linie an größere Forschungsprojekte und soll die Entwicklung einer projektinternen Forschungsdaten-Policy erleichtern. Er ist als Fragebogen mit vorgegebenen Antwortoptionen konzipiert und gibt basierend auf den gewählten Antwortoptionen Textbausteine als Formulierungshilfe aus. Der Fragebogen ist auf Deutsch und Englisch verfügbar.

# 2. FAQ
**Was ist der Forschungsdaten-Policy-Generator?**  
Der Forschungsdaten-Policy-Generator ist ein Werkzeug, das Sie bei der Erstellung einer Forschungsdaten-Policy für Ihr Forschungsprojekt unterstützt. Er generiert Textbausteine basierend auf Ihren Antworten im nachfolgenden Fragebogen.  
**Welche Vorteile bietet die Verwendung des Generators?**  
Die Nutzung des Generators vereinfacht den Prozess der Policy-Erstellung und stellt sicher, dass alle relevanten Themen abgedeckt werden.  
**Wie funktioniert die Beantwortung der Fragen im Generator?**  
Bei den meisten Fragen können Sie aus vorgegebenen Antworten auswählen und bei Bedarf individuelle Formulierungen hinzufügen. Einige Fragen erfordern nur Freitextantworten.  
**Kann ich die Bearbeitung unterbrechen und später fortsetzen?**  
Ja, es ist jederzeit möglich, die Bearbeitung zu unterbrechen und an späterer Stelle fortzusetzen. Auch können Sie über die Navigation zwischen Fragen hin- und herspringen und brauchen sie nicht in der vorgegebenen Reihenfolge zu bearbeiten.
**In welcher Form werden die Textbausteine ausgegeben?**    
Nachdem Sie den Fragebogen ausgefüllt haben, erhalten Sie eine Übersicht aller Fragen und Antworten, die Sie zur Formulierung Ihrer Policy nutzen können. Diese Übersicht kann in ein Textverarbeitungsprogramm exportiert und weiterbearbeitet werden.   
**Wie lange dauert es, den Fragebogen auszufüllen?**  
Erfahrungsgemäß dauert das Ausfüllen des Fragebogens zwischen 30 und 45 Minuten. Bitte beachten Sie, dass die Zeit für ggf. vorgelagerte Abstimmungsprozesse im Team nicht inbegriffen ist.  
**Muss ich alle Fragen im Fragebogen beantworten?**  
Nein, alle Fragen sind optional. Sie brauchen nur diejenigen beantworten, die für Ihr Projekt relevant sind.  
**Wo finde ich Beispiele für Forschungsdaten-Policies?**   
Sie können Beispiele für Forschungsdaten-Policies auf [forschungsdaten.org](https://www.forschungsdaten.org/index.php/Data_Policies) finden.  
**Gibt es weitere Hilfestellungen zur Erstellung einer Forschungsdaten-Policy?**  
Ja, in der Publikation ["Forschungsdaten-Policies für Forschungsprojekte: ein strukturierter Leitfaden"](http://dx.doi.org/10.14279/depositonce-16196) finden Sie zusätzliche Hinweise zur Erstellung einer projektinternen Forschungsdaten-Policy.  
**Zu welchem Zeitpunkt der Projektlaufzeit sollte das Tool verwendet werden?**  
Wir empfehlen, direkt zu Projektbeginn eine Policy mit unserem Tool zu erstellen, damit Sie sich im Team von Anfang an auf gemeinsame Ziele festlegen und genügend Zeit für die notwendigen Abstimmungsprozesse haben.  

## 3. Einrichtung des Fragenkatalogs
Der Fragenkatalog zur Erstellung einer Projekt-Forschungsdaten-Policy wird über den Import der Datei fdnext_template.xml in RDMO eingebunden. Das Template wurde auf einer RDMO Version 2.2.2 erstellt und als "XML (full)" Katalog exportiert. Für den Import müssen Sie neben dem XML-Dokument nichts weiter importieren, aber ggf. kann es zu Importproblemen bei älteren Versionen von RDMO kommen. In diesem Fall kontaktieren Sie bitte den Administrator Ihrer eigenen RDMO-Instanz. 

# 4. Überblick über die Struktur des Fragenkatalogs und die verwendeten Attribute und Optionen.

## Allgemeine Hinweise / General information
### Einführung
#### Gelesen und verstanden
> Attribut: https://fdm.ub.tu-berlin.de/domain/fdnext/domain/yesno  
> Widget-Typ: Ja/Nein

## Präambel
### Beschreibung des Forschungsprojekts
#### Kurzbeschreibung
> Attribut: https://fdm.ub.tu-berlin.de/domain/fdnext/description/description  
> Widget-Typ: Textfeld

### Definitionen
#### Folgende zentrale Begriffe sollen definiert werden:
> Attribut: https://fdm.ub.tu-berlin.de/domain/fdnext/definitions/definitions  
> Widget-Typ: Ankreuzfelder  
> Optionenset: https://fdm.ub.tu-berlin.de/options/definitions  

#### Weitere für das Projekt relevante Definitionen:
> Attribut: https://fdm.ub.tu-berlin.de/domain/fdnext/definitions/definitions01   
> Widget-Typ: Textfeld  

### Ziele der Policy
#### Mit der Forschungsdatenpolicy werden für das Projekt folgende Ziele verfolgt:
> Attribut: https://fdm.ub.tu-berlin.de/domain/fdnext/goals/goals  
> Widget-Typ: Ankreuzfelder  
> Optionenset: https://fdm.ub.tu-berlin.de/options/fdnext-goals  

## Geltungsbereich
### Personenkreis und Forschungsdaten
#### Die folgenden zwei Fragen verfügen über keinen Fragetext, da diese den Leseflusses der Textbausteine stören würden. Alle notwendigen Informationen zu der Frage finden sich im Hilfetext.
> Attribut: https://fdm.ub.tu-berlin.de/domain/fdnext/scope/persons  
> Widget-Typ: Ankreuzfelder  
> Optionenset: https://fdm.ub.tu-berlin.de/options/persons  

> Attribut: https://fdm.ub.tu-berlin.de/domain/fdnext/scope/data  
> Widget-Typ: Ankreuzfelder  
> Optionenset: https://fdm.ub.tu-berlin.de/domain/fdnext/scope/data  

## Rechtliche Aspekte
### Gesetze und Richtlinien
Neben dem Urheberrecht spielen folgende Gesetze, die den Umgang mit Forschungsdaten betreffen, im Projekt eine Rolle:
> Attribut: https://fdm.ub.tu-berlin.de/domain/fdnext/legal/law  
> Widget-Typ: Ankreuzfelder  
> Optionenset: https://fdm.ub.tu-berlin.de/options/law  

#### Der urheberrechtskonforme Umgang mit Forschungsdaten wird insbesondere durch folgende Maßnahmen gewährleistet:
> Attribut: https://fdm.ub.tu-berlin.de/domain/fdnext/legal/lawm  
> Widget-Typ: Ankreuzfelder  
> Optionenset: https://fdm.ub.tu-berlin.de/options/lawm  

#### Der datenschutzkonforme Umgang mit Forschungsdaten wird insbesondere durch folgende Maßnahmen gewährleistet:
> Attribut: https://rdmorganiser.github.io/terms/domain/project/legal_aspects/ipr  
> Widget-Typ: Ankreuzfelder  
> Optionenset: https://fdm.ub.tu-berlin.de/options/data-protection  

#### Darüber hinaus sind im Umgang mit den Forschungsdaten neben dem Kodex zur Sicherung guter wissenschaftlicher Praxis der DFG im Projekt folgende Richtlinien relevant:
> Attribut: https://rdmorganiser.github.io/terms/domain/project/legal_aspects  
> Widget-Typ: Ankreuzfelder  
> Optionenset: https://fdm.ub.tu-berlin.de/options/guidelines  

## Verantwortlichkeit
### Zuständigkeit für die Umsetzung der Policy
Für die Umsetzung der in der Policy formulierten Grundsätze sind die folgenden Personen zuständig:
> Attribut: https://rdmorganiser.github.io/terms/domain/project/data_management/name  
> Widget-Typ: Ankreuzfelder  
> Optionenset: https://fdm.ub.tu-berlin.de/options/responsibility  

## Umgang mit Forschungsdaten
### Speicherung und Datenorganisation
#### Es werden folgende Absprachen bezüglich der Speicherung von Forschungsdaten getroffen:
> Attribut: https://rdmorganiser.github.io/terms/domain/project/dataset/id  
> Widget-Typ: Ankreuzfelder  
> Optionenset: https://fdm.ub.tu-berlin.de/options/storage  

#### Es bestehen folgende Festlegungen zum Back-Up der Daten:
> Attribut: https://rdmorganiser.github.io/terms/domain/project/dataset/data_security/backup_responsible/name  
> Widget-Typ: Ankreuzfelder  
> Optionenset: https://fdm.ub.tu-berlin.de/options/backup  

#### Es gelten folgende Zugriffsregelungen:
> Attribut: https://rdmorganiser.github.io/terms/domain/project/dataset/data_security/access_permissions  
> Widget-Typ: Ankreuzfelder  
> Optionenset: https://fdm.ub.tu-berlin.de/options/access  

#### Folgende Festlegungen wurden zur Benennung von Dateien und zur Datei- und Ordnerstruktur getroffen:
> Attribut: https://rdmorganiser.github.io/terms/domain/project/dataset/storage/naming_policy  
> Widget-Typ: Ankreuzfelder  
> Optionenset: https://fdm.ub.tu-berlin.de/options/backup  

### Datendokumentation
#### Die Forschungsdaten sollen in folgender Form dokumentiert werden:
> Attribut: https://rdmorganiser.github.io/terms/domain/project/dataset/metadata/creation  
> Widget-Typ: Ankreuzfelder  
> Optionenset: https://fdm.ub.tu-berlin.de/options/options/documentation  

### Archivierung
#### Die Forschungsdaten werden nach Ablauf des Projekts an folgenden Orten für zehn Jahre aufbewahrt:
> Attribut: https://rdmorganiser.github.io/terms/domain/project/dataset/preservation/repository  
> Widget-Typ: Ankreuzfelder  
> Optionenset: https://fdm.ub.tu-berlin.de/options/archive-repo  

### Veröffentlichung und Lizenzen
#### Folgende im Projekt entstandene Forschungsdaten werden öffentlich zur Verfügung gestellt:
> Attribut: https://rdmorganiser.github.io/terms/domain/project/dataset/sharing/yesno  
> Widget-Typ: Ankreuzfelder  
> Optionenset: https://fdm.ub.tu-berlin.de/options/publication  

#### Die im Projekt entstandenen Forschungsdaten sollen an folgender Stelle veröffentlicht werden:
> Attribut: https://rdmorganiser.github.io/terms/domain/project/dataset/sharing/repository  
> Widget-Typ: Ankreuzfelder  
> Optionenset: https://fdm.ub.tu-berlin.de/options/place  

#### Bezüglich der Lizenzierung bei der Veröffentlichung wurden folgende Absprachen getroffen:
> Attribut: https://rdmorganiser.github.io/terms/domain/project/dataset/sharing/conditions   
> Widget-Typ: Ankreuzfelder  
> Optionenset: https://fdm.ub.tu-berlin.de/options/license  

### Projektspezifische Angaben
#### [Die folgende Frage verfügen über keinen Fragetext, da diese den Leseflusses der Textbausteine stören würden. Alle notwendigen Informationen zu der Frage finden sich im Hilfetext.]
> Attribut: https://rdmorganiser.github.io/terms/domain/project/additional_rdm_policy/requirements  
> Widget-Typ: Textfeld  

## Verabschiedung und Gültigkeit
### Datum und Gremium
#### [Die folgende Frage verfügen über keinen Fragetext, da diese den Leseflusses der Textbausteine stören würden. Alle notwendigen Informationen zu der Frage finden sich im Hilfetext.]
> Attribut: https://rdmorganiser.github.io/terms/domain/project/dmp/dmp_date  
> Widget-Typ: Textfeld  

## Abschließende Hinweise
### Hinweise
#### Gelesen und verstanden
> Attribut: https://fdm.ub.tu-berlin.de/domain/fdnext/domain/yesno  
> Widget-Typ: Ja/Nein
