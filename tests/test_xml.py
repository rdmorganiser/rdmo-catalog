import os
import xml.etree.ElementTree as ET
from pathlib import Path
from subprocess import check_call

import pytest

PATHS = ["rdmorganiser", "shared"]
TAGS = [
    "condition",
    "attribute",
    "optionset",
    "option",
    "catalog",
    "section",
    "questionset",
    "question",
    "task",
    "view",
]


def walk_xml_files():
    for path in PATHS:
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = Path(root) / file
                if file_path.suffix == ".xml":
                    yield file_path


@pytest.mark.parametrize("xml_file", walk_xml_files())
def test_xmllint(xml_file):
    check_call(["xmllint", "--noout", xml_file])


@pytest.mark.parametrize("xml_file", walk_xml_files())
def test_tags(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    assert root.tag == "rdmo"
    for child in root:
        assert child.tag in TAGS
