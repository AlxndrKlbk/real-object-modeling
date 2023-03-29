"""Module with feature types"""

__author__ = 'Kolbeko A.B'


# built-in
from enum import Enum, unique


@unique
class FeatureTypes(Enum):
    """Possible feature types"""

    NUMERIC = 'numeric'
    CATEGORICAL = 'categorical'
