# European Research Council (ERC)

[toc]

# Allgemeine Hinweise zur Verwendung des Fragenkatalogs European Research Council (ERC)

Der Fragebogen wurde im Rahmen des Projekts "eHumanities-interdisziplinär" (https://www.fdm-bayern.org/ehumanities-interdisziplinaer/) erstellt und nutzt Elemente des Fragenkatalogs des RDMO-Projektes. Der Fragenkatalog European Research Council (ERC) orientiert sich am Template für den ERC Open Research Datenmanagementplan. Die Fragen und Hilfetexte sind in deutscher und englischer Sprache verfügbar. Es wurden für diesen Katalog keine neuen Attribute erstellt.

## Beispiel-DMP
Wir stellen ein kurzes DMP-Beispiel zur Verfügung, das mit Hilfe dieses Fragebogens erstellt wurde. Wenn Fragen von einer Beispielantwort profitieren, verlinken wir auf diesen. Der Beispiel-DMP ist kürzer als die üblichen ERC-DMPs: typische ERC-DMPs haben einen Umfang von 4-6 Seiten. Der DMP kann auf GitLab eingesehen werden: https://gitlab.lrz.de/UBderLMU-IT/FDM/rdmo-catalog/-/blob/master/Fragen/ERC/ERC_Example.md.

## Einsatz und Lizenz
Der Katalog wurde in erster Linie zur Vorbereitung von ERC-Anträgen erstellt. Die Fragen decken die Anforderungen / Themen ab, die im Antrag prinzipiell behandelt / erwähnt werden sollten. Forschende können die Fragen zur Selbstkontrolle des Antrags verwenden oder ihre knappen Antworten der Antragsberatung als Ausgangspunkt für einen Textvorschlag zur Verfügung stellen. 

Der Fragenkatalog steht unter einer **CC0 Lizenz**, um eine möglichst einfache Wiederverwendung und Anpassung zu ermöglichen.


# Überblick über die Struktur des Fragenkatalogs und die verwendeten Attribute und Optionen. 

## Allgemeines / General information

### Einführende Informationen / Introductory information

> Attribut: -

### Projektinformation / Project information

> Attribut: -

#### Wie lautet das Akronym des Projektes? / What is the project acronym?

> Attribut: /project/acronym

> Widget-Typ: Text

#### Wie lautet die Nummer des Projektes? / What is the project number?

> Attribut: /project/funder/grant_nr

> Widget-Typ: Text

## Zusammenfassung / Summary

### Beschreibung / Description

> Attribut: /project/dataset/id [collection]

#### Bitte beschreiben Sie den Datensatz knapp: / Give a short descriptive abstract for the dataset:

> Attribut: /project/dataset/description

> Widget-Typ: Textfeld

### Datenursprung / Data origin

> Attribut: /project/dataset/id [collection]

#### Wird der Datensatz selbst erzeugt oder nachgenutzt? / Is the dataset being created or reused?

> Attribut: /project/dataset/origin

> Widget-Typ: Radio Buttons

> Optionenset: /options/dataset_origin_options

#### Falls nachgenutzt, wer hat den Datensatz erzeugt? / If reused, who created the dataset?

> Attribut: /project/datset/creator/name

> Widget-Typ: Textfeld

#### Falls nachgenutzt, wo befindet sich der Datensatz? / If reused, where can the dataset be found?

> Attribut: /project/dataset/uri

> Widget-Typ: Text

### Datentyp / Data type

> Attribut: /project/dataset/id [collection]

#### In welchen Formaten liegen die Daten vor? / Which file formats are used?

> Attribut: /project/dataset/format

> Widget-Typ: Textfeld

> Optionenset: /options/file_type

#### Was ist die tatsächliche oder erwartete Größe des Datensatzes? / What is the actual or expected size of the dataset?

> Attribut: /project/dataset/size/volume

> Widget-Typ: Radio Buttons

> Optionenset: /options/dataset_size_options

### Sonstige Informationen / Further information

> Attribut: /project/dataset/id [collection]

#### Welche Maßnahmen zur Qualitätssicherung der Datenspeicherung und der Datenerhebung werden durchgeführt? / What measures will be taken to ensure integrity and quality of the data?

> Attribut: /project/dataset/quality_assurance

> Widget-Typ: Textfeld

#### Nehmen Sie externen Support (z.B. von anderen Institutionen) in Anspruch? / Do you use support from external institutions within the project?

> Attribut: /project/support

> Widget-Typ: Textfeld

## Auffindbarkeit der Daten / Making data findable

### Identifikatoren und Metadaten / Identifiers and metadata

> Attribut: /project/dataset/id [collection]

#### Wie wird der Datensatz und dessen Entstehung dokumentiert? Nutzen Sie eindeutige Identifikatoren für Messungen und Proben? / Will you use unique identifiers for measurements and samples? Are you assigning persistent identifiers to datasets at certain stages of processing?

> Attribut: /project/dataset/documentation

> Widget-Typ: Textfeld

#### Werden hierfür Metadaten erhoben? / What metadata will be created?

> Attribut: /project/dataset/metadata/creation

> Widget-Typ: Textfeld

## Daten offen zugänglich machen / Making Data Openly Accessible

### Datenzugang / Data sharing

> Attribut: /project/dataset/id [collection]

#### Werden die Daten anderen Forschungsprojekten zugänglich gemacht bzw. publiziert? / Will the data be made available to other research projects / published?

> Attribut: /project/dataset/sharing/explanation

> Widget-Typ: Textfeld

#### Falls Daten nicht veröffentlicht werden, begründen Sie dies bitte. Unterscheiden Sie zwischen rechtlichen oder vertraglichen Verpflichtungen und freiwilligen Einschränkungen. / If some data is not published, please explain your reasoning. Differentiate between legal and contractual reasons and voluntary restrictions.

> Attribut: /project/dataset/sharing/restrictions_explanation

> Widget-Typ: Textfeld

#### Wo werden die Daten (einschließlich Metadaten, Dokumentation und ggf. relevantem Code bzw. relevanter Software) nach Projektende publiziert bzw. archiviert? / Where will the data (including metadata, documentation and, if applicable, relevant code) be published or archived after the end of the project?

> Attribut: /project/dataset/preservation/repository [collection]

> Widget-Typ: Ankreuzfelder

> Optionenset: /options/preservation_repository_options

#### Wie wird die einfache Nachnutzbarkeit der Daten sichergestellt? / How will you insure that the data can be accessed and used?

> Attribut: /project/dataset/sharing/conditions

> Widget-Typ: Textfeld

## Interoperabilität der Daten / Making Data Interoperable

### Dokumentation und Metadaten / Documentation and metadata

> Attribut: /project/dataset/id [collection]

#### Welche Informationen sind für Außenstehende notwendig, um die Daten zu verstehen (d. h. ihre Erhebung bzw. Entstehung, Analyse sowie die auf ihrer Basis gewonnenen Forschungsergebnisse nachvollziehen) und nachnutzen zu können? / Which information is necessary and provided for other parties to understand the data (that is, to understand their collection or creation, analysis, and research results obtained on its basis) and to reuse it?

> Attribut: /project/dataset/metadata/scope [collection]

> Widget-Typ: Ankreuzfelder

> Optionenset: /options/mandatory_metadata_options

#### Welche Standards, Ontologien, Klassifikationen etc. werden zur Beschreibung der Daten genutzt? / Which standards, ontologies, classifications etc. are used to describe the data?

> Attribut: /project/dataset/metadata/standards

> Widget-Typ: Radiobutton

> Optionenset: /options/metadata_standards

## Nachnutzung der Daten / Increase Data Reuse

### Nachnutzung / Reuse

> Attribut: /project/dataset/id [collection]

#### Wie wird die langfristige Verfügbarkeit der Daten sichergestellt? / How will you ensure that the data is preserved?

> Attribut: /project/dataset/preservation

> Widget-Typ: Textfeld

#### Unter welcher Lizenz werden die Daten zur Verfügung gestellt? / Under what license will the data be made available?

> Attribut: /project/dataset/sharing/sharing_license [collection]

> Widget-Typ: Ankreuzfelder

> Optionenset: /options/dataset_license_types

#### Sollen die Daten erst nach Ablauf einer Sperrfrist zugänglich gemacht werden? / Shall there be an embargo period before the data are made available?

> Attribut: /project/dataset/preservation/embargo_period

> Widget-Typ: Textfeld

## Ressourcen und Datensicherheit / Allocation of Resources and Data Security

### Datenspeicherung / Storage

> Attribut: /project/dataset/id [collection]

#### Wo werden die Daten während des Projektes gespeichert? / Where will the data be stored during the project?

> Attribut: /project/dataset/storage

> Widget-Typ: Textfeld

#### Beschreiben Sie den Datentransfer zu Projektpartner:innen, falls vorhanden. / Describe the data transfer to project partners, if applicable.

> Attribut: /project/dataset/storage/organisation_policy

> Widget-Typ: Textfeld

### Datensicherheit / Data security

> Attribut: /project/dataset/id [collection]

#### Welche Maßnahmen zur Gewährleistung der Datensicherheit werden getroffen (z. B. Schutz vor unbefugtem Zugriff, Datenwiederherstellung, Übertragung sensibler Daten)? / Which measures or provisions are in place to ensure data security (e.g., protection against unauthorised access, data recovery, transfer of sensitive data)?

> Attribut: /project/dataset/data_security/security_measures [collection]

> Widget-Typ: Ankreuzfelder

> Optionenset: /options/security_measures

### Nachnutzungspotential und langfristige Aussichten / Potential reuse and long-term prospects

> Attribut: /project/dataset [collection]

#### Für welche Personen, Gruppen oder Institutionen könnte dieser Datensatz (für die Nachnutzung) von Interesse sein? Für welche Szenarien ist dies denkbar? Welche Konsequenzen hat das Nachnutzungspotential später für die Bereitstellung der Daten? / Which individuals, groups or institutions could be interested in re-using this dataset? What are possible scenarios? What consequences does the reuse potential have for the provision of the data later?

> Attribut: /project/dataset/reuse_scenario

> Widget-Typ: Textfeld

### Kosten / Costs

> Attribut: -

#### Wie hoch sind Personalaufwand und Sachkosten, die im Projekt im Rahmen des Datenmanagements entstehen (z.B. im Zusammenhang mit der Datendokumentation, der Erstellung der Metadaten, der Vergabe von persistenten Identifikatoren und der Langzeitcharchivierung)? / What personnel and material costs are associated with data management in the project (e.g., in terms of data documentation, creation of metadata, assignment of persistent identifiers, and long-term archiving)?

> Attribut: /project/costs

> Widget-Typ: Textfeld

#### Wie werden die Kosten für das Datenmanagement im Projekt aufgebracht? / How will the data management costs of the project be covered?

> Attribut: /project/costs/preservation/cover_how

> Widget-Typ: Textfeld
