"""Module with abstract class-interface for real-world object-representations"""

__author__ = 'Kolbeko A.B.'

# built-in
from abc import ABC, abstractmethod


class AbcModel(ABC):
    """Class define interface for object-representation"""

    def __init__(self):
        self._measuring = ()
        self._connections = ()

    def get_measuring(self):
        return self._measuring

    def _get_connections(self):
        return self._connections

    @abstractmethod
    def _init_measuring(self):
        """Method for initialization of measuring for object"""
        ...

    @abstractmethod
    def _init_connections(self):
        """Method for initialization of possible connections for object"""
        ...
