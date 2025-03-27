# About the research data policy generator (FDNext)

# 1. Aim and purpose
Research data policies for research projects are becoming increasingly widespread - especially in collaborative projects. The Research Data Policy Generator was developed to support those responsible for RDM in research projects in the creation of a project-internal research data policy. The Research Data Policy Generator is primarily aimed at larger research projects and is intended to facilitate the development of a project-internal research data policy. It is designed as a questionnaire with predefined answer options and provides text modules as a formulation aid based on the selected answer options. The questionnaire is available in German and English.

# 2. FAQ
**What is the Research Data Policy Generator?**
The Research Data Policy Generator is a tool that supports you in creating a research data policy for your research project. It generates text modules based on your answers in the following questionnaire.
**What are the advantages of using the generator?**
Using the generator simplifies the process of policy creation and ensures that all relevant topics are covered.
**How does answering the questions in the generator work?**
For most questions, you can choose from pre-set answers and add customised wording if needed. Some questions require free text answers.
**Can I interrupt the questionnaire and continue later?**
Yes, you can interrupt your work at any time and continue at a later point. You can also use the navigation to jump back and forth between questions and do not need to work on them in the given order.
**In what form are the text modules output?**
After you have completed the questionnaire, you will receive an overview of all questions and answers that you can use to formulate your policy. This overview can be exported to a text processing programme and further edited.
**How long does it take to complete the questionnaire?**
Experience shows that it takes between 30 and 45 minutes to complete the questionnaire. Please note that the time for any upstream coordination processes in the team is not included.
**Do I have to answer all the questions in the questionnaire?**
No, all questions are optional. You only need to answer those that are relevant to your project.
**Where can I find examples of research data policies?**
You can find examples of research data policies at [forschungsdaten.org](https://www.forschungsdaten.org/index.php/Data_Policies).
**Is there any further help for creating a research data policy?**
Yes, in the publication ["Forschungsdaten-Policies für Forschungsprojekte: ein strukturierter Leitfaden"](http://dx.doi.org/10.14279/depositonce-16196) you will find additional guidance on how to create a project-internal research data policy.
**At what point during the project should the tool be used?**
We recommend creating a policy with our tool right at the beginning of the project so that you can commit to common goals in the team right from the start and have enough time for the necessary coordination processes.
 
## 3. Setting up the questionnaire
The question catalog for creating a project research data policy can be integrated into RDMO by importing the fdnext_template.xml file. The template was created on an RDMO version 2.2.2 and exported as an “XML (full)” catalog. You do not need to import anything else besides the XML document for the import, but there may be import problems with older versions of RDMO. In this case, please contact the administrator of your own RDMO instance. 

# 4. Overview of the structure of the question catalogue and the attributes and options used 

## General information
### Einführung
#### Gelesen und verstanden
> Attribute: https://fdm.ub.tu-berlin.de/domain/fdnext/domain/yesno  
> Widget-type: Ja/Nein

## Präambel
### Description of the research project
#### Short description
> Attribute: https://fdm.ub.tu-berlin.de/domain/fdnext/description/description  
> Widget-Type: Textfeld

### Definitions
#### The following key terms are to be defined:
> Attribute: https://fdm.ub.tu-berlin.de/domain/fdnext/definitions/definitions  
> Widget-Type: Ankreuzfelder  
> Option set: https://fdm.ub.tu-berlin.de/options/definitions  

#### Other definitions relevant to the project:
> Attribute: https://fdm.ub.tu-berlin.de/domain/fdnext/definitions/definitions01   
> Widget-Type: Textfeld  

### Policy Objectives
#### The research data policy seeks to achieve the following goals for the project:
> Attribute: https://fdm.ub.tu-berlin.de/domain/fdnext/goals/goals  
> Widget-Type: Ankreuzfelder  
> Option set: https://fdm.ub.tu-berlin.de/options/fdnext-goals  

## Scope
### Persons and research data
#### The following two questions do not have a question text, as this would disrupt the flow of the text modules. All necessary information on the question can be found in the help text.
> Attribute: https://fdm.ub.tu-berlin.de/domain/fdnext/scope/persons  
> Widget-Type: Ankreuzfelder  
> Option set: https://fdm.ub.tu-berlin.de/options/persons  

> Attribute: https://fdm.ub.tu-berlin.de/domain/fdnext/scope/data  
> Widget-Type: Ankreuzfelder  
> Option set: https://fdm.ub.tu-berlin.de/domain/fdnext/scope/data  

## Legal Aspects
### Ensuring legal compliance
In addition to copyright, the following laws concerning the handling of research data play a role in the project:
> Attribute: https://fdm.ub.tu-berlin.de/domain/fdnext/legal/law  
> Widget-Type: Ankreuzfelder  
> Option set: https://fdm.ub.tu-berlin.de/options/law  

#### The handling of research data in compliance with copyright law is ensured in particular by the following measures:
> Attribute: https://fdm.ub.tu-berlin.de/domain/fdnext/legal/lawm  
> Widget-Type: Ankreuzfelder  
> Option set: https://fdm.ub.tu-berlin.de/options/lawm  

#### The handling of research data in compliance with data protection law is ensured in particular by the following measures:
> Attribute: https://rdmorganiser.github.io/terms/domain/project/legal_aspects/ipr  
> Widget-Type: Ankreuzfelder  
> Option set: https://fdm.ub.tu-berlin.de/options/data-protection  

#### Furthermore, in addition to the DFG's Guidelines for Safeguarding Good Research Practice, the following guidelines are relevant to the handling of research data in the project:
> Attribute: https://rdmorganiser.github.io/terms/domain/project/legal_aspects  
> Widget-Type: Ankreuzfelder  
> Option set: https://fdm.ub.tu-berlin.de/options/guidelines  

## Accountability
### Responsibility for implementing the policy
#### Responsibility for the practical implementation of the measures contained in the policy lies with the following person(s):
> Attribute: https://rdmorganiser.github.io/terms/domain/project/data_management/name  
> Widget-Type: Ankreuzfelder  
> Option set: https://fdm.ub.tu-berlin.de/options/responsibility  

## Managing research data
### Storage and data organization
#### The following agreements are made regarding data storage:
> Attribute: https://rdmorganiser.github.io/terms/domain/project/dataset/id  
> Widget-Type: Ankreuzfelder  
> Option set: https://fdm.ub.tu-berlin.de/options/storage  

#### The following specifications exist for the back-up of the data:
> Attribute: https://rdmorganiser.github.io/terms/domain/project/dataset/data_security/backup_responsible/name  
> Widget-Type: Ankreuzfelder  
> Option set: https://fdm.ub.tu-berlin.de/options/backup  

#### The following regulations apply regarding access:
> Attribute: https://rdmorganiser.github.io/terms/domain/project/dataset/data_security/access_permissions  
> Widget-Type: Ankreuzfelder  
> Option set: https://fdm.ub.tu-berlin.de/options/access  

#### The following specifications apply to naming files and to file and folder structures:
> Attribute: https://rdmorganiser.github.io/terms/domain/project/dataset/storage/naming_policy  
> Widget-Type: Ankreuzfelder  
> Option set: https://fdm.ub.tu-berlin.de/options/backup  

### Documenting data
#### Research data should be documented as follows: 
> Attribute: https://rdmorganiser.github.io/terms/domain/project/dataset/metadata/creation  
> Widget-Type: Ankreuzfelder  
> Option set: https://fdm.ub.tu-berlin.de/options/options/documentation  

### Archiving
#### By the end of the project, the research data will be stored for ten years at the following location:
> Attribute: https://rdmorganiser.github.io/terms/domain/project/dataset/preservation/repository  
> Widget-Type: Ankreuzfelder  
> Option set: https://fdm.ub.tu-berlin.de/options/archive-repo  

### Publishing and licenses
#### The following research data resulting from the project will be made publicly accessible:
> Attribute: https://rdmorganiser.github.io/terms/domain/project/dataset/sharing/yesno  
> Widget-Type: Ankreuzfelder  
> Option set: https://fdm.ub.tu-berlin.de/options/publication  

#### The research data generated in the project are to be published at the following location:
> Attribute: https://rdmorganiser.github.io/terms/domain/project/dataset/sharing/repository  
> Widget-Type: Ankreuzfelder  
> Option set: https://fdm.ub.tu-berlin.de/options/place  

#### The following agreements have been concluded regarding licensing upon publication:
> Attribute: https://rdmorganiser.github.io/terms/domain/project/dataset/sharing/conditions   
> Widget-Type: Ankreuzfelder  
> Option set: https://fdm.ub.tu-berlin.de/options/license  

### Project-specific information
#### [The following question does not have a question text, as this would disrupt the flow of the text modules. All necessary information on the question can be found in the help text.]
> Attribute: https://rdmorganiser.github.io/terms/domain/project/additional_rdm_policy/requirements  
> Widget-Type: Textfeld  

## Passage and Validity
### Date and approving body
#### [The following question does not have a question text, as this would disrupt the flow of the text modules. All necessary information on the question can be found in the help text.]
> Attribute: https://rdmorganiser.github.io/terms/domain/project/dmp/dmp_date  
> Widget-Type: Textfeld  

## Final notes
### Note
#### Read and understood
> Attribute: https://fdm.ub.tu-berlin.de/domain/fdnext/domain/yesno  
> Widget-Type: Ja/Nein




