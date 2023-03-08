"""Module fix abstract class-interface for measurements entity"""

__author__ = 'Kolbeko A.B'

# built-in
from numbers import Number

# built-in
from abc import ABC, abstractmethod
from typing import TypeVar, List, Dict


generic_types = TypeVar('generic_types', bound=Number | str)


class AbcDimension(ABC):

    def __init__(self, params: Dict):
        self._header: str = ...
        self._dimension: str = ...
        self._scale_step: List[generic_types] = ...
        self.load_spec(params)

    @abstractmethod
    def load_spec(self, params: Dict):
        """Method for downloading specification"""
        ...
