UA Ruhr catalogs
============

This repository contains the resaearch data management life cycle catalogs for [RDMO](https://github.com/rdmorganiser/rdmo) prepared by the work group FDM UA Ruhr.

To import the catalogs into a freshly installed instance of RDMO, use

```
./manage.py import /path/to/domain/rdmo.xml
./manage.py import /path/to/conditions/rdmo.xml
./manage.py import /path/to/options/rdmo.xml
./manage.py import /path/to/conditions/rdmo.xml  # yes, again
./manage.py import /path/to/questions/uaruhr.xml  # repeat this for every catalog file
./manage.py import /path/to/tasks/rdmo.xml
./manage.py import /path/to/views/rdmo.xml
```

Use the same order when importing over the RDMO web interface.

NOTE: The domain of rdmo-catalog-uaruhr `domain/rdmo.xml` is required to cover additional w.r.t. [https://github.com/rdmorganiser/rdmo-catalog](https://github.com/rdmorganiser/rdmo-catalog) the content of the present catalogs.

=======


Reindent
--------

To indent the XML files use:

```bash
for f in *.xml; do xmllint --format $f > /tmp/$f; mv /tmp/$f $f; done
```
