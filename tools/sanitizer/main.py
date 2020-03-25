#!/usr/bin/python3

import os
import sys

from lib.sanitizer import sanitizer
from lib.util import util

if __name__ == '__main__':

    try:
        basedir = sys.argv[1]
    except IndexError:
        basedir = os.getcwd()

    utl = util(basedir)

    for filename in utl.xml_files:
        print('\nStart to process ' + filename)
        content = utl.read_xml(filename)
        san = sanitizer(content, filename)
        san.process()

        outfile = utl.output_filename(filename)
        utl.write_xml(san.content, outfile)
        print('Done.')
