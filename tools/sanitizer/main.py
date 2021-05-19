#!/usr/bin/python3

import os
import re
from os.path import abspath
from os.path import join as pj

from lib.argparse import parse_args
from lib.init import Init
from lib.sanitize import Sanitize
from lib.util import read_xml, write_xml

if __name__ == '__main__':
    dirs = {}
    dirs['base'] = re.search(r'.*rdmo-catalog?', os.getcwd()).group(0)
    dirs['input'] = pj(dirs['base'], 'shared')
    dirs['rdmo'] = pj(dirs['base'], 'rdmorganiser')
    dirs['output'] = pj(dirs['base'], 'tmp')

    args = parse_args(dirs)
    dirs['input'] = abspath(args.input_folder)
    dirs['output'] = abspath(args.output_folder)

    conf = Init(dirs, args)

    max = len(conf.shared_xmls)-1
    for idx, filename in enumerate(conf.shared_xmls):
        prog = '\n[' + str(idx) + '/' + str(max) + '] '
        print(prog + 'Start to process ' + filename)
        content = read_xml(filename)
        san = Sanitize(content, filename, conf.rdmo_uris)
        if args.debug is False:
            san.process()
        outfolder, outfile = conf.output_filename(filename)
        write_xml(san.content, outfolder, outfile, args.debug)
