"""Module with names of entities, represented on XML"""

__author__ = 'Kolbeko A.B.'

# built-in
from enum import Enum, unique


@unique
class Entities(str, Enum):
    OBJECT = 'object'
    MEASUREMENT = 'measurement'
