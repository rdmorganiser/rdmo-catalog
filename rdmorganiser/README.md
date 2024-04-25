RDMO catalog
============

This folder contains the content for [RDMO](https://github.com/rdmorganiser/rdmo) curated by the [RDMO Consortium](https://rdmorganiser.github.io/Community/).

Install content
---------------

The RDMO content objects (catalogs, attributes, options, conditions, views, tasks) depend on each other, as shown in the [documentation](https://rdmo.readthedocs.io/en/latest/management/data-model.html).

In particular, the installation of question catalogues requires the newest version of attributes, optionsets and conditions. 

Therefore we suggest this sequence to install content in a RDMO instance:

```
./manage.py import /path/to/domain/rdmo.xml
./manage.py import /path/to/options/rdmo.xml
./manage.py import /path/to/conditions/rdmo.xml
./manage.py import /path/to/questions/<chosen_catalog>.xml
./manage.py import /path/to/tasks/<chosen_task>.xml
./manage.py import /path/to/views/<chosen_view>.xml
```

Use the same order when importing over the RDMO web interface.

Please note that the master branch will only work with the latest version of RDMO. If you need the xml files for an older version, please browse the releases or contact us.

Reindent
--------

To indent the XML files use:

```bash
for f in *.xml; do xmllint --format $f > /tmp/$f; mv /tmp/$f $f; done
```
