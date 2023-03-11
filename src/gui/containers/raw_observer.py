"""Module with basic class for containing rows and data at GUI"""

__author__ = 'Kolbeko A.B.'

# built-in
from typing import Optional, Dict, NoReturn
import tkinter as tk

# internal
from .default_row import DefaultRow
from .button_toolbar import ButtonsToolbar
from ..const.params_keys import ParamsKeys


class RowsObserver(tk.LabelFrame):
    """Container for rows"""

    def __init__(self, master, items: Optional[Dict] = None):
        super().__init__(master, text=items.get(ParamsKeys.FRAME_NAME))

        # ToDo add frame with column names
        buttons_spec = [('Add object', self.add_row),
                        ('Del object', self.del_row)]
        self.__buttons_toolbar = ButtonsToolbar(self, buttons_spec)

        items = items if items else {}

        self._entries_count = items.get(ParamsKeys.ENTRIES_COUNT)
        self._row_title = items.get(ParamsKeys.TITLE)

        # ToDo fix scroll bar
        self.scroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.rows_list = []
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


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.x_scale = self.winfo_screenwidth()
        self.y_scale = self.winfo_screenheight()
        self.geometry(f'{self.x_scale}x{self.y_scale}')

        self.frame_a = RowsObserver(self,
                                    {ParamsKeys.ENTRIES_COUNT: 3, ParamsKeys.TITLE: 'Object',
                                     ParamsKeys.FRAME_NAME: 'Objects frame', ParamsKeys.X_SCALE: self.x_scale,
                                     ParamsKeys.Y_SCALE: self.y_scale})
        self.frame_a.pack(side=tk.TOP)

        self.frame_b = RowsObserver(self,
                                    {ParamsKeys.ENTRIES_COUNT: 4, ParamsKeys.TITLE: 'Measurement',
                                     ParamsKeys.FRAME_NAME: 'Measurements frame', ParamsKeys.X_SCALE: self.x_scale,
                                     ParamsKeys.Y_SCALE: self.y_scale})
        self.frame_b.pack(anchor=tk.CENTER, side=tk.TOP)
