from abc import ABC

from .abstract import Controller, View
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from .custom_widgets import Button
from typing import Any, Callable
from .components.buttons import BasicButton


class SICAssemblyMain(View):
    def build_gui(self):
        self.title_lbl = tk.Label(self.window)
        ft = tkFont.Font(family='Times', size=16)
        self.title_lbl["font"] = ft
        self.title_lbl["fg"] = "#333333"
        self.title_lbl["justify"] = "center"
        self.title_lbl.configure(text="SIC-Assembler")
        self.title_lbl.place(x=0, y=0, width=301, height=98)

        self.pass_one_btn = BasicButton(self.window)
        self.pass_one_btn.configure(text="Pass 1")
        self.pass_one_btn.place(x=90, y=80, width=120, height=59)

        self.pass_two_btn = BasicButton(self.window)
        self.pass_two_btn.configure(text="Pass 2")
        self.pass_two_btn.place(x=90, y=160, width=120, height=59)

    def pre_show(self):
        # setting title
        self.parent.title("Main")
        # setting window size
        width = 300
        height = 300
        screenwidth = self.parent.winfo_screenwidth()
        screenheight = self.parent.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.parent.geometry(alignstr)
        self.parent.resizable(width=False, height=False)

    def pass_one_btn_add_command(self, command: Callable):
        self.pass_one_btn.commands.append(command)

    def pass_two_btn_add_command(self, command: Callable):
        self.pass_two_btn.commands.append(command)

    def set_pass_one_command(self, fn: Callable):
        self.pass_one_btn['command'] = fn

    def set_pass_two_command(self, fn: Callable):
        self.pass_two_btn['command'] = fn


class ChooseAssemblyFileView(View):
    def build_gui(self):
        self.title_lbl = tk.Label(self.window)
        ft = tkFont.Font(family='Times', size=18)
        self.title_lbl["font"] = ft
        self.title_lbl["fg"] = "#333333"
        self.title_lbl["justify"] = "center"
        self.title_lbl.configure(text="Choose Input")
        self.title_lbl.place(x=0, y=0, width=300, height=44)
        # self.title_lbl.grid(row=0, column=0)

        self.sub_lbl = tk.Label(self.window)
        ft = tkFont.Font(family='Times', size=14)
        self.sub_lbl["font"] = ft
        self.sub_lbl["fg"] = "#333333"
        self.sub_lbl["justify"] = "center"
        self.sub_lbl.configure(text="File")
        self.sub_lbl.place(x=0, y=50, width=50, height=25)

        self.path_textbox = tk.Entry(self.window)
        self.path_textbox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.path_textbox["font"] = ft
        self.path_textbox["fg"] = "#333333"
        self.path_textbox["justify"] = "center"
        self.path_textbox.place(x=50, y=50, width=200, height=25)

        self.choose_file_btn = BasicButton(self.window)
        self.choose_file_btn.configure(text="*")
        self.choose_file_btn.place(x=260, y=50, width=30, height=25)


        self.execute_btn = BasicButton(self.window)
        self.execute_btn.configure(text="Execute")
        self.execute_btn.place(x=200, y=90, width=75, height=35)

        self.cancel_btn = BasicButton(self.window)
        self.cancel_btn.configure(text="Main")
        self.cancel_btn.place(x=110, y=90, width=75, height=35)

        self.data_btn = BasicButton(self.window)
        self.data_btn.configure(text="Data")
        self.data_btn.place(x=20, y=90, width=75, height=35)

    def set_path_textbox(self, value):
        self.path_textbox.delete(0, tk.END)
        self.path_textbox.insert(0, value)

    def set_choose_file_btn_command(self, fn: Callable):
        self.choose_file_btn['command'] = fn

    def set_execute_btn_command(self, fn: Callable):
        self.execute_btn['command'] = fn

    def add_choose_file_btn_command(self, fn: Callable):
        self.choose_file_btn.commands.append(fn)

    def add_execute_btn_command(self, fn: Callable):
        self.execute_btn.commands.append(fn)

    def add_cancel_btn_command(self, fn: Callable):
        self.cancel_btn.commands.append(fn)

    def add_data_btn_command(self, fn: Callable):
        self.data_btn.commands.append(fn)

    def pre_show(self):
        # setting title
        self.parent.title("Choose Assembly File")
        # setting window size
        width = 300
        height = 150
        screenwidth = self.parent.winfo_screenwidth()
        screenheight = self.parent.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.parent.geometry(alignstr)
        self.parent.resizable(width=False, height=False)


class ShowGeneratedFilesView(View):
    def build_gui(self):
        width = 38
        self.intermediate_lbl = tk.Label(self.window, text="Intermediate File", width=width)
        self.intermediate_lbl.grid(row=0, column=0)
        self.intermediate_textaea = tk.Text(self.window, width=width)
        self.intermediate_textaea.grid(row=1, column=0)

        self.symbol_tab_lbl = tk.Label(self.window, text="Symbol Tab File", width=width)
        self.symbol_tab_lbl.grid(row=0, column=1)
        self.symbol_tab_textaea = tk.Text(self.window, width=width)
        self.symbol_tab_textaea.grid(row=1, column=1)

        self.back_btn = BasicButton(self.window)
        self.back_btn.configure(text="Back")
        self.back_btn.grid(row=2, column=0, columnspan=2)

    def update_intermediate_textarea(self, data):
        self.intermediate_textaea.delete('1.0', tk.END)
        self.intermediate_textaea.insert('1.0', data)

    def update_symbol_tab_textarea(self, data):
        self.symbol_tab_textaea.delete('1.0', tk.END)
        self.symbol_tab_textaea.insert('1.0', data)

    def add_back_btn_command(self, fn: Callable):
        self.back_btn.commands.append(fn)

    def pre_show(self):
        # setting title
        self.parent.title("Generated Files")
        # setting window size
        width = 615
        height = 440
        screenwidth = self.parent.winfo_screenwidth()
        screenheight = self.parent.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.parent.geometry(alignstr)
        self.parent.resizable(width=False, height=False)


class ShowObjectProgramFileView(View):
    def build_gui(self):
        self.main_btn = BasicButton(self.window)
        self.main_btn.configure(text="Main")
        self.main_btn.grid(row=2, column=0)

        width = 38
        self.object_file_lbl = tk.Label(self.window, text="Object Program", width=width)
        self.object_file_lbl.grid(row=0, column=0)
        self.object_file_textaea = tk.Text(self.window, width=width)
        self.object_file_textaea.grid(row=1, column=0)

    def pre_show(self):
        # setting title
        self.parent.title("Object Program File")
        # setting window size
        width = 310
        height = 440
        screenwidth = self.parent.winfo_screenwidth()
        screenheight = self.parent.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.parent.geometry(alignstr)
        self.parent.resizable(width=False, height=False)

    def add_main_btn_command(self, fn: Callable):
        self.main_btn.commands.append(fn)

    def update_object_file_textarea(self, data):
        self.object_file_textaea.delete('1.0', tk.END)
        self.object_file_textaea.insert('1.0', data)
