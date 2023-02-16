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

# Implementing
The catalogue uses some of the generic elements from RDMO. Therefore, all generic elements from "Conditions", "Domain", "Options" and "Questions" must already be implemented in advance.
To use this SMP, the additional SMP elements "Condition", "Domain" and "Questions" must then be imported into the own RDMO system. The respective order is documented in the [generic Readme file of the RDMO content](https://github.com/rdmorganiser/rdmo-catalog/tree/master/rdmorganiser#readme) and must be observed.

# Transferability
This catalogue introduces many custom attributes, as the generic RDMO attributes do not always cover the specific aspects of software. For this reason, the existing views in RDMO cannot be used for this catalogue, or only to a very limited extent.

# Use outside RDMO
Due to multiple requests, we have created a template on the SMP for use outside of RDMO. The Word document is freely writable, has a CC0 and is freely available via https://doi.org/10.17617/2.3481986 for your own re-use.

# FAIR4RS Viewer
A viewer for the presentation of the FAIR4RS principles is under development and will be made available soon.

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

### Infrastructure

To what extend will infrastructure resources be required?

Is there already existing infrastructure for the software development? Where is the infrastructure hosted?

Are there technical aspects where competences are (still) lacking, so that support would be helpful?

### Preservation

How long should the software remain usable?

Does this software have to be preserved for a longer term?

Where will the software be stored? Does the storage place have a clear preservation policy?

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