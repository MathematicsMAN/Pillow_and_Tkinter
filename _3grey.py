from tkinter.ttk import *
from main_frame import MainFrame


class Grey(MainFrame):
    def __init__(self, master):
        super().__init__(master)
        self.init_ui()

    def init_ui(self):
        super().init_ui()
        Label(self, text="Сделать серым").place(x=5, y=5)
        Button(self, text="Сделать серым", command=self.do_grey_img).place(x=5, y=25)

    def do_grey_img(self):
        temp_img = self.img.convert("L")
        self.master.master.refresh_img(temp_img)
