from tkinter.ttk import *
from PIL import Image
from main_frame import MainFrame


class Mask(MainFrame):
    def __init__(self, master):
        super().__init__(master)
        self.init_ui()

    def init_ui(self):
        super().init_ui()
        Label(self, text="Наложить маску на оригинал").place(x=5, y=5)
        Button(self, text="Наложить маску", command=self.do_mask).place(x=5, y=25)

    def do_mask(self):
        blank = self.master.master.img_for_mask.point(lambda _: 0)
        cat_segmented = Image.composite(
                            self.master.master.img_for_mask,
                            blank, self.img)
        # cat_segmented.show()
        self.master.master.refresh_img(cat_segmented)
