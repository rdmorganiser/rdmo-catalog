#!/usr/bin/env python3

import argparse
import csv
import sys
import xml.etree.ElementTree as et

nsmap = {
    'dc': '{http://purl.org/dc/elements/1.1/}'
}

parser = argparse.ArgumentParser()
parser.add_argument('file')
args = parser.parse_args()

writer = csv.writer(sys.stdout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

tree = et.parse(args.file)
root = tree.getroot()

for child in root:
    uri = child.attrib['{dc}uri'.format(**nsmap)]
    row = [uri] + [node.text or '' for node in child]
    writer.writerow(row)
