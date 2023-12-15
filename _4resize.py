from tkinter.ttk import *
from PIL import Image
from main_frame import MainFrame


class Resize(MainFrame):
    def __init__(self, master):
        super().__init__(master)
        val = ['0.25', '0.5', '1', '2', '4']
        self.x = Combobox(self, values=val, state="readonly", width=5)
        self.y = Combobox(self, values=val, state="readonly", width=5)
        self.init_ui()

    def init_ui(self):
        super().init_ui()
        Label(self, text="Изменить размер").place(x=5, y=5)
        Label(self, text="По ширине:").place(x=5, y=25)
        self.x.set('1')
        self.x.place(x=5, y=45)
        Label(self, text="По высоте:").place(x=5, y=70)
        self.y.set('1')
        self.y.place(x=5, y=90)

        Button(self, text="Изменить", command=self.resize_img).place(x=5, y=115)

    def resize_img(self):
        width = int(float(self.x.get()) * self.img.width)
        height = int(float(self.y.get()) * self.img.height)
        temp_img = self.img.resize((width, height))
        self.master.master.refresh_img(temp_img)
