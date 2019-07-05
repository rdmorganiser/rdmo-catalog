import os
from copy import deepcopy
from lxml import etree
from lxml.etree import Element

def main():
    # start cleaning both input domains of duplicates (idealy none present)
    oldroot = read_xml("rdmo.xml")
    newroot = read_xml("domain.xml")
    olddomain = clean_up_domain(oldroot)
    newdomain = clean_up_domain(newroot)
    print("number of elements: old = %s, new = %s" % (len(olddomain), len(newdomain)))

    changed_attributes = make_root()
    added_attributes = make_root()
    deleted_attributes = make_root()

    # checking which attributes got added into the new domain and which are missing from the old
    # deleted attributes always contain uaruhr specific attributes
    for attribute in newdomain.iterchildren("attribute"):
        xpath = "//path[text()='" + attribute.find("path").text + "']"
        if len(olddomain.xpath(xpath)) == 1:
            # checking if any attribute got changed (these may be falsly
            # interpreted as missing or added)
            if check_identical(attribute, olddomain.xpath(xpath)[0].getparent()):
                pass
            else:
                changed_attributes.append(deepcopy(attribute))
                changed_attributes.append(deepcopy(olddomain.xpath(xpath)[0].getparent()))
        else: added_attributes.append(deepcopy(attribute))

    for attribute in olddomain.iterchildren("attribute"):
        xpath = "//path[text()='" + attribute.find("path").text + "']"
        if len(newdomain.xpath(xpath)) == 1:
            continue
        else: deleted_attributes.append(deepcopy(attribute))

    write_catalogs([added_attributes, deleted_attributes, changed_attributes],["added", "deleted", "changed"])

def check_identical(element1, element2):
    # checks only for element texts, but since
    # the ID elements are not independent this should do just fine
    for child in element1.iterchildren():
        if child.text == element2.find(child.tag).text:
            continue
        else:
            return False
    return True

def clean_up_domain(root):
    # removing duplicates present in the domain files and returning seperate roots
    newroot = make_root()
    duplicates = 0
    for attribute in root.iterchildren("attribute"):
        xpath = "//path[text()='" + attribute.find("path").text + "']"
        if len(newroot.xpath(xpath)) == 1:
            duplicates += 1
            continue
        elif len(newroot.xpath(xpath)) == 0:
            newroot.append(deepcopy(attribute))
        else:
            raise ValueError("unexpected Value of entries in new root: %s" % (len(newroot.xpath(xpath))))
    print("removed %s duplicates" % (duplicates))
    return newroot

def write_catalogs(cat_list, name_list):
    # takes a list of root elements and file names and writes them to the specified
    # relative directory
    for n, cat in enumerate(cat_list):
        tree = etree.ElementTree(cat)
        tree.write(name_list[n] + ".xml",
                    xml_declaration=True, encoding="UTF-8")

def read_xml(file_name):
    # reads in a xml file and returns it as etree.Element
    tree = etree.parse(os.path.abspath(file_name))
    root = tree.getroot()
    return root

def make_root():
    # takes a list of catalog variables [key, name] and generates a root element
    # with a predefined name space among other informations
    XHTML_NAMESPACE = "http://purl.org/dc/elements/1.1/"
    XHTML = "{%s}" % XHTML_NAMESPACE
    NSMAP = {"dc":XHTML_NAMESPACE} # the default namespace with prefix
    root = etree.Element("rdmo", nsmap=NSMAP) # lxml only!
    return root

if __name__ == "__main__":
    main()
