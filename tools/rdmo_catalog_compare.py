import codecs, os
import xml.etree.ElementTree as ET

def read_xml():
    # read in the xml files from both versions and return tree objects
    # This is reads in rdmo >v0.11 data model 
    xml_example = codecs.open(os.path.abspath("rdmo_questions_old.xml"),
                    "r", "utf-8")
    old_tree = ET.parse(xml_example)
    xml_example = codecs.open(os.path.abspath("rdmo_questions_new.xml"),
                    "r", "utf-8")
    new_tree = ET.parse(xml_example)
    return old_tree, new_tree

def get_new_root_content(root):
    questions_de = []
    questions_en = []
    uris = []
    help_de = []
    help_en = []
    for question in root.iter("question"):
        for text in question.findall("text"):
            if text.attrib["lang"] == "de":
                questions_de.append(text.text)
            elif text.attrib["lang"] == "en":
                questions_en.append(text.text)
        for key in question.attrib:
            uris.append(question.attrib[key])
        for help in question.findall("help"):
            if help.attrib["lang"] == "de":
                if help.text == None:
                    help_de.append("")
                else:
                    help_de.append(help.text)
            elif help.attrib["lang"] == "en":
                if help.text == None:
                    help_en.append("")
                else:
                    help_en.append(help.text)
    assert len(uris) == len(questions_de)
    assert len(uris) == len(questions_en)
    return uris, questions_de, questions_en, help_de, help_en

def strip_uris(uris):
    stripped_uris = []
    for uri in uris:
        assert type(uri) == type("")
        uri = uri.replace("/", " ")
        uri = uri.replace("-", " ")
        uri = uri.replace("_", " ")
        stripped_uris.append(uri)
    return stripped_uris

def main():
    old_tree, new_tree = read_xml()
##    preview_o = open("preview_old", "w")
##    preview_y = open("preview_new", "w")
    output = open("questions_differences", "w")
    name_space = {"dc":"http://purl.org/dc/elements/1.1/"}
    old_uris, old_questions_de, old_questions_en, old_help_de, old_help_en = get_new_root_content(old_tree.getroot())
    new_uris, new_questions_de, new_questions_en, new_help_de, new_help_en = get_new_root_content(new_tree.getroot())
    old_uris_s = strip_uris(old_uris)
    new_uris_s = strip_uris(new_uris)

    assert len(old_uris) == len(old_uris_s) == len(old_questions_de) == len(old_questions_en) == len(old_help_de) == len(old_help_en)
    assert len(new_uris) == len(new_uris_s) == len(new_questions_de) == len(new_questions_en)

    identical_uris = 0
    identical_questions = 0
    for x in range(len(old_uris_s)):
        if new_uris_s[x] in old_uris_s:
            # uris are identical and questions are checked
            identical_uris += 1
            # mapping the current URI of the new catalog to the old one
            list_index = old_uris_s.index(new_uris_s[x])
            output.write(new_uris[x][52:] + "\n")
            if new_questions_de[x] != old_questions_de[list_index]:
                output.write("different question texts: \n" +
                "new: " + new_questions_de[x] + "\n" +
                "old: " + old_questions_de[list_index] + "\n")
            if new_help_de[x] != old_help_de[list_index]:
                output.write("different help texts: \n" +
                "new help: " + new_help_de[x] + "\n" +
                "old help: " + old_help_de[list_index] + "\n")
            if new_questions_en[x] != old_questions_en[list_index]:
                output.write("different question texts: \n" +
                "new: " + new_questions_en[x] + "\n" +
                "old: " + old_questions_en[list_index] + "\n")
            if new_help_en[x] != old_help_en[list_index]:
                output.write("different help texts: \n" +
                "new help: " + new_help_en[x] + "\n" +
                "old help: " + old_help_en[list_index] + "\n")
            output.write("----------------------------------------------------- \n")
        else:
            # there is no identical uri in the other dataset
            output.write("new uri: " + new_uris[x][52:]  + "\n" +
            new_questions_de[x] + "\n" + new_help_de[x] + "\n" +
            new_questions_en[x] + "\n" + new_help_en[x] + "\n")
            output.write("----------------------------------------------------- \n")
        if old_uris_s[x] not in new_uris_s:
            # grabbing removed (or changed) uris
            output.write("removed old uri: " + old_uris[x][52:]  + "\n" +
            old_questions_de[x] + "\n" + old_help_de[x] + "\n" +
            old_questions_en[x] + "\n" + old_help_en[x] + "\n")
            output.write("----------------------------------------------------- \n")
    output.write("identical Uris: " + str(identical_uris))

if __name__ == "__main__":
    main()
