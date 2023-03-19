
# built-in
import tkinter as tk
from tkinter import messagebox
from typing import Union, Callable


def quite_callback(self: Union[tk.Tk, Callable]):
    if tk.messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        self.destroy()
