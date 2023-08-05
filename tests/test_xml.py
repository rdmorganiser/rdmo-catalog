import xml.etree.ElementTree as ET
from pathlib import Path
from subprocess import check_call

import pytest

PATHS = ("rdmorganiser", "shared")
PATHS = (Path(p) for p in PATHS)
TAGS = {
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
}


def walk_xml_files():
    for path in PATHS:
        yield from path.rglob("*.xml")


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
