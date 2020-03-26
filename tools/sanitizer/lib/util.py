import os
import re


class util():
    def __init__(self, basedir):
        self.basedir = basedir
        self.xml_files = self.detect_xml_files()

    def detect_xml_files(self):
        xml_files = []
        for root, dirs, files in os.walk(self.basedir):
            for file in files:
                if file.endswith('.xml') is True \
                        and file.startswith('_new') is False:
                    xml_files.append(os.path.join(root, file))
        return sorted(xml_files)

    def read_xml(self, filename):
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

    def write_xml(self, data, filename):
        print('Write file ' + filename)
        with open(filename, 'w') as fp:
            for line in data:
                fp.write(line + '\n')

    def output_filename(self, filename):
        folder = re.search('.*(?=\/)', filename).group(0)
        shortname = re.search('[^/]+$', filename).group(0)
        return os.path.join(folder, '_new_' + shortname)
