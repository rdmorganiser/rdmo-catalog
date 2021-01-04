#!/usr/bin/env python3

import argparse
import csv
import json
import logging
import os
import xml.etree.ElementTree as et
from collections import OrderedDict
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

nsmap = {
    'dc': '{http://purl.org/dc/elements/1.1/}'
}

modulemap = {
    'condition': 'conditions',
    'attribute': 'domain',
    'optionset': 'options',
    'option': 'options',
    'catalog': 'questions',
    'section': 'questions',
    'questionset': 'questions',
    'question': 'questions',
    'task': 'tasks',
    'view': 'views'
}

parser = argparse.ArgumentParser(description='Convert xml files to csv or json.')
parser.add_argument('format', help='format to convert to', choices=['csv', 'json'])

args = parser.parse_args()

output = {
    'conditions': [],
    'domain': [],
    'options': [],
    'questions': [],
    'tasks': [],
    'views': []
}

for path in ['rdmorganiser', 'shared']:
    for root, dirs, files in os.walk(path):
        if not root.startswith('./.'):
            root_path = Path(root)

            for file in files:
                file_path = root_path / file

                if file_path.suffix == '.xml':
                    logger.info('Processing %s', file_path)

                    tree = et.parse(file_path)
                    root_node = tree.getroot()

                    if root_node.tag == 'rdmo':
                        for element_node in root_node:
                            element = OrderedDict()
                            element['type'] = element_node.tag
                            element['uri'] = element_node.attrib['{dc}uri'.format(**nsmap)]

                            for child_node in element_node:
                                if child_node.tag.startswith(nsmap['dc']):
                                    key = child_node.tag[len(nsmap['dc']):]
                                elif 'lang' in child_node.attrib:
                                    key = child_node.tag + '_' + child_node.attrib['lang']
                                else:
                                    key = child_node.tag

                                if child_node.attrib.get('{dc}uri'.format(**nsmap)):
                                    value = child_node.attrib.get('{dc}uri'.format(**nsmap))
                                else:
                                    value = child_node.text

                                element[key] = value

                            module = modulemap[element_node.tag]
                            output[module].append(element)

output_path = Path(args.format)
output_path.mkdir(exist_ok=True)

for output_name, output_list in output.items():
    file_path = output_path.joinpath(output_name).with_suffix('.' + args.format)
    logger.info('Writing %s', file_path)

    if args.format == 'json':
        with file_path.open('w') as fp:
            json.dump(output_list, fp, indent=2)

    elif args.format == 'csv':
        # collect and oder columns
        keys = []
        for element in output_list:
            for key in element.keys():
                if key not in ['uri', 'uri_prefix', 'key', 'path', 'comment']:
                    keys.append(key)
        fieldnames = ['uri', 'uri_prefix', 'key', 'comment'] + sorted(set(keys))

        with open(file_path, 'w', newline='') as csvfile:
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore', quoting=csv.QUOTE_NONNUMERIC)
            csvwriter.writeheader()
            csvwriter.writerows(output_list)
