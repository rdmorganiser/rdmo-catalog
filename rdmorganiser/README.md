RDMO catalog
============

This repository contains the content for [RDMO](https://github.com/rdmorganiser/rdmo) prepared by the [RDMO-Project](https://rdmorganiser.github.io).

To install the catalog into a freshly installed instance of RDMO, use

```
./manage.py import /path/to/rdmo-domain.xml
./manage.py import /path/to/rdmo-conditions.xml
./manage.py import /path/to/rdmo-options.xml
./manage.py import /path/to/rdmo-conditions.xml  # yes, again
./manage.py import /path/to/rdmo-questions.xml
./manage.py import /path/to/rdmo-tasks.xml
./manage.py import /path/to/rdmo-views.xml
```

Use the same order when importing over the RDMO web interface.


Reindent
--------

To indent the XML files use:

```bash
for f in *.xml; do xmllint --format $f > /tmp/$f; mv /tmp/$f $f; done
```
