"""Module with  params keys enums"""

__author__ = 'Kolbeko A.B.'

# built-in
from enum import Enum, unique


@unique
class ParamsKeys(str, Enum):
    """Enum for params keys for RawObserver and nested frames"""

    TITLE = 'text'
    ROW_NUM = 'row_num'
    ENTRIES = 'ENTRIES'
    FRAME_NAME = 'frame_name'
    X_SCALE = 'x_scale'
    Y_SCALE = 'y_scale'
    BACKGROUND = 'background'
    X_RATIO = 'x_ratio'
    Y_RATIO = 'y_ratio'
    WIDTH = 'width'
    HEIGHT = 'height'
