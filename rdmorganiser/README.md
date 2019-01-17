RDMO catalog
============

This repository contains the content for [RDMO](https://github.com/rdmorganiser/rdmo) prepared by the [RDMO-Project](https://rdmorganiser.github.io).

To install the catalog into a freshly installed instance of RDMO, use

```
./manage.py import /path/to/domain/rdmo.xml
./manage.py import /path/to/conditions/rdmo.xml  # yes, again
./manage.py import /path/to/options/rdmo.xml
./manage.py import /path/to/conditions/rdmo.xml  # yes, again
./manage.py import /path/to/questions/rdmo.xml
./manage.py import /path/to/tasks/rdmo.xml
./manage.py import /path/to/views/rdmo.xml
```

Use the same order when importing over the RDMO web interface.


Reindent
--------

To indent the XML files use:

```bash
for f in *.xml; do xmllint --format $f > /tmp/$f; mv /tmp/$f $f; done
```
