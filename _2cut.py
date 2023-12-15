from tkinter.ttk import *
from main_frame import MainFrame


class Cut(MainFrame):
    def __init__(self, master):
        super().__init__(master)
        self.x1 = Entry(self, width=4)
        self.x2 = Entry(self, width=4)
        self.y1 = Entry(self, width=4)
        self.y2 = Entry(self, width=4)
        self.init_ui()

    def init_ui(self):
        super().init_ui()
        Label(self, text="x1").place(x=5, y=5)
        Label(self, text="x2").place(x=5, y=25)
        Label(self, text="y1").place(x=5, y=45)
        Label(self, text="y2").place(x=5, y=65)
        self.x1.insert(0, "780")
        self.x1.place(x=30, y=5)
        self.x2.insert(0, "1700")
        self.x2.place(x=30, y=25)
        self.y1.insert(0, "210")
        self.y1.place(x=30, y=45)
        self.y2.insert(0, "1200")
        self.y2.place(x=30, y=65)
        Button(self, text="Вырезать", command=self.cut_img).place(x=80, y=65)
        Button(self, text="Сохранить для маски", command=self.save_to_mask).place(x=80, y=90)

    def cut_img(self):
        x1 = int(self.x1.get())
        x2 = int(self.x2.get())
        y1 = int(self.y1.get())
        y2 = int(self.y2.get())
        temp_img = self.img.crop((x1, y1, x2, y2))
        self.master.master.refresh_img(temp_img)

    def save_to_mask(self):
        self.master.master.save_to_mask()

