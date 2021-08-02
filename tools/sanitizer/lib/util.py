import os
import pprint as ppr
import re
from os.path import join as pj


def detect_xml_files(basedir):
    xml_files = []
    for root, dirs, files in os.walk(basedir):
        for file in files:
            if file.endswith('.xml') is True \
                    and file.startswith('_new') is False:
                xml_files.append(os.path.join(root, file))
    return sorted(xml_files)


def get_uris_from_file(fil, filter=None):
    uris = []
    content = read_xml(fil)
    for line in content:
        s = rxsearch(r'(?<=dc:uri=").*?(?=")', line)
        if s is not None:
            if filter is None:
                uris.append(s)
            else:
                if rxmatch(filter, s) is True:
                    uris.append(s)
    return uris


def mkdir(folder):
    try:
        os.makedirs(folder)
    except FileExistsError:
        pass


def pprint(obj):
    pp = ppr.PrettyPrinter(indent=4)
    pp.pprint(obj)


def rxmatch(rxscheme, s):
    return bool(re.search(rxscheme, s))


def rxsearch(rxscheme, s, group=0):
    r = None
    m = re.search(rxscheme, s)
    if m is not None:
        r = m.group(group)
    return r


def read_xml(filename):
    print('Read file ' + filename)
    arr = []
    try:
        filecontent = open(filename, 'r')
    except Exception as e:
        print(e)
    else:
        for line in filecontent.read().splitlines():
            arr.append(line)
    return(arr)


def write_xml(data, folder, filename, debug=False):
    mkdir(folder)
    target = pj(folder, filename)
    print('Write file ' + target)
    if debug is False:
        with open(target, 'w') as fp:
            for line in data:
                fp.write(line + '\n')
