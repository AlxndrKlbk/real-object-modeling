"""base realization of meaurement"""

__author__ = 'Kolbeko A.B'

# built-in
from typing import Dict

# internal
from core.layer import FeaturesAttr
from .feature_types import FeatureTypes
from .abc_feature import AbcFeature


class BaseFeature(AbcFeature):

    def __init__(self, params: Dict):
        for key, value in params.items():
            if key in [FeaturesAttr.LINKS, FeaturesAttr.VALUES]:
                if params.get(FeaturesAttr.TYPE) == FeatureTypes.NUMERIC and value:
                    # ToDo
                    #  1.possible errors while processing data
                    #  2.Need to use more effective numeric type
                    value = [float(val.strip()) for val in value.split(',')]
                elif value:
                    value = [val.strip() for val in value.split(',')]

            object.__setattr__(self, key, value)
