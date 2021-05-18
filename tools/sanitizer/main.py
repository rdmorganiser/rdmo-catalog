#!/usr/bin/python3

import os
import re
from os.path import join as pj

from lib.init import Init
from lib.sanitize import Sanitize
from lib.util import read_xml, write_xml

if __name__ == '__main__':
    dirs = {}
    dirs['base'] = re.search(r'.*rdmo-catalog?', os.getcwd()).group(0)
    dirs['shared'] = pj(dirs['base'], 'shared')
    dirs['rdmo'] = pj(dirs['base'], 'rdmorganiser')
    dirs['temp'] = pj(dirs['base'], 'tmp')

    conf = Init(dirs)
    max = len(conf.shared_xmls)-1
    for idx, filename in enumerate(conf.shared_xmls):
        prog = '\n[' + str(idx) + '/' + str(max) + '] '
        print(prog + 'Start to process ' + filename)
        content = read_xml(filename)
        san = Sanitize(content, filename, conf.rdmo_uris)
        san.process()

        outfolder, outfile = conf.output_filename(filename)
        write_xml(san.content, outfolder, outfile)
        print('Done.')
