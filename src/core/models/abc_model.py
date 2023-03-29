"""Module with abstract class-interface for real-world object-representations"""

__author__ = 'Kolbeko A.B.'

# built-in
from abc import ABC, abstractmethod
from typing import List, Type, NoReturn, Callable, Dict

# internal
from core.measurements import AbcFeature
from core.measurements import BaseFeature

features_hint = List[Type[Callable[[AbcFeature, ...], AbcFeature]]]


class AbcModel(ABC):
    """Class define interface for object-representation"""

    @abstractmethod
    def __init__(self, params: Dict):
        self._name: str = ...
        self._features: features_hint = ...
        self._links: List[Type[Callable[[AbcModel, ...], AbcModel]]] = ...

    @abstractmethod
    def get_links(self):
        return self._links

    @abstractmethod
    def set_features(self, feature_entities: Dict[BaseFeature]) -> NoReturn:
        """Initialize feature instances and write on object instance links"""
        ...
