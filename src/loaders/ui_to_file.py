"""Module with methods for uploading data from ui"""

__author__ = 'Kolbeko A.B.'

# built-in
from typing import Dict, List, NoReturn
from io import StringIO
import xml.etree.ElementTree as et

# internal
from .const import XMLTags, Entities


def save_to_file(data: Dict, path: str = '../file.xml') -> NoReturn:
    """
    Method for download data to XML-file
    Args:
        data: dict with data from UI
        path: destination for XML-file
    Returns:
        str - path to saved file
    """
    xml_tree = json_to_xml(data)
    _save_to_file(xml_tree, path)


def save_to_io(data: Dict) -> StringIO:
    """
    Method for upload data to IO
    Args:
        data: dict with data from UI
    Returns:
        StringIO prepared for reading
    """
    xml_tree = json_to_xml(data)
    xml_tree = et.tostring(xml_tree).decode()

    buffered = StringIO()
    buffered.write(xml_tree)
    buffered.seek(0)

    #  ToDo function for reading object from IO xml or writing on IO xml in binaries
    # read_file = et.parse(buffered)
    # xml_tree = read_file.getroot()
    return buffered


def json_to_xml(data: Dict) -> et.Element:
    """
    Method converting json to XML-tree (instance of et.Element)
    Args:
        data: dict with data from UI
    Returns:
        et.Element
    """
    xml_tree = et.Element(XMLTags.ROOT)

    for entity_type, entities in data.items():
        sub_tree = et.Element(XMLTags.ARRAY)
        _add_entities_type(sub_tree, entity_type)
        _parse_entities(sub_tree, entities)
        xml_tree.append(sub_tree)

    et.indent(xml_tree)
    return xml_tree


def _save_to_file(tree: et.Element, path: str):

    payload = et.tostring(tree).decode()
    with open(path, 'w+') as file:
        file.write(payload)


def _add_entities_type(parent: et.Element, ent_type: Entities) -> NoReturn:
    element = et.Element(XMLTags.TYPE)
    element.text = ent_type
    parent.append(element)


def _parse_entities(parent: et.Element, entities_list: List):

    for spec in entities_list:
        entity = et.Element(XMLTags.ITEM)
        _fill_entity(entity, spec)
        parent.append(entity)


def _fill_entity(entity: et.Element, spec: Dict) -> NoReturn:
    for feature_name, feature_value in spec.items():
        feature = et.Element(feature_name)
        feature.text = feature_value
        entity.append(feature)


if __name__ == '__main__':
    print('test')
