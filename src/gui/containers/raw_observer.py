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
        self.interior: tk.Frame = ...

    def load_content(self, init_data: Dict, params: Optional[Dict] = None) -> NoReturn:
        """
        Method for Downloads data to components of parent frame
        Args:
            init_data: dict for canvas init
            params: dict for other components init
        """
        params = params if params else {}

        self._entries_count = params.get(ParamsKeys.ENTRIES_COUNT)
        self._row_title = params.get(ParamsKeys.TITLE)

        self._init_canvas(**init_data)
        self.interior = tk.Frame(self.canvas, **init_data)

        # ToDo add frame with column names
        buttons_spec = [('Add row', self.add_row),
                        ('Del row', self.del_row)]
        self._buttons_toolbar = ButtonsToolbar(self.interior, buttons_spec)

        interior_id = self.canvas.create_window(0, 0, window=self.interior, anchor=tk.NW)

        self._bind_interior()
        self._bind_canvas(interior_id)

    def _init_canvas(self, **kwargs) -> NoReturn:
        """
        Method initialize canvas and scrollbar
        """
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.scrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                                yscrollcommand=self.scrollbar.set, **kwargs)

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        self.scrollbar.config(command=self.canvas.yview)

        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

    def _bind_interior(self) -> NoReturn:
        """
        Update the scrollbars to match the size of the inner frame.
        """
        def _configure_interior(_):
            size = (0, 0, str(self.interior.winfo_reqwidth()), str(self.interior.winfo_reqheight()))
            self.canvas.config(scrollregion=size)
            if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
                self.canvas.config(width=self.interior.winfo_reqwidth())
        self.interior.bind('<Configure>', _configure_interior)

    def _bind_canvas(self, interior_id: int) -> NoReturn:
        """
        Update the inner frame's width to fill the canvas.
        Args:
            interior_id: identifier of window
        """
        def _configure_canvas(_):
            if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
                self.canvas.itemconfigure(interior_id, width=self.canvas.winfo_width())
        self.canvas.bind('<Configure>', _configure_canvas)

    def add_row(self) -> NoReturn:
        """Method for inserting row"""
        total_row = len(self.rows_list)

        raw_params = {ParamsKeys.ENTRIES_COUNT: self._entries_count,
                      ParamsKeys.ROW_NUM: total_row,
                      ParamsKeys.TITLE: self._row_title}

        new_row = DefaultRow(self.interior, raw_params)
        new_row.pack(anchor=tk.S, side=tk.TOP)
        self.rows_list.insert(total_row, new_row)
        self.update()

    def del_row(self) -> NoReturn:
        """
        Method for delete last added row
        """
        if len(self.rows_list) > 1:
            self.rows_list.pop().destroy()
