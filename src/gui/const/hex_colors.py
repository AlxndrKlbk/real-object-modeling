"""Module with hexadecimal RGB codes"""

__author__ = 'Kolbeko A.B.'

# built-in
from enum import Enum, unique


@unique
class HexColors(str, Enum):
    """Enum hexadecimal RGB codes"""

    LIGHT_GREEN = '#dff4a7'
    SATURATE_GREE = '#befe15'
    LIGHT_YELLOW = '#faf578'
    EGS_YELLOW = '#ffff00'
    BLUE = '#85c1e9'
