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
        for key, value in params:
            if key in [FeaturesAttr.LINKS, FeaturesAttr.Values]:
                if params.get(FeaturesAttr.TYPE) == FeatureTypes.NUMERIC:
                    # ToDo
                    #  possible errors while processing data
                    value = [float(val.strip()) for val in value.split(',')]
                else:
                    value = [val.strip() for val in value.split(',')]

            object.__setattr__(self, key, value)
