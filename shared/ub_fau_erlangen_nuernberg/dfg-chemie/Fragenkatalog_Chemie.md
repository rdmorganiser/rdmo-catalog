# DFG-Anträge (Chemie) / DFG grants (chemistry)

[toc]

# Allgemeine Hinweise zur Verwendung des Fragenkatalogs DFG-Anträge (Chemie)

Der Fragebogen wurde im Rahmen des Projekts "eHumanities-interdisziplinär" (https://www.fdm-bayern.org/ehumanities-interdisziplinaer/) erstellt und nutzt Elemente des Fragenkatalogs des RDMO-Projektes. Der Fragenkatalog DFG-Anträge Chemie orientiert sich an der "Handlungsempfehlung zum Umgang mit Forschungsdaten" der Fachkollegien Chemie der Deutschen Forschungsgemeinschaft (DFG) (Link: https://www.dfg.de/download/pdf/foerderung/grundlagen_dfg_foerderung/forschungsdaten/handreichung_fachkollegien_chemie_forschungsdaten.pdf). Die Fragen und Hilfetexte sind in deutscher und englischer Sprache verfügbar. Es wurden für diesen Katalog keine neuen Attribute erstellt.

## Einsatz und Lizenz
Der Katalog wurde in erster Linie zur Vorbereitung von DFG-Anträgen im Fach Chemie erstellt. Die Fragen decken die Anforderungen / Themen ab, die im Antrag prinzipiell behandelt / erwähnt werden sollten. Forschende können die Fragen zur Selbstkontrolle des Antrags verwenden oder ihre knappen Antworten der Antragsberatung als Ausgangspunkt für einen Textvorschlag zur Verfügung stellen. 
    
Der Fragenkatalog steht unter einer **CC0 Lizenz**, um eine möglichst einfache Wiederverwendung und Anpassung zu ermöglichen.


# Überblick über die Struktur des Fragenkatalogs und die verwendeten Attribute und Optionen. 

## Allgemeine und projektübergreifende Aspekte / General or global topics

### Fachspezifische Regelungen / Subject Specific Requirements

> Attribut: /project
 
#### Haben Sie sich schon über die fachspezifischen Anforderungen informiert? / Have you already considered discipline-specific DFG requirements?

> Attribut: /project/research_field 

> Widget-Typ: Radio Buttons

> Optionen: /options/yes_no_not_yet

### Datenpolicy / Data policy

> Attribut: /project/funder

####  Werden für das Gesamtprojekt eigene Regeln zum Umgang mit Forschungsdaten vorgegeben? Wenn ja, welche Regeln sind das? Gibt es noch andere Richtlinien, die verbindlich sind? / Are there established rules for handling data within the project? If so, what are these rules? Are there other guidelines that will be followed?

> Attribut: /project/funder/rdm_policy

> Widget-Typ: Textfeld

### Kooperation mit Infrastruktureinrichtungen / Cooperation with infrastructure organizations

> Attribut: /project/partner [Collection]

#### Beschreiben Sie, wie die Infrastruktureinrichtung das Projekt beim Daten- und Wissensmanagement unterstützt: / Discuss how infrastructure facilities support data and knowledge management:

> Attribut: /project/external_services

> Widget-Typ: Textfeld

## Art und Umfang der Daten / Type and scope of data

### Beschreibung / Description

> Attribut: /project/dataset [Collection]

#### Welche Datensätze (oder Software) werden erzeugt, gesammelt oder wiederverwendet? / What research datasets (or software) will be created, collected or re-used in the project?

> Attribut: /project/dataset/description

> Widget-Typ: Textfeld

#### Welche Datenformate werden hierfür eingesetzt? / What data formats will be used for the data?

> Attribut: /project/dataset/format

> Widget-Typ: Textfeld

#### Was ist die erwartete Größe des Datensatzes? / What is the expected data volume?

> Attribut: /project/dataset/size/volume

> Widget-Typ: Textfeld

### Datenursprung / Data origin

> Attribut: /project/dataset [Collection]

#### Wird der Datensatz selbst erzeugt oder nachgenutzt? / Is the dataset being created or re-used?

> Attribut: /project/dataset/origin

> Widget-Typ: Radio Buttons

> Option: /options/dataset_origin_options

#### Falls nachgenutzt, wer hat den Datensatz erzeugt? / If re-used, who created the dataset?

> Attribut: /project/dataset/creator/name

> Widget-Typ: Textfeld

#### Falls nachgenutzt, wo befindet sich der Datensatz? / If re-used, where can the dataset be found?

> Attribut: /project/dataset/uri

> Widget-Typ: Text

## Dokumentation und Datenqualität / Documentation and data quality

### (Elektronisches) Laborbuch / (Electronic) Lab Notebook

> Attribut: /project

#### Wie wird eine Digitalisierung der Laborbücher erreicht? / How will you ensure a suitable digitisation of the laboratory notebooks?

> Attribut: /project/dataset/documentation/where

> Widget-Typ: Textfeld

### Dokumentation und Metadaten / Documentation and metadata

> Attribut: /project/dataset [Collection]

#### Wie wird der Datensatz und dessen Entstehung dokumentiert? Nutzen Sie eindeutige Identifikatoren für Messungen und Proben? / How will this dataset and its creation process be documented? Will you use unique identifiers for measurements and samples? 

> Attribut: /project/dataset/documentation

> Widget-Typ: Textfeld

#### Werden hierfür Metadaten erhoben? / What metadata will be created?

> Attribut: /project/dataset/metadata

> Widget-Typ: Textfeld

### Datenaufbereitung / Data handling

> Attribut:  /project/dataset [Collection]

#### Wie werden die Daten im Projekt aufbereitet? / How are the data processed / cleansed in the project?

> Attribut: /project/dataset/method

> Widget-Typ: Textfeld

#### Welche Software-Werkzeuge oder Datenbankanwendungen kommen dabei zum Einsatz? / Will you use specific software tools or databases for data cleansing / organisation?

> Attribut: /project/dataset/usage_technology

> Widget-Typ: Textfeld

### Qualitätssicherung / Quality assurance

> Attribut: /project/dataset

#### Beschreiben Sie die im Projekt eingesetzten Qualitätssicherungsmaßnahmen. / Please also discuss further quality assurance measures.

> Attribut: /project/dataset/quality_assurance

> Widget-Typ: Textfeld

## Speicherung und Sicherheit / Data storage and security

### Datensicherung / Data storage

> Attribut: /project/dataset [Collection]

#### Wie werden die Daten (einschließlich Metadaten, Dokumentation und ggf. relevantem Code bzw. relevanter Software) während des Projektes gesichert? / How will the data (including metadata, documentation and, if applicable, relevant code) be stored during the project?

> Attribut: /project/dataset/storage

> Widget-Typ: Ankreuzfelder

> Optionen: /options/preservation_repository_options

## Rechtliche Aspekte / Legal aspects

### Rechtliche Fragen und Auflagen / Legal issues and requirements

> Attribut: /project

#### Welche rechtlichen Verpflichtungen und Rahmenbedingungen gelten für das Projekt? / Which legal requirements and frameworks apply to the project?

> Attribut: /project/legal_aspects

> Widget-Typ: Textfeld

## Datenaustausch, Nachnutzbarkeit und langfristige Zugänglichkeit / Data sharing, re-use and long-term availability

### Auswahl der Daten zur dauerhaften Zugänglichkeit / Data selected for persistent access

> Attribut: /project/dataset [Collection]

#### Wird dieser Datensatz oder Teile davon dauerhaft zugänglich gemacht? / Will you provide persistent access to this dataset or to parts of it?

> Attribut: /project/dataset/sharing

> Widget-Typ: Textfeld

#### Wie werden die Daten zugänglich gemacht? / How will you make the data accessible?

> Attribut: /project/dataset/preservation/repository

> Widget-Typ: Textfeld

#### Ist das Repositorium zertifiziert? / Is the repository certified?

> Attribut: /project/dataset/preservation/certification

> Widget-Typ: Radio Buttons

> Option: /options/yes_no_not_yet

#### Werden im Projekt Lösungen zur Datentransformation auf bestimmte Standards oder Vergleichbares erarbeitet? / Do you develop solutions for data transformations to specific standards or similar approaches within the project?

> Attribut: /project/dataset/metadata/mappings

> Widget-Typ: Textfeld

## Verantwortlichkeiten und Ressourcen / Responsibilities and resources

### Verantwortliche für den Umgang mit Daten in dem Projekt / Persons responsible for data management in the project

> Attribut: /project

#### Wer ist im Projekt für den verantwortungsvollen Umgang mit Forschungsdaten zuständig? / Who is in charge of the responsible handling of research data in the project?

> Attribut: /project/preservation/responsible_person

> Widget-Typ: Textfeld

### Kosten / Costs

> Attribut: /project

#### Wie hoch sind die Kosten für das Datenmanagement im Projekt? / What are the costs associated with data management in the project?

> Attribut: /project/costs

> Widget-Typ: Textfeld




