"""Module with base realization of input row"""

__author__ = 'Kolbeko A.B.'

# built-in
from typing import Optional, Dict, NoReturn
import tkinter as tk

# internal
from ..const.params_keys import ParamsKeys


class DefaultRow(tk.Frame):
    def __init__(self, parent, params: Optional[Dict] = None):
        """
        Method pack Entries boxes to row insight of Frame
        Args:
            parent: root object
            params: dict with params
        """
        super().__init__(parent)
        title_str = params.get(ParamsKeys.TITLE)
        row_num = params.get(ParamsKeys.ROW_NUM)
        entries_count = len(params.get(ParamsKeys.ENTRIES))

        label = tk.Label(self, text=f'{title_str} №{row_num+1}')
        label.pack(side=tk.LEFT, padx=25, pady=5)

        self.label = label
        self.entries = []
        for i in range(0, entries_count):
            entry = tk.Entry(self)
            entry.pack(side=tk.LEFT, padx=5, pady=5)
            self.entries.append(entry)

    def destroy(self) -> NoReturn:
        self.label.destroy()
        [entry.destroy() for entry in self.entries]
        super().destroy()

    def get_entries_data(self):
        entries_content = {}
        for i, data in enumerate(self.entries):
            ...

        return entries_content
