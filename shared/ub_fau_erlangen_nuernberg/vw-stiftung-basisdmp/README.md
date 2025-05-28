# VW Stiftung  - DMP / VW Foundation  -  DMP

# Allgemeine Hinweise zur Verwendung des Fragenkatalogs VW Stiftung - DMP

Der Fragebogen wurde kooperativ von der UB der FAU Erlangen-Nürnberg und der UB der LMU München erstellt. Diese Vorlage orientiert sich an dem Basis-Datenmanagementplan der VW-Stiftung ([Basis-DMP](https://www.volkswagenstiftung.de/sites/default/files/documents/Basis-Datenmanagementplan.docx)). Die Fragen folgen nicht genau dem offiziellen VW-Plan. Der Hauptgrund dafür ist, dass der offizielle Plan verwandte FDM-Themen in verschiedene Abschnitte aufteilt. Nach dem Ausfüllen dieses Fragebogens kann die entsprechende Ansicht (view_vw_stiftung.xml) genutzt werden, um die Antworten entsprechend der offiziellen VW-Vorlage zu formatieren und zu exportieren. Die Fragen und Hilfetexte sind in deutscher und englischer Sprache verfügbar. Es wurden für diesen Katalog keine neuen Attribute erstellt. Es wurde eine neue Bedingung (https://fdm-bayern.org/eHumanities/conditions/data_reused) und eine neue Option (https://fdm-bayern.org/eHumanities/options/yes_restricted_no) eingeführt. 

## Besipielantworten
Um eine Vorstellung davon zu vermitteln, wie die Antworten aussehen könnten, wurde ein kurzer DMP für ein fiktives Projekt unter Verwendung dieser Vorlage erstellt. Die Vorlage kann auf der GitLab-Instanz der FAU Erlangen-Nürnberg abgerufen werden: https://gitlab.rrze.fau.de/cdi/labs/literacy/proposal-self-service/-/tree/main/RDMO/VW_Stiftung?ref_type=heads 

## Lizenz   
Der Fragenkatalog steht unter einer **CC0 Lizenz**, um eine möglichst einfache Wiederverwendung und Anpassung zu ermöglichen.


# Überblick über die Struktur des Fragenkatalogs und die verwendeten Attribute und Optionen. 

## Einleitung / Introduction

### Allgemeine Informationen / General information

Attribut: 

## Datenbeschreibung / Data description

### Datensätze / Datasets

Attribut: /project/dataset/id [Collection]

#### Um welche Art Datensatz handelt es sich? / What kind of dataset is it?

Attribut: /project/dataset/description

Widget: textarea

#### Wird der Datensatz selbst erzeugt oder nachgenutzt? / Is the dataset being created or reused?

Attribut: /project/dataset/origin

Widget: radio

Option: /options/dataset_origin_options

#### Sind diese Daten frei zugänglich oder sind hier Urheber- oder Persönlichkeitsrechte zu berücksichtigen? / Are these datasets freely accessible, or must copyright, data protection regulations, personality rights be considered?

Attribut: /project/legal_aspects

Widget: textarea

#### Falls Sie einen Link oder einen DOI zu dem Datensatz haben, etwa weil er in einem Repositorium liegt, geben Sie diesen hier an: / If you have a link to the dataset, e.g., in a repository, or a DOI, please give it here:

Attribut: /project/dataset/uri

Widget: text

Bedingung: https://fdm-bayern.org/eHumanities/conditions/data_reused

#### In welchem Rahmen liegt die tatsächliche oder erwartete Größe des Datensatzes? / What is the actual or expected size of the dataset?

Attribut: /project/dataset/size/volume

Widget: radio

Option: /options/dataset_size_options

### Datenorganisation und Metadaten / Data organisation and metadata

Attribut: /project/dataset/id [Collection]

#### In welchen Formaten liegen die Daten vor? / Which file formats are used?

Attribut: /project/dataset/format

Widget: textarea

#### Welche Informationen sind für Außenstehende notwendig, um die Daten zu verstehen (d.h. ihre Erhebung bzw. Entstehung, Analyse sowie die auf ihrer Basis gewonnenen Forschungsergebnisse nachvollziehen) und nachnutzen zu können? / Which information is necessary for other parties to understand the data (that is, to understand their collection or creation, analysis, and research results obtained on its basis) and to reuse it?

Attribut: /project/dataset/metadata/scope

Widget: checkbox

Option: /options/mandatory_metadata_options

#### Welche Standards, Ontologien, Klassifikationen etc. werden zur Beschreibung der Daten genutzt? / Which standards, ontologies, classifications etc. are used to describe the data?

Attribut: /project/dataset/metadata/standards

Widget: radio

Option: /options/metadata_standards

#### Bekommen die Daten einen persistenten Identifikator (PID), mit dem sie nachhaltig referenzierbar und zitierfähig sind? / Is a persistent identifier (PID) assigned to the data so that it can be referenced and cited in a sustainable manner?

Attribut: /project/dataset/pids/system

Widget: radio

Option: /options/pid_types

## Nutzungsrechte und Vereinbarungen / Rights to use and agreements

### Vereinbarungen im Projekt / Project-internal agreements

Attribut: /project/partner

#### Wie wird die Nutzung / Verwertung der Daten innerhalb des Projektes geregelt? / How does the project regulate access to and use of the data within the project?

Attribut: /project/partner/agreement

Widget: textarea

### Nachnutzung und Teilen der Daten / Reuse and data sharing

Attribut: /project/dataset/id [Collection]

#### Soll dieser Datensatz veröffentlicht oder geteilt werden? / Will this dataset be published or shared?

Attribut: /project/dataset/sharing/yesno

Widget: radio

Option: https://fdm-bayern.org/eHumanities/options/yes_restricted_no

#### Wenn nicht, begründen Sie dies bitte und unterscheiden Sie dabei zwischen rechtlichen und/oder vertraglichen Gründen und freiwilligen Einschränkungen. / If no, please explain why not. Please differentiate between legal and contractual reasons and voluntary restrictions.

Attribut: /project/dataset/sharing/explanation

Widget: textarea

#### Unter welcher Lizenz werden die Daten zur Verfügung gestellt? / Under what license will the data be made available?

Attribut: /project/dataset/sharing/sharing_license

Widget: checkbox

Option: /options/dataset_license_types

#### Wann wird der Datensatz mit der wissenschaftlichen Community geteilt? / When will the dataset be made available to the community?

Attribut: /project/dataset/data_publication_date

Widget: textarea

## Repositorien und Datenarchive / Repositories and data archives

### Datensicherung in Repositorien / Data storage in repositories

Attribut: /project/dataset/id [Collection]

#### Wo werden die Daten (einschließlich Metadaten, Dokumentation und ggf. relevantem Code bzw. relevanter Software) nach Projektende gespeichert bzw. archiviert? / Where will the data (including metadata, documentation and, if applicable, relevant code) be stored or archived after the end of the project?

Attribut: /project/dataset/preservation/repository

Widget: checkbox

Option: /options/preservation_repository_options

#### Wie lange sollen die Daten nach Projektende (nach)nutzbar sein? / How long is it intended that the data remains reusable.

Attribut: /project/dataset/preservation/reuse_duration

Widget: textarea

## Verantwortlichkeiten / Responsibilities

### Verantwortliche für Datenmanagement / Responsible persons for data management

Attribut: /project/partner/responsibilities

#### Wer ist im Projekt für den adäquaten Umgang mit den Forschungsdaten verantwortlich? Bitte Angabe der verantwortlichen Person. / Who is responsible for the appropriate handling of research data in the project? Please specify the person responsible.

Attribut: /project/support

Widget: textarea

