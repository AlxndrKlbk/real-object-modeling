"""Module fix abstract class-interface for measurements entity"""

__author__ = 'Kolbeko A.B'

# built-in
from numbers import Number

# built-in
from abc import ABC, abstractmethod
from typing import TypeVar, List, Dict


generic_types = TypeVar('generic_types', bound=Number | str)


class AbcFeature(ABC):

    @abstractmethod
    def __init__(self, params: Dict):
        ...

        # ToDo
        # support possibility to init possible values by steps for numeric features
        self._scale_step: List[generic_types] = ...
        # self.load_spec(params)
