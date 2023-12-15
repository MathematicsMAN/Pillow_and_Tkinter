from tkinter.ttk import *
from PIL import Image, ImageFilter
from main_frame import MainFrame


class Focus(MainFrame):
    def __init__(self, master):
        super().__init__(master)
        eros_lst = [str(a) for a in range(1, 50)]
        self.eros = Combobox(self, values=eros_lst, state="readonly", width=5)
        delat_lst = [str(a) for a in range(1, 50)]
        self.dilat = Combobox(self, values=delat_lst, state="readonly", width=5)
        self.init_ui()

    def init_ui(self):
        super().init_ui()
        Label(self, text="Выделить главный объект").place(x=5, y=5)
        Label(self, text="Уровень эрозии:").place(x=5, y=25)
        self.eros.set('18')
        self.eros.place(x=5, y=46)
        Button(self, text="Изменить",
               command=lambda:self.do_eros_img(int(self.eros.get()))
               ).place(x=60, y=45)

        Label(self, text="Уровень дилатации:").place(x=5, y=75)
        self.dilat.set('44')
        self.dilat.place(x=5, y=96)
        Button(self, text="Изменить",
               command=lambda:self.do_dilat_img(int(self.dilat.get()))
               ).place(x=60, y=95)

    def do_eros_img(self, eros_num):
        temp_img = self.master.master.img
        for _ in range(eros_num):
            temp_img = temp_img.filter(ImageFilter.MinFilter(3))
        self.master.master.refresh_img(temp_img)

    def do_dilat_img(self, dilat_num):
        temp_img = self.master.master.img
        for _ in range(dilat_num):
            temp_img = temp_img.filter(ImageFilter.MaxFilter(3))
        self.master.master.refresh_img(temp_img)
