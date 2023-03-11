"""Module with buttons frame"""

__author__ = 'Kolbeko A.B.'

# built-in
from typing import List, Tuple
import tkinter as tk


class ButtonsToolbar(tk.Frame):
    """
    Toolbar with buttons
    """

    def __init__(self, parent, params: List[Tuple]):
        super().__init__(parent, bg='brown')
        self.pack(side=tk.TOP)
        for heading, func in params:
            tk.Button(self, text=heading, command=func).pack(side=tk.LEFT)
