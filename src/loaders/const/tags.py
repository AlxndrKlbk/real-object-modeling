"""Module with tags enums"""

__author__ = 'Kolbeko A.B.'

# built-in
from enum import Enum, unique


@unique
class XMLTags(str, Enum):
    """Enum for params keys for RawObserver and nested frames"""

    ROOT = 'root'
    ARRAY = 'array'
    ITEM = 'item'
    TYPE = 'type'
