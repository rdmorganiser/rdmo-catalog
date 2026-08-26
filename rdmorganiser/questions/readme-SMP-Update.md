# Updates from the project [MAUS](https://gepris.dfg.de/gepris/projekt/543616919)

## General remarks

- All additions / updates were made with the uri prefix: `https://rdmo.mpdl.mpg.de/terms`

## Updates to SMP catalog

- We are including:
    - our current version of the whole SMP catalog, i.e. an updated version of `questions-smp.xml` of this repo
    - a subset of `questions-smp.xml` (`questions-smp-subset.xml`) containing only updated or added catalog elements. We also included the parent element, so that it is clear where the updated / element belongs (for example, if a new question was added, we also included the new question's page)

- The main modifications were:
    - the structuring of the project contributors (before: Software Project Partner(s))
    - the inclusion of 2 option set providers: ORCID and ROR

## New Views

We added 4 views for the SMP catalog:
    - `view-smp-citation.xml`
    - `view-smp-codemeta.xml`
    - `view-smp-readme.xml`
    - `view-smp-report.xml`

The first 3 views are templates for the corresponding metadata files. `view-smp-report.xml` is a template that displays the answers in the SMP project as a continuous-text report.

## History

The SMP catalog was created at the Max Planck Digital Library (Max Planck Information and Technology) to support scientists developing research software to plan and document their work. This catalog was inspired by some documentation, specially https://www.software.ac.uk/resources/guides/software-management-plans and https://opencarp.org/about/software-management-plan.

The first version (2021-2023) was developed by Yves Vincent Grossmann, including a FAIR4RS view by Jan Matthiesen.  
The second version (2026) was developed within the DFG project MAUS (MAschinelle Unterstützung von Software-Management-Plänen), including 4 views (`view-smp-citation.xml`, `view-smp-codemeta.xml`, `view-smp-readme.xml`, `view-smp-report.xml`)
# Software Management Plan for Researchers

## Scope

The Software Management Plan for Researchers has been created at the Max Planck Digital Library (Max Planck Information and Technology) and included in the collection of the RDMO core catalogs.  
It was designed to support scientists developing research software to plan and document their work. Its structure was inspired by some documentation, specially https://www.software.ac.uk/resources/guides/software-management-plans and https://opencarp.org/about/software-management-plan.  
The first version (2021-2023) was developed by Yves Vincent Grossmann, with a contribution by Jan Matthiesen.  
The second version (2026) was developed within the DFG project [MAUS (MAschinelle Unterstützung von Software-Management-Plänen)](https://gepris.dfg.de/gepris/projekt/543616919).

## Content

The RDMO package for SMPs contains the following components:

- A question catalog: `questions-smp.xml`.
- 
    - a subset of `questions-smp.xml` (`questions-smp-subset.xml`) containing only updated or added catalog elements. We also included the parent element, so that it is clear where the updated / element belongs (for example, if a new question was added, we also included the new question's page)
    - 

- Attributes, conditions and optionsets already included in the core RDMO package.
- Five views (export templates):
    - `view-smp-citation.xml`
    - `view-smp-codemeta.xml`
    - `view-smp-readme.xml`
    - `view-smp-report.xml`
  - `view-FAIR4RS.xml`

The first 3 views generate the corresponding metadata files required by software repositories. `view-smp-report.xml` displays the answers in the SMP project as a continuous-text report. `view-FAIR4RS.xml` displays the answers structured according to the FAIR principles for research software.

## Dependencies

The 2026 version of the catalog contains a call to 2 option set providers - ORCID and ROR - which requires a previous installation of the following plugins: ....

If you want to automatically carry the exported metadata files to a software repository, you additional need the following plugins: .....
