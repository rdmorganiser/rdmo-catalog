#!/usr/bin/env python3

import argparse
import json
import logging
import os
import xml.etree.ElementTree as ET
from pathlib import Path
from pydantic import BaseModel, Field, HttpUrl, ConfigDict
from typing import Optional, List, Dict

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Namespace and module mappings
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

# Define Pydantic models
class Element(BaseModel):
    type: str
    uri: HttpUrl
    uri_prefix: Optional[HttpUrl] = None
    key: Optional[str] = None
    path: Optional[str] = None
    comment: Optional[str] = None
    additional_attributes: Dict[str, Optional[str]] = Field(default_factory=dict)

    model_config = ConfigDict(extra="allow", populate_by_name=True)

class Output(BaseModel):
    conditions: List[Element] = Field(default_factory=list)
    domain: List[Element] = Field(default_factory=list)
    options: List[Element] = Field(default_factory=list)
    questions: List[Element] = Field(default_factory=list)
    tasks: List[Element] = Field(default_factory=list)
    views: List[Element] = Field(default_factory=list)

    def add_element(self, element: Element, module_name: str):
        if hasattr(self, module_name):
            getattr(self, module_name).append(element)

    def model_dump_filtered(self, *args, **kwargs) -> Dict:
        # Use model_dump to get the dictionary representation and remove empty lists
        data = self.model_dump(**kwargs)
        return {k: v for k, v in data.items() if v}

# Function to parse XML and map it to the Pydantic models
def parse_xml_to_output(xml_file: Path) -> Output:
    output = Output()
    try:
        tree = ET.parse(xml_file)
        root_node = tree.getroot()

        if root_node.tag == 'rdmo':
            for element_node in root_node:
                element_data = {
                    'type': element_node.tag,
                    'uri': element_node.attrib.get(f"{nsmap['dc']}uri")
                }

                if not element_data['uri']:
                    logger.warning(f"Missing URI in element {element_node.tag} in {xml_file}")
                    continue

                for child_node in element_node:
                    if child_node.tag.startswith(nsmap['dc']):
                        key = child_node.tag[len(nsmap['dc']):]
                    elif 'lang' in child_node.attrib:
                        key = f"{child_node.tag}_{child_node.attrib['lang']}"
                    else:
                        key = child_node.tag

                    value = child_node.attrib.get(f"{nsmap['dc']}uri") or child_node.text
                    element_data[key] = value

                # Identify module and append element
                module_name = modulemap.get(element_node.tag, None)
                if module_name:
                    element = Element(**element_data)
                    output.add_element(element, module_name)
                    logger.info(f"Added element of type {element_data['type']} to {module_name}")

    except ET.ParseError as e:
        logger.error(f"Failed to parse XML file {xml_file}: {e}")
    return output

# Main function to handle command-line arguments and aggregate multiple XML files
def main():
    parser = argparse.ArgumentParser(description='Convert XML files to a single JSON using Pydantic models.')
    parser.add_argument('input_dir', help='Directory containing XML files', type=str)
    parser.add_argument('output_path', help='Path to save the single JSON output', type=str)

    args = parser.parse_args()
    input_dir = Path(args.input_dir)
    output_file = Path(args.output_path)

    # Aggregate output across multiple files
    aggregated_output = Output()

    for root, _, files in os.walk(input_dir):
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix == '.xml':
                logger.info(f'Processing {file_path}')
                file_output = parse_xml_to_output(file_path)
                # breakpoint()
                # Merge the contents of file_output into aggregated_output
                for field in aggregated_output.model_fields.keys():
                    getattr(aggregated_output, field).extend(getattr(file_output, field))

    # Save aggregated output as JSON, filtering out empty lists
    try:
        with output_file.open('w') as fp:
            json.dump(aggregated_output.model_dump_filtered(mode="json"), fp, indent=2)
        logger.info(f'Saved aggregated JSON output to {output_file}')
    except Exception as e:
        logger.error(f"Error saving JSON output: {e}")

if __name__ == '__main__':
    main()
