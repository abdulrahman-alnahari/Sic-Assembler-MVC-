import tkinter as tk
from tkinter import ttk
from typing import Callable


class Button(tk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.commands: list[Callable] = []
        self['command'] = self.run_commands

    def run_commands(self):
        for command in self.commands:
            command()


class TTKButton(ttk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.commands: list[Callable] = []
        self['command'] = self.run_commands

    def run_commands(self):
        for command in self.commands:
            command()
