import hashlib
import re


class sanitizer():
    def __init__(self, content, filename):
        self.content = content
        self.filename = filename
        self.new_uri = self.new_uri()
        self.default_uri_prefix = 'https://rdmorganiser.github.io/terms'
        self.things_to_replace = [
            '<uri_prefix',
            '<catalog\sdc:uri',
            '<question\sdc:uri',
            '<questionset\sdc:uri',
            '<section\sdc:uri',
            '<option\sdc:uri',
            '<optionset\sdc:uri',
            '<condition\sdc:uri',
        ]

    def process(self):
        new_content = []
        for line in self.content:
            for el in self.things_to_replace:
                line = self.replace_uri(el, line)
            new_content.append(line)
        self.content = new_content

    def hash_string(self, str):
        hash_object = hashlib.sha1(str.encode('utf-8'))
        return hash_object.hexdigest()

    def new_uri(self):
        h = self.hash_string(
            re.search(r'(?<=\/shared\/).*?(?=\/)', self.filename).group(0)
        )
        return 'https://' + h + '.rdmo'

    def replace_uri(self, rxmatch, line):
        if bool(re.search(rxmatch, line)) is True:
            line = line.replace(self.default_uri_prefix, self.new_uri)
        return line
