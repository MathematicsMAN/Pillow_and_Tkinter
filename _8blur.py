from tkinter.ttk import *
from PIL import ImageFilter
from main_frame import MainFrame


class Blur(MainFrame):
    def __init__(self, master):
        super().__init__(master)
        val = [str(a) for a in range(1, 50)]
        self.step = Combobox(self, values=val, state="readonly", width=5)
        self.init_ui()

    def init_ui(self):
        super().init_ui()
        Label(self, text="Сделать блюр").place(x=5, y=5)
        Label(self, text="Глубина блюра:").place(x=5, y=25)
        self.step.set('20')
        self.step.place(x=5, y=46)
        Button(self, text="Сделать блюр", command=self.do_blur_img).place(x=60, y=45)

    def do_blur_img(self):
        temp_img = self.img.convert('L')
        num = int(self.step.get())
        temp_img = temp_img.filter(ImageFilter.BoxBlur(num))
        self.master.master.refresh_img(temp_img)
