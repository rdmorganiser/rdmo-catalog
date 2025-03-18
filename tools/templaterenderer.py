import glob
import os

import xml.etree.ElementTree as ET

files = list(zip(
    glob.glob(os.path.join(os.path.dirname(__file__), 'templaterenderer-djangotemplates', '*.django')),
    glob.glob(os.path.join(os.path.dirname(__file__), 'templaterenderer-djangotemplates', '*.xmlskeleton'))
))
for template, headerfile in files:
    print('# Working on file pair:')
    print('  ' + os.path.abspath(template))
    print('  ' + os.path.abspath(headerfile))
    with open(template, 'r', encoding='utf-8') as open_template:
        escaped_template = open_template.read().replace('<','&lt;').replace('>','&gt;')
    with open(headerfile, 'r', encoding='utf-8') as open_header:
        header_content =  open_header.read()
        try:
            header_start=header_content.rsplit('<template>',1)[0]
            header_end=header_content.rsplit('</template>',1)[1]
        except IndexError:
            print('# The files do not hold a template-section. We try the next one.\n')
            continue
    outfile_path = os.path.join(os.path.dirname(__file__), '..', 'shared', os.path.basename(template).rsplit('.',1)[0] + '.xml')
    with open(
        outfile_path, 
        'w', 
        encoding='utf-8'
    ) as xmloutput:
        xmloutput.write(
            header_start + '<template>\n' + escaped_template + '\n        </template>' + header_end
        )
        print('# Template-file written: {}\n'.format(outfile_path))