"""Module with base realisation"""

__author__ = 'Kolbeko A.B'

# built-in
from typing import List, Type, NoReturn, Callable, Iterable

# internal
from .abc_model import AbcModel

links_hint = List[Type[Callable[[AbcModel], AbcModel]]]


class BaseModel(AbcModel):

    def _get_links(self) -> links_hint:
        return self._links

    def _init_specs(self, params) -> NoReturn:
        """Method for initialization of measurement for object"""
        for spec_type, spec_sequence in params:
            self._iterate_spec(spec_type, spec_sequence)

    def _iterate_spec(self, spec_name: str, spec_sequence: Iterable):
        """Method iterate specifications and direct data for specific handlers"""
        init_container = []
        for spec in spec_sequence:

            #  ToDo
            #  define possible spec types, data structures and handlers for them
            initialized = spec()
            init_container.append(initialized)
        setattr(self, '_' + spec_name, init_container)
