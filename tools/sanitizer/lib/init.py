import os
import re
import sys
from os.path import join as pj

from lib.util import detect_xml_files, get_uris_from_file, mkdir


class Init():
    def __init__(self, dirs, args):
        self.conf = {}
        self.conf['dirs'] = dirs
        self.conf['args'] = args
        self.check_dirs()
        self.shared_xmls = detect_xml_files(self.conf['dirs']['input'])
        self.rdmo_xmls = detect_xml_files(self.conf['dirs']['rdmo'])
        self.detect_rdmos_uris()

    def check_dirs(self):
        mkdir(self.conf['dirs']['output'])
        for key in self.conf['dirs']:
            val = self.conf['dirs'][key]
            if os.path.isdir(val) is False:
                print('\nFolder does not exist ' + val + '\nExit.\n')
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
        return pj(self.conf['dirs']['output'], folder), shortname
