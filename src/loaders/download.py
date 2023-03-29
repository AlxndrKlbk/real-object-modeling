"""Module with methods for download data from xml"""

__author__ = 'Kolbeko A.B.'

# built-in
from typing import Dict, List, NoReturn
from io import StringIO
import xml.etree.ElementTree as et

# internal
from const import XMLTags, Entities
from core.models import BaseModel
from core.measurements import BaseFeature


entities_map = {
    Entities.OBJECT: BaseModel,
    Entities.MEASUREMENT: BaseFeature
}


def download_from_xml(path: str):
    tree = et.parse(path)
    root = tree.getroot()
    for items in root.findall(XMLTags.ARRAY):
        _process_items(items)


def _process_items(items: et.Element):
    type_tag = items.find(XMLTags.TYPE)
    if type_tag is not None:
        type_tag = type_tag.text
        entity = entities_map.get(type_tag)
    else:
        raise RuntimeError(f'Got unsupported entity type tag:\n'
                           f'{et.tostring(items).decode()}')

    for item in items.findall(XMLTags.ITEM):
        meme = item.attrib


if __name__ == '__main__':
    download_from_xml('../../saves/upsv.xml')