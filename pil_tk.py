from tkinter import Tk
from tkinter.ttk import *
from PIL import ImageTk


class WorkingWithImage(Frame):
    def __init__(self):
        super().__init__()
        self.lbl = Label(self)
        self.init_ui()

    def init_ui(self):
        img_lbl = ImageTk.PhotoImage(self.master.img)
        self.lbl['image'] = img_lbl
        self.lbl.image = img_lbl
        self.lbl.pack(pady=3)
        self.pack(pady=3)

    def set_img(self, img):
        img_tk = ImageTk.PhotoImage(img)
        self.lbl['image'] = img_tk
        self.lbl.image = img_tk
