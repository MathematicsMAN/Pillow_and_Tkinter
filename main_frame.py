from tkinter import *
from PIL import ImageTk
from setting import *


class MainFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.width = WIDTH_FRAME
        self.height = HEIGHT_FRAME
        self.img = self.master.master.img
        self.lbl = Label(self)

    def init_ui(self):
        Button(self, text="Сохранить текущее", command=self.save).place(x=170, y=5)
        Button(self, text="Восстановить", command=self.recover).place(x=170, y=35)
        self.load_mini_img()

    def save(self):
        self.img = self.master.master.img
        self.load_mini_img()

    def recover(self):
        self.master.master.refresh_img(self.img)

    def load_mini_img(self):
        k = HEIGHT_FRAME/ self.img.height
        img_lbl = self.img.resize((int(self.img.width * k), HEIGHT_FRAME - 5))
        img_lbl = ImageTk.PhotoImage(img_lbl)
        self.lbl['image'] = img_lbl
        self.lbl.image = img_lbl
        self.lbl.place(x=300, y=3)


