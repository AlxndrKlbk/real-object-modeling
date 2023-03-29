

# built-in
from enum import Enum, unique

# internal
from gui import FeatureRowObserver, ObjectsRowObserver


@unique
class ObjectAttr(str, Enum):
    """Enum with BaseObject fields"""

    NAME = ObjectsRowObserver.NAME.value
    FEATURES = ObjectsRowObserver.METRICS.value
    LINKS = ObjectsRowObserver.CONNECTIONS.value


@unique
class FeaturesAttr(str, Enum):
    NAME = FeatureRowObserver.NAME.value
    VALUES = FeatureRowObserver.VALUES.value
    TYPE = FeatureRowObserver.TYPE.value
    UNITS = FeatureRowObserver.DIMENSION.value
    LINKS = FeatureRowObserver.CONNECTIONS.value
