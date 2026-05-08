The script `templaterenderer.py' can be used to combine a django-template in plain xml and a xml-skeleton into one view-template that holds the skeleton and the (partially) html-encoded django-template which can be imported into RDMO.

just start the script from your command line:

```bash
python templaterenderer.py
```

It looks in the directory templaterenderer-djangotemplates for a pair of files. One ending with `.django`, one with `.xmlskeleton`. 

It exports a file into the shared folder.
