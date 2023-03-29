"""Module with UI strings and containers with output strings"""

__author__ = 'Kolbeko A.B'


# built-in
from enum import Enum, unique


@unique
class ObjectsRowObserver(str, Enum):
    NAME = 'Name'
    METRICS = 'Metrics'
    CONNECTIONS = 'Connections'


@unique
class FeatureRowObserver(str, Enum):
    NAME = 'Name'
    TYPE = 'Type'
    VALUES = 'Values'
    DIMENSION = 'Dimension'
    CONNECTIONS = 'Connections'


OBJECT_FRAME_COLUMN_NAMES = [ObjectsRowObserver.NAME, ObjectsRowObserver.METRICS, ObjectsRowObserver.CONNECTIONS]
MEASUREMENT_FRAME_COLUMN_NAMES = [FeatureRowObserver.NAME, FeatureRowObserver.TYPE,
                                  FeatureRowObserver.VALUES, FeatureRowObserver.DIMENSION,
                                  FeatureRowObserver.CONNECTIONS]
