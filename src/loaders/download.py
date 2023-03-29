"""Module with methods for download data from xml"""

__author__ = 'Kolbeko A.B.'

# built-in
from typing import Dict, List, NoReturn, Union
from io import StringIO
import xml.etree.ElementTree as et

# internal
from const import XMLTags, Entities
from core.models import BaseModel
from core.measurements import BaseFeature
from core.layer import ObjectAttr

entities_map = {
    Entities.OBJECT: BaseModel,
    Entities.MEASUREMENT: BaseFeature
}

parsed_structure_hint = Dict[str, Dict[str, Union[BaseFeature, BaseFeature]]]


def download_from_xml(path: str) -> parsed_structure_hint:
    """Method for parsing XML to json"""

    tree = et.parse(path)
    root = tree.getroot()
    result = {}
    for items in root.findall(XMLTags.ARRAY):
        result.update(_process_items(items))
    return result


def _process_items(items: et.Element) -> parsed_structure_hint:
    type_tag = items.find(XMLTags.TYPE)
    if type_tag is not None:
        type_tag = type_tag.text
        entity = entities_map.get(type_tag)
    else:
        raise RuntimeError(f'Got unsupported entity type tag:\n'
                           f'{et.tostring(items).decode()}')

    objects_dict = {}
    for item in items.findall(XMLTags.ITEM):
        entity_spec = {}
        for elem in item.iter():
            entity_spec[elem.tag] = elem.text

        entity_spec.pop(XMLTags.ITEM)
        name = entity_spec.get(ObjectAttr.NAME)
        instance = entity(entity_spec)
        objects_dict[name] = instance

    return {type_tag: objects_dict}


if __name__ == '__main__':
    downloaded = download_from_xml('../../saves/upsv.xml')
    print(downloaded)