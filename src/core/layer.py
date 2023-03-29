

# built-in
from enum import Enum, unique

# internal
from gui import FeatureRowObserver, ObjectsRowObserver


@unique
class ObjectAttr(str, Enum):
    """Enum with BaseObject fields"""

    NAME = ObjectsRowObserver.NAME
    FEATURES = ObjectsRowObserver.METRICS
    LINKS = ObjectsRowObserver.CONNECTIONS


@unique
class FeaturesAttr(str, Enum):
    NAME = FeatureRowObserver.NAME
    VALUES = FeatureRowObserver.VALUES
    TYPE = FeatureRowObserver.TYPE
    UNITS = FeatureRowObserver.DIMENSION
    LINKS = FeatureRowObserver.CONNECTIONS
