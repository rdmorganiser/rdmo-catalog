# Preface
This questionnaire was developed by the [Max Planck Digital Library](https://www.mpdl.mpg.de) in the Collections area in late summer and autumn 2022. It can be used to create a software management plan in RDMO. Of course, we are always happy to receive feedback: rdmo@mpdl.mpg.de.

The catalogue is available under the CC0 licence (https://creativecommons.org/share-your-work/public-domain/cc0/), so that it can be freely (re)used. Changes and adaptations by the RDMO community are of course welcome and can easily be made via GitHub.

# General
This RDMO catalogue supports the writing of a Software Management Plan. This questionnaire was developed by the Max Planck Digital Library in the Collections area in late summer and autumn 2022. It can be used to create a software management plan in RDMO.
A software management plan (SMP) can help significantly with design, implementation and long-term availability. The essential advantage of an SMP filled out in advance is the explicit handling of the emerging research software with documented information. At the same time, it also makes it clearer which topics (fields) have not yet been solved or covered.

# Development
This catalogue was developed through many conversations and iterations. It represents an attempt or approximation of what a Software Management Plan could possibly be. The main focus from our side was on added value for scientists who write software for their research themselves, but have not learned how to do this or have learned it only a little. At the same time, such an SMP can also be helpful in advising information and infrastructure experts.

Furthermore, this SMP template was inspired by some documentations, specially:
* https://www.software.ac.uk/resources/guides/software-management-plans
* https://opencarp.org/about/software-management-plan
* https://zenodo.org/record/7248877
* https://biohackrxiv.org/k8znb/

# Versions of the SMP Catalogue
| Version Number | Release Date | Description |
| -------------- | ------------ | ----------- |
| 1.0 | 5th December 2022  | Initialisation   |
| 1.1 | 27th February 2023 | Minor adjustments to help texts and some widget types of questions|
| 2.0 | 18th August 2023   | a) Addition of a question regarding Qualifty References (reference to FAIR4RS I2 and R2); b) adjustments to questions and help texts for the FAIR4RS viewer; c) minor adjustments to help texts thanks to feedback; d) broken links repair + Thanks a lot for the feedback by the RDMO Community!|
| 3.0 | 29th November 2023 | Implementing application classes and structure the appearence of different question after the DLR Research Software Guidelines (https://doi.org/10.5281/zenodo.1344612). This work was done within the NFDI4DataScience miniHackathons on maSMPs in 2023 at the ZB Med, see https://doi.org/10.5281/zenodo.10374839.|

# Implementing
The catalogue uses the generic elements from RDMO. Therefore, all generic elements from "Conditions", "Domain", "Options" and "Questions" must already be implemented in advance. The respective order is documented in the [generic Readme file of the RDMO content](/README.md) and must be observed.

# Transferability
This catalogue introduces many custom attributes, as the generic RDMO attributes do not always cover the specific aspects of software. For this reason, the existing views in RDMO cannot be used for this catalogue, or only to a very limited extent.

# Use outside RDMO
Due to multiple requests, we have created a standalone SMP template for use outside of RDMO. The Word document is freely available under a CC0 license via https://doi.org/10.17617/2.3481986 (direct link to the docx file: https://hdl.handle.net/21.11116/0000-000C-1076-D) for your own re-use.

# Metadata crosswalk to the maSMP ontology
The attributes we defined for a structured SMP have been aligned to the recommendations on machine-actionable software management plans (maSMPs) https://doi.org/10.5281/zenodo.7806638 being developed in the German SMP community. A metadata crosswalk document is published on https://doi.org/10.5281/zenodo.10275895. More SMP metadata fields for this usage are available within https://github.com/zbmed-semtec/maSMPs and https://discovery.biothings.io/ns/maSMP.

# FAIR4RS Viewer
A viewer for the presentation of the FAIR4RS principles is available under views. Using the Viewer only makes sense in combination with the SMP catalogue. With other RDMO catalogue this special viewer with focus on research software is not helpful. For more information, see the corresponding readme at the Viewer.

# Talks on the Topic
There were also some presentations on the development of this catalogue by the Max Planck Digital Library. See, for example, at the E-Science Days 2023 in Heidelberg: https://hdl.handle.net/21.11116/0000-000C-B40F-9.

# Feedback
Of course, we are always happy to receive feedback: rdmo@mpdl.mpg.de.

# Selection of Questions used for the SMP

## General
### Topic

What is the title of the software project?

Which research field(s) does this software belong to?

What is the intended use of the software? How will your software contribute to research?

Are your sure that no suitable software exists with the functionality your are planning?

### Software Project Partner(s)

Who are the project participants that deal with this software?

Where do the (financial/personnel) resources come from?

Is there or will there be specific funding for the software development?


### Software Project Schedule

When does the software project start?

When does the software project end?

### Software Project Management

Which software development process is defined? How will process roles be assigned?

How do you track the different tasks and use cases?

Will there be a specification document (briefly) outlining the most important requirements?

### Software Development Requirements

Are there institutional requirements for software development?

Are there requirements regarding the software development form other parties?

## Technical

### Code

Which programming language(s) do you plan to use?

Which technology or process is used for versioning?

### Third Party Components and Libraries

Which external software components will be used? What dependencies on software libraries do exist? How do you document this?

What licences are on the third-party software components?

What is the process to keep track of the external software components? Can critical dependencies be eliminated or mitigated?

Do you plan to use third party web services?

 Does the software refer to other software projects or objects?

### Infrastructure

To what extend will infrastructure resources be required?

Is there already existing infrastructure for the software development? Where is the infrastructure hosted?

Are there technical aspects where competences are (still) lacking, so that support would be helpful?

### Preservation

How long should the software remain usable?

Does this software have to be preserved for a longer term?

### Security

Which measures or provisions are in place to ensure software security?

What Measures Do You Take to Minimise Risks in Relation to Software Development?

## Quality Assurance

### Governance and Defined Processes

Do you have a governance model for the software development?

Do you apply specific coding standards? How do you take care about code quality control?

### Documentation

How is software documentation created?

Where will the documentation be stored or made available? Which language will be used?

### Testing

Which software test strategy are you going to follow? Which types of tests are planned for the project?

How is testing and test documentation organised?

## Release and Publish

### Releasing

Are there defined release processes for the software?

What is the decision process for releasing? How often will a software version be released?

Where will the software be stored? Does the storage place have a clear preservation policy?

### Publicly Availability

Will this software be publicly available?

In which repository or archive will the software be held? How easy can it be found?

Will users have the possibility to contribute to your software?

Is (Open) Peer Review planned for the software?

### Metadata

How do you assign metadata for your software?

Do you give a persistent identifier for you software?

### Support

Do you plan to give support or help to re-users of your software?

How do you organise the support and feedback process with other users?

Does your Software Management Plan relate to other Software/Data Management Plans?

Do you intend to make your software management plan publicly available (later)?

## Legal and Ethics

### Intellectual Property Rights

What is the legal ownership of the software?

Does the project use and/or produce software that is protected by third party intellectual or industrial property rights?
### License

Under what kind of license(s) will the software be published?

### Dual Use

Can the software also be used for military purposes?
