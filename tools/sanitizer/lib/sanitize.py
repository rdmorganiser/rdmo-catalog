import hashlib

from lib.util import rxsearch


class Sanitize():
    def __init__(self, content, filename, conf):
        self.content = content
        self.filename = filename
        self.rdmo_uris = conf.rdmo_uris
        self.old_uri_prefix = conf.conf['args'].old_uri_prefix
        self.new_uri_prefix = conf.conf['args'].new_uri_prefix

    def process(self):
        new_content = []
        for line in self.content:
            line = self.replace_uri(line)
            new_content.append(line)
        self.content = new_content

    def replace_uri(self, line):
        if self.contains_rdmo_uri(line) is False:
            line = line.replace(self.old_uri_prefix, self.new_uri_prefix)
        return line

    def contains_rdmo_uri(self, s):
        b = False
        for uri in self.rdmo_uris:
            if uri in s:
                b = True
                break
        return b

    def hash_string(self, str):
        hash_object = hashlib.sha1(str.encode('utf-8'))
        return hash_object.hexdigest()

    def new_uri(self):
        h = self.hash_string(
            rxsearch(r'(?<=\/shared\/).*?(?=\/)', self.filename)
        )
        return 'https://' + h + '.rdmo'
