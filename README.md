RDMO catalog
============

This repository contains the content for [RDMO](https://github.com/rdmorganiser/rdmo) prepared by the [RDMO-Project](https://rdmorganiser.github.io).

To install the catalog into a freshly installed instance of RDMO, use

```
./manage.py import /path/to/options.xml
./manage.py import /path/to/conditions.xml
./manage.py import /path/to/domain.xml
./manage.py import /path/to/conditions.xml  # yes, again
./manage.py import /path/to/questions.xml
./manage.py import /path/to/views.xml
```

Reindent
--------

To indent the XML files use:

```bash
for f in *.xml; do xmllint --format $f > /tmp/$f; mv /tmp/$f $f; done
```
