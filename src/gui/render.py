"""
Module for launch GUI
"""

__author__ = 'Kolbeko A.B.'

# built-in
from tkinter import *
from functools import partial
from typing import Type, NoReturn, Generic


def add_row(parent: Misc) -> NoReturn:
    """
    Method add row of components to parent objects
    Args:
        parent: Misk
    """

    # ToDO pack rows under row
    row_num = len(entries) // 3
    label = Label(parent, text=f'Введите значения измерения {row_num+1}')

    n = len(entries)
    label.pack(side=LEFT, padx=5, pady=5)
    labels.append(label)
    for i in range(1, 4):
        entry = Entry(parent)
        entry.pack(side=LEFT, padx=5, pady=5)
        entries.append(entry)


def remove_row() -> NoReturn:
    """
    Method for delete row, pop extract last element from all GUI-containers
    destroy used to delete this element
    """
    if len(entries) > 1:
        labels.pop().destroy()
        for i in range(1, 4):
            entries.pop().destroy()


def calculate():
    # Тут какие-то вычисления
    ...


def create_frame(parent: Misc, frame_name: str) -> LabelFrame:
    label_frame = LabelFrame(parent, text=frame_name, width=X_SCALE*0.8, height=Y_SCALE*0.8)
    return label_frame


if __name__ == '__main__':
    root = Tk()

    X_SCALE = root.winfo_screenwidth()
    Y_SCALE = root.winfo_screenheight()
    labels = []
    entries = []

    root.geometry(f'{X_SCALE}x{Y_SCALE}')

    objects_frame = create_frame(root, 'objects_frame')
    objects_frame.pack(anchor=N)
    # ToDo possible need to use ComboBox in row of Objects_frame
    wrapper_objects_add = partial(add_row, objects_frame)
    Button(objects_frame, text="Добавить объект", command=wrapper_objects_add).pack()

    metrics_frame = create_frame(root, 'metrics_frame')
    metrics_frame.pack(anchor=S)
    wrapper_metrics_add = partial(add_row, metrics_frame)
    Button(metrics_frame, text="Добавить измерение", command=wrapper_metrics_add).pack()

    root.mainloop()
