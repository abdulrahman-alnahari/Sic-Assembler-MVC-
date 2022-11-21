from ..custom_widgets import Button, TTKButton
import tkinter.font as tkFont


class BasicButton(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=12)
        self["font"] = ft
        self["fg"] = "#222222"
        self["justify"] = "center"
        self.configure(border="1px")


# class BasicButton(TTKButton):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)