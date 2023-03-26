"""main gui App module"""

__author__ = 'Kolbeko A.B.'

# built-in
import tkinter as tk
from typing import List, Dict, NoReturn
from functools import partial

# internal
from loaders import save_to_file
from loaders.const import Entities
from .raw_observer import RowsObserver
from ..const.params_keys import ParamsKeys
from ..const.hex_colors import HexColors
from ..const.ui_text import MEASUREMENT_FRAME_COLUMN_NAMES, OBJECT_FRAME_COLUMN_NAMES
from .handlers import quite_callback


components_inits = [
    {ParamsKeys.ENTRIES: OBJECT_FRAME_COLUMN_NAMES, ParamsKeys.TITLE: 'Object', ParamsKeys.X_RATIO: 0.6,
     ParamsKeys.Y_RATIO: 0.4, ParamsKeys.FRAME_NAME: Entities.OBJECT, ParamsKeys.BACKGROUND: HexColors.LIGHT_GREEN},
    {ParamsKeys.ENTRIES: MEASUREMENT_FRAME_COLUMN_NAMES, ParamsKeys.TITLE: 'Measurement', ParamsKeys.X_RATIO: 0.6,
     ParamsKeys.Y_RATIO: 0.4, ParamsKeys.FRAME_NAME: Entities.MEASUREMENT, ParamsKeys.BACKGROUND: HexColors.EGS_YELLOW}
]


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.x_scale = self.winfo_screenwidth()
        self.y_scale = self.winfo_screenheight()
        self.geometry(f'{self.x_scale}x{self.y_scale}')
        self.frames = {}
        self._init_components(components_inits)
        self._set_callbacks()

    def _init_components(self, observers_data: List[Dict]):
        observers_frame = tk.Frame(self)
        buttons_frame = tk.Frame(self, background=HexColors.LIGHT_GREEN,
                                 width=self.x_scale, height=self.y_scale)
        self._add_input_frames(observers_frame, observers_data)
        self._add_main_buttons(buttons_frame)
        observers_frame.pack(side=tk.LEFT, padx=50)
        buttons_frame.pack(side=tk.LEFT, padx=20)

    def _add_main_buttons(self, frame: tk.Frame):
        button = tk.Button(frame, text='save to xml', command=self.load_data_from_entries, bg=HexColors.BLUE)
        button.pack(side=tk.TOP)

    def _add_input_frames(self, frame: tk.Frame, components_data: List[Dict]):
        for content_data in components_data:
            init_data = {
                ParamsKeys.WIDTH: content_data.get(ParamsKeys.X_RATIO) * self.x_scale,
                ParamsKeys.HEIGHT: content_data.get(ParamsKeys.Y_RATIO) * self.y_scale,
                ParamsKeys.TITLE: content_data.get(ParamsKeys.TITLE),
                ParamsKeys.BACKGROUND: content_data.get(ParamsKeys.BACKGROUND)
            }

            nested_frame = RowsObserver(frame, **init_data)

            init_data.pop(ParamsKeys.TITLE)
            nested_frame.load_content(init_data, content_data)
            nested_frame.pack(side=tk.TOP)
            nested_frame.propagate(False)
            nested_frame.add_row()
            self.frames[content_data.get(ParamsKeys.FRAME_NAME)] = nested_frame

    def _set_callbacks(self):
        quite_wrapper = partial(quite_callback, self)
        self.protocol("WM_DELETE_WINDOW", quite_wrapper)

    def load_data_from_entries(self) -> NoReturn:
        """
        Method for save data from input boxes. Binded to button
        """
        result = {}
        for observer_name, observer in self.frames.items():
            observer_data = observer.load_data_from_entries()
            result[observer_name] = observer_data

        save_to_file(result)
