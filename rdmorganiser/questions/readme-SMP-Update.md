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
