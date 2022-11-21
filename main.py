import tkinter as tk
from assembler.views import SICAssemblyMain, ChooseAssemblyFileView, ShowGeneratedFilesView, ShowObjectProgramFileView
from assembler.controller import MainController, ChooseAssemblyFileController, ShowGeneratedFilesController, ShowObjectProgramFileController
from assembler.models import SICAssemblerModel, ChooseAssemblyFileModel, ShowGeneratedFilesModel, ShowObjectProgramFileModel


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.main_controller = MainController(self, self.root, SICAssemblyMain, SICAssemblerModel)
        self.choose_assembly_file_controller = ChooseAssemblyFileController(self, self.root, ChooseAssemblyFileView, ChooseAssemblyFileModel)
        self.show_generated_files_controller = ShowGeneratedFilesController(self, self.root, ShowGeneratedFilesView, ShowGeneratedFilesModel)
        self.show_object_program_file = ShowObjectProgramFileController(self, self.root, ShowObjectProgramFileView, ShowObjectProgramFileModel)
        self.global_data = {'status': False, 'values': None}

    def routes(self):
        # Main Controller
        self.main_controller.view.pass_one_btn_add_command(self.choose_assembly_file_controller.show)
        self.main_controller.view.pass_two_btn_add_command(self.show_object_program_file.execute)

        # Choose Assembly Window
        self.choose_assembly_file_controller.view.add_cancel_btn_command(self.main_controller.show)
        self.choose_assembly_file_controller.view.add_execute_btn_command(self.execute_command)
        self.choose_assembly_file_controller.view.add_data_btn_command(self.show_generated_files_controller.show)

        # Show Generated File Window
        self.show_generated_files_controller.view.add_back_btn_command(self.choose_assembly_file_controller.show)

        # Show Object File Window
        self.show_object_program_file.view.add_main_btn_command(self.main_controller.show)

    def execute_command(self):
        if self.global_data['status']:
            self.show_generated_files_controller.show()

    def run(self):
        self.routes()
        self.main_controller.show()
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()



