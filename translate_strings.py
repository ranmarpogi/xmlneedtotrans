import os
import xml.etree.ElementTree as ET
from googletrans import Translator

def translate_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        translator = Translator()

        for value in root.iter('VALUE'):
            if value.text:
                translated_text = translator.translate(value.text, dest='en').text
                value.text = translated_text

        tree.write(file_path, encoding='utf-8', xml_declaration=True)
    except ET.ParseError as e:
        print(f"Error parsing {file_path}: {e}")

def main():
    xml_files = [
        'autolevelset.xml',
        'commentstrtable.xml',
        'gameextext.xml',
        'launcher_gs.xml',
        'servertext.xml',
        'tipstrtable.xml'
    ]

    for xml_file in xml_files:
        if os.path.exists(xml_file):
            translate_xml_file(xml_file)
            print(f'Translated {xml_file}')
        else:
            print(f'{xml_file} not found')

if __name__ == '__main__':
    main()
