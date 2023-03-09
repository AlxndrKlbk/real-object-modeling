"""Module with enums"""

__author__ = 'Kolbeko A.B.'

# built-in
from enum import Enum, unique


@unique
class ParamsKeys(Enum):
    """Enum for params keys for RawObserver and nested frames"""
    TITLE = 'title'
    ROW_NUM = 'row_num'
    ENTRIES_COUNT = 'entries_count'
    FRAME_NAME = 'frame_name'
    X_SCALE = 'x_scale'
    Y_SCALE = 'y_scale'
