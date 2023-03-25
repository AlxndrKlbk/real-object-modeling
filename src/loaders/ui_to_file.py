"""Module with methods for download data from ui"""

__author__ = 'Kolbeko A.B.'

# built-in
from typing import Dict
from io import StringIO
import xml.etree.ElementTree as ET


def save_to_xml(data: Dict) -> str:
    """
    Method for download data to xml
    Args:
        data: dict with data from UI
    Returns:
        str - path to saved file
    """
    print(f'I aws here {data}')

    # ToDo save to xml
    ...
    return ''


if __name__ == '__main__':
    root = ET.Element('a')
    objects = ET.SubElement(root, 'objects_array')

    for i in range(3):
        item = ET.Element('item')
        i_name = ET.Element('name')
        i_name.text = f'separator_{i}'

        item.append(i_name)
        objects.append(item)

    measurements = ET.SubElement(root, 'measuremens_array')
    # ET.dump(root)
    ET.indent(root)

    # print(ET.tostring(root, encoding="unicode"))
    # print(ET.tostring(root).decode())

    file_path = '../../file.xml'

    payload = ET.tostring(root).decode()
    with open(file_path, 'w+') as file:
        file.write(payload)

    buffered = StringIO()
    # buffered.write('<?xml version="1.0" encoding="UTF-8"?>')
    buffered.write(payload)
    buffered.seek(0)
    read_file = ET.parse(buffered)

    xml_tree = read_file.getroot()
    print(ET.tostring(xml_tree).decode())
