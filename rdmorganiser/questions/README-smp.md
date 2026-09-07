# Software Management Plan for Researchers

## Scope / Preface / General

This RDMO catalogue supports the writing of a Software Management Plan. This questionnaire was developed by the Max Planck Digital Library in the Collections area in late summer and autumn 2022. It can be used to create a software management plan in RDMO.  
A software management plan (SMP) can help significantly with design, implementation and long-term availability. The essential advantage of an SMP filled out in advance is the explicit handling of the emerging research software with documented information. At the same time, it also makes it clearer which topics (fields) have not yet been solved or covered.





The Software Management Plan for Researchers has been created at the Max Planck Digital Library (Max Planck Information and Technology).  
It was designed to support scientists developing research software to plan and document their work. Its structure was inspired by some documentation, specially https://www.software.ac.uk/resources/guides/software-management-plans and https://opencarp.org/about/software-management-plan.  

It has been included in the collection of the RDMO core catalogs. The catalogue is available under the CC0 licence (https://creativecommons.org/share-your-work/public-domain/cc0/), so that it can be freely (re)used. Changes and adaptations by the RDMO community are of course welcome and can easily be made via GitHub.

The first version (2021-2023) was developed by Yves Vincent Grossmann, including a FAIR4RS view by Jan Matthiesen.  
The second version (2026) was developed within the DFG project [MAUS (MAschinelle Unterstützung von Software-Management-Plänen)](https://gepris.dfg.de/gepris/projekt/543616919), including 4 views (`view-smp-citation.xml`, `view-smp-codemeta.xml`, `view-smp-readme.xml`, `view-smp-report.xml`)







## Content

The RDMO package for SMPs contains the following components:

- A question catalog: `questions-smp.xml`.
- ~a subset of `questions-smp.xml` (`questions-smp-subset.xml`) containing only updated or added catalog elements. We also included the parent element, so that it is clear where the updated / element belongs (for example, if a new question was added, we also included the new question's page)~

- Attributes, conditions and optionsets already included in the core RDMO package.
- Five views (export templates):
    - `view-smp-citation.xml`
    - `view-smp-codemeta.xml`
    - `view-smp-readme.xml`
    - `view-smp-report.xml`
    - `view-FAIR4RS.xml`

The first 3 views generate the corresponding metadata files required by software repositories. `view-smp-report.xml` displays the answers in the SMP project as a continuous-text report. `view-FAIR4RS.xml` displays the answers structured according to the FAIR principles for research software.

## Dependencies

The 2026 version of the catalog contains a call to 2 option set providers - ORCID and ROR - which requires a previous installation of the following plugins:
- https://github.com/MPDL/rdmo-plugins-orcid -> the fork of https://github.com/rdmorganiser/rdmo-plugins-orcid adapted for the SMP catalog
- https://github.com/MPDL/rdmo-plugins-ror -> the fork of https://github.com/rdmorganiser/rdmo-plugins-ror adapted for the SMP catalog

If you want to automatically carry the exported metadata files to a software repository on GitHub or GitLab, you additionally need the following plugins:
- https://github.com/rdmorganiser/rdmo-plugins-github
- https://github.com/rdmorganiser/rdmo-plugins-gitlab

## Development

This catalogue was developed through many conversations and iterations. It represents an attempt or approximation of what a Software Management Plan could possibly be. The main focus from our side was on added value for scientists who write software for their research themselves, but have not learned how to do this or have learned it only a little. At the same time, such an SMP can also be helpful in advising information and infrastructure experts.

Furthermore, this SMP template was inspired by some documentations, specially:
* https://www.software.ac.uk/resources/guides/software-management-plans
* https://opencarp.org/about/software-management-plan
* https://zenodo.org/record/7248877
* https://biohackrxiv.org/k8znb/

## History

The SMP catalog was created at the Max Planck Digital Library (Max Planck Information and Technology) to support scientists developing research software to plan and document their work. This catalog was inspired by some documentation, specially https://www.software.ac.uk/resources/guides/software-management-plans and https://opencarp.org/about/software-management-plan.

The first version (2021-2023) was developed by Yves Vincent Grossmann, including a FAIR4RS view by Jan Matthiesen.  
The second version (2026) was developed within the DFG project [MAUS (MAschinelle Unterstützung von Software-Management-Plänen)](https://gepris.dfg.de/gepris/projekt/543616919), including 4 views (`view-smp-citation.xml`, `view-smp-codemeta.xml`, `view-smp-readme.xml`, `view-smp-report.xml`)

- The main modifications were:
    - the structuring of the project contributors (before: Software Project Partner(s))
    - the inclusion of 2 option set providers: ORCID and ROR

## Versions of the SMP Catalogue
| Version Number | Release Date | Description |
| -------------- | ------------ | ----------- |
| 1.0 | 2022-12-05 | Initialisation   |
| 1.1 | 2023-02-27 | Minor adjustments to help texts and some widget types of questions|
| 2.0 | 2023-08-18 | a) Addition of a question regarding Qualifty References (reference to FAIR4RS I2 and R2); b) adjustments to questions and help texts for the FAIR4RS viewer; c) minor adjustments to help texts thanks to feedback; d) broken links repair + Thanks a lot for the feedback by the RDMO Community!|
| 3.0 | 2023-11-29 | Implementing application classes and structure the appearence of different question after the DLR Research Software Guidelines (https://doi.org/10.5281/zenodo.1344612). This work was done within the NFDI4DataScience miniHackathons on maSMPs in 2023 at the ZB Med, see https://doi.org/10.5281/zenodo.10374839.|
| 4.0 | 2026-08-XX | New views; fine-grained description of contributors; integration of the ORCID plugin |

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
