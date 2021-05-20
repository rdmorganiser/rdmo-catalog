#!/usr/bin/env python3

import argparse
import logging
import xml.etree.ElementTree as et

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

nsmap = {
    'dc': '{http://purl.org/dc/elements/1.1/}'
}

parser = argparse.ArgumentParser(description='Compare xml files and show which urls are not in the first input file.')
parser.add_argument('files', nargs='+', help='files to compare')
parser.add_argument('--prefix', help='only compare a specific URI prefix')

args = parser.parse_args()

n = len(args.files)

uri_list = []
for file_path in args.files:
    tree = et.parse(file_path)
    root_node = tree.getroot()

    uri_set = set()
    if root_node.tag == 'rdmo':
        for element_node in root_node:
            uri = element_node.attrib['{dc}uri'.format(**nsmap)]
            if not args.prefix or uri.startswith(args.prefix):
                uri_set.add(uri)

    uri_list.append(uri_set)

for i in range(n):
    for j in range(n):
        difference = uri_list[i].difference(uri_list[j])

        if difference:
            print()
            print('# URI which are in {}, but not in {}'.format(args.files[i], args.files[j]))
            for uri in difference:
                print(uri)
