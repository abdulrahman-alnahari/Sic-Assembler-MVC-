from .abstract import Controller, View, Model
from . import views as Views
from . import models as Models
from tkinter import messagebox


class MainController(Controller):
    def __init__(self, app, parent, view, model):
        super().__init__(app, parent, view, model)
        self.view: Views.SICAssemblyMain
        self.model: Models.SICAssemblerModel


class ChooseAssemblyFileController(Controller):
    def __init__(self, app, parent, view, model):
        super().__init__(app, parent, view, model)
        self.view: Views.ChooseAssemblyFileView
        self.model: Models.ChooseAssemblyFileModel
        self.filepath = None
        self.view.add_choose_file_btn_command(self.get_file_path)
        self.view.add_execute_btn_command(self.execute_command)

    def get_file_path(self):
        self.filepath = self.model.open_file_dialog()
        self.view.set_path_textbox(self.filepath)

    def execute_command(self):
        if self.filepath:
            self.app.global_data['values'] = self.model.execute_pass_one_code(self.filepath)
            if self.app.global_data['values']:
                self.app.global_data['status'] = True
            else:
                messagebox.showerror("Execution Error", "Error While Executing The Program")
                self.app.global_data['status'] = False
        else:
            messagebox.showerror("File Error", "Please Select File First")
            self.app.global_data['status'] = False


    def show(self):
        self.view.show()


class ShowGeneratedFilesController(Controller):
    def __init__(self, app, root, view, model):
        super().__init__(app, root, view, model)
        self.view: Views.ShowGeneratedFilesView
        self.model: Models.ShowGeneratedFilesModel

    def set_data(self):
        intermediate = self.model.get_intermediate_data()
        symboltab = self.model.get_symbol_tab_data()

        self.view.update_intermediate_textarea(intermediate)
        self.view.update_symbol_tab_textarea(symboltab)

    def show(self):
        self.set_data()
        self.view.show()


class ShowObjectProgramFileController(Controller):
    def __init__(self, app, root, view, model):
        super().__init__(app, root, view, model)
        self.view: Views.ShowObjectProgramFileView
        self.model: Models.ShowObjectProgramFileModel

    def execute(self):
        status = self.app.global_data['status']
        if status:
            values: dict = self.app.global_data['values']
            sym, optab, LOCCTR, start = values.values()
            result = self.model.execute_pass_two_code(sym, optab, LOCCTR, start)
            if result:
                self.view.update_object_file_textarea(self.model.get_object_code_data())
                self.show()
            else:
                messagebox.showerror('Error', 'Error While Running Pass Two')
        else:
            messagebox.showerror("Pass One Error", "Pass One Failed To Execute Successfully")

