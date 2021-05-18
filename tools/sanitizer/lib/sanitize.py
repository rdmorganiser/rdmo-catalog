import hashlib

from lib.util import rxmatch, rxsearch


class Sanitize():
    def __init__(self, content, filename, rdmo_uris):
        self.content = content
        self.filename = filename
        self.new_uri = self.new_uri()
        self.rdmo_uris = rdmo_uris
        self.default_uri_prefix = 'https://rdmorganiser.github.io/terms'
        self.things_to_replace = [
            '<uri_prefix',
            '<catalog dc:uri',
            '<question dc:uri',
            '<questionset dc:uri',
            '<section dc:uri',
            '<option dc:uri',
            '<optionset dc:uri',
            '<condition dc:uri',
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
            rxsearch(r'(?<=\/shared\/).*?(?=\/)', self.filename)
        )
        return 'https://' + h + '.rdmo'

    def replace_uri(self, rxscheme, line):
        if rxmatch(rxscheme, line) is True \
                and self.contains_rdmo_uri(line) is False:
            line = line.replace(self.default_uri_prefix, self.new_uri)
        return line

    def contains_rdmo_uri(self, s):
        b = False
        for uri in self.rdmo_uris:
            if rxmatch(uri, s):
                b = True
                break
        return b
