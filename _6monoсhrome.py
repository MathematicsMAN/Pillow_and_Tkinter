from tkinter.ttk import *
from main_frame import MainFrame


class Monochrome(MainFrame):
    def __init__(self, master):
        super().__init__(master)
        val = [str(a) for a in range(256)]
        self.threshold = Combobox(self, values=val, state="readonly", width=5)
        self.init_ui()

    def init_ui(self):
        super().init_ui()
        Label(self, text="Сделать монохромным").place(x=5, y=5)
        Label(self, text="Градация чёрного:").place(x=5, y=25)
        self.threshold.set('64')
        self.threshold.place(x=5, y=46)

        Button(self, text="Изменить", command=self.do_mono_img).place(x=60, y=45)

    def do_mono_img(self):
        threshold = int(self.threshold.get())
        temp_img = self.img.point(
            lambda x: 255 if x > threshold else 0
        )
        temp_img = temp_img.convert("1")
        self.master.master.refresh_img(temp_img)
