import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod
from typing import Any, Callable



class View(ABC):
    def __init__(self, parent: tk.Tk):
        self.window = ttk.Frame(parent)
        self.parent = parent
        self.build_gui()

    def pre_show(self):
        pass

    def pre_hide(self):
        pass

    @abstractmethod
    def build_gui(self):
        """"""

    def _clear(self):
        for child in self.parent.winfo_children():
            child.pack_forget()

    def hide(self):
        self.pre_hide()
        self.window.pack_forget()

    def show(self):
        self._clear()
        self.pre_show()
        self.window.pack(fill='both', expand=True)


class Model(ABC):
    pass


class Controller(ABC):
    def __init__(self, app: Any, root: tk.Tk, view: Callable[[Any], View], model: Callable[[], Model]):
        self.view = view(root)
        self.model = model()
        self.app = app

    def hide(self):
        self.view.hide()

    def show(self):
        self.view.show()