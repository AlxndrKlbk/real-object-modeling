"""Module with base realisation"""

__author__ = 'Kolbeko A.B'

# built-in
from typing import List, Type, NoReturn, Callable, Iterable, Dict
from copy import deepcopy

# internal
from .abc_model import AbcModel
from core.layer import ObjectAttr
from core.measurements.base_feature import BaseFeature


links_hint = List[Type[Callable[[AbcModel], AbcModel]]]


class BaseModel(AbcModel):

    def __init__(self, params: Dict):
        for key, value in params:
            if key in [ObjectAttr.FEATURES, ObjectAttr.LINKS]:
                value = [val.strip() for val in value.split(',')]
            object.__setattr__(self, key, value)

    def __getattribute__(self, item):
        return self[item]

    def get_links(self) -> links_hint:
        return getattr(self, ObjectAttr.LINKS)

    def set_features(self, feature_entities: Dict[BaseFeature]) -> NoReturn:
        """Method iterate specifications and direct data for specific handlers"""

        for feature_name in self[ObjectAttr.FEATURES]:
            feature_instance = feature_entities.get(feature_name)

            if feature_instance is None:
                # ToDo
                #  possible it is error in data, need to handling it
                continue

            feature_instance = deepcopy(feature_instance)
            self._features[feature_name] = feature_instance
