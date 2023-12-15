from tkinter.ttk import *
from main_frame import MainFrame


class RGB(MainFrame):
    def __init__(self, master):
        super().__init__(master)
        self.init_ui()

    def init_ui(self):
        super().init_ui()
        Label(self, text="Посмотреть:").place(x=5, y=5)
        Button(self, text="Красный", command=lambda:self.show_img("red")).place(x=5, y=25)
        Button(self, text="Зелёный", command=lambda:self.show_img("green")).place(x=5, y=50)
        Button(self, text="Синий", command=lambda:self.show_img("blue")).place(x=5, y=75)

        Label(self, text="Применить:").place(x=90, y=5)
        Button(self, text="Красный", command=lambda:self.apply_img("red")).place(x=90, y=25)
        Button(self, text="Зелёный", command=lambda:self.apply_img("green")).place(x=90, y=50)
        Button(self, text="Синий", command=lambda:self.apply_img("blue")).place(x=90, y=75)

    def show_img(self, col):
        red, green, blue, a = self.img.split()
        if col == 'red':
            red.show()
        elif col == 'green':
            green.show()
        elif col == 'blue':
            blue.show()

    def apply_img(self, col):
        red, green, blue, a = self.img.split()
        if col == 'red':
            self.master.master.refresh_img(red)
        elif col == 'green':
            self.master.master.refresh_img(green)
        elif col == 'blue':
            self.master.master.refresh_img(blue)
