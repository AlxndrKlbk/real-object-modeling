"""Module with basic class for containing rows and data at GUI"""

__author__ = 'Kolbeko A.B.'

# built-in
from typing import Optional, Dict, NoReturn
import tkinter as tk
from tkinter import ttk

# internal
from .default_row import DefaultRow
from .button_toolbar import ButtonsToolbar
from ..const.params_keys import ParamsKeys


class RowsObserver(tk.LabelFrame):
    """Container for rows"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rows_list = []
        self.scrollbar: tk.Scrollbar = ...
        self._entries_count: int = ...
        self._row_title: str = ...
        self._buttons_toolbar: ButtonsToolbar = ...

    def load_content(self, params: Optional[Dict] = None):
        # ToDo add frame with column names
        buttons_spec = [('Add object', self.add_row),
                        ('Del object', self.del_row)]
        self._buttons_toolbar = ButtonsToolbar(self, buttons_spec)

        params = params if params else {}

        self._entries_count = params.get(ParamsKeys.ENTRIES_COUNT)
        self._row_title = params.get(ParamsKeys.TITLE)

        # ToDo fix scroll bar
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk. Y, expand=False)


        params = {ParamsKeys.ENTRIES_COUNT: self._entries_count,
                  ParamsKeys.ROW_NUM: len(self.rows_list),
                  ParamsKeys.TITLE: self._row_title}

        new_row = DefaultRow(self, params)
        new_row.pack(anchor=tk.S, side=tk.TOP)
        self.rows_list.insert(0, new_row)

    def add_row(self):
        """Method for inserting row"""
        total_row = len(self.rows_list)

        raw_params = {ParamsKeys.ENTRIES_COUNT: self._entries_count,
                      ParamsKeys.ROW_NUM: total_row,
                      ParamsKeys.TITLE: self._row_title}

        new_row = DefaultRow(self, raw_params)
        new_row.pack(anchor=tk.S, side=tk.TOP)
        self.rows_list.insert(total_row, new_row)
        self.update()

    def del_row(self) -> NoReturn:
        """
        Method for delete last added row
        """
        if len(self.rows_list) > 1:
            self.rows_list.pop().destroy()

