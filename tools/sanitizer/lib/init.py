import os
import re
import sys
from os.path import join as pj

from lib.util import detect_xml_files, get_uris_from_file, mkdir


class Init():
    def __init__(self, dirs):
        self.dirs = dirs
        self.check_dirs()
        self.shared_xmls = detect_xml_files(self.dirs["shared"])
        self.rdmo_xmls = detect_xml_files(self.dirs["rdmo"])
        self.detect_rdmos_uris()

    def check_dirs(self):
        mkdir(self.dirs["temp"])
        for key in self.dirs:
            val = self.dirs[key]
            if os.path.isdir(val) is False:
                print('Folder config seems to be wrong. Immediate exit.')
                sys.exit(1)

    def detect_rdmos_uris(self):
        self.rdmo_uris = []
        for fil in self.rdmo_xmls:
            self.rdmo_uris.extend(
                get_uris_from_file(fil, 'rdmorganiser.github.io')
            )

    def output_filename(self, filename):
        folder = re.search('shared.*(?=/)', filename).group(0)
        shortname = re.search('[^/]+$', filename).group(0)
        return pj(self.dirs["temp"], folder), shortname
