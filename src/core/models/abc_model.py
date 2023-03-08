"""Module with abstract class-interface for real-world object-representations"""

__author__ = 'Kolbeko A.B.'

# built-in
from abc import ABC, abstractmethod
from typing import List, Type, NoReturn, Callable, Dict, Iterable

# internal
from core.measurements import AbcDimension

dimensions_hint = List[Type[Callable[[AbcDimension, ...], AbcDimension]]]


class AbcModel(ABC):
    """Class define interface for object-representation"""

    def __init__(self, params: Dict):
        self._dimensions: dimensions_hint = ...
        self._links: List[Type[Callable[[AbcModel, ...], AbcModel]]] = ...
        self._init_specs(params)

    def get_dimensions(self) -> List[AbcDimension]:
        return self._dimensions

    @abstractmethod
    def _get_links(self):
        return self._links

    @abstractmethod
    def _init_specs(self, params: Dict) -> NoReturn:
        """Method for initialization of measuring for object"""
        ...

    @abstractmethod
    def _iterate_spec(self, spec_name: str, spec_sequence: Iterable):
        """Inizialize object by specificatino sequence"""
        ...
