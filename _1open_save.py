from tkinter import *
from tkinter import filedialog as fd
from PIL import Image
from main_frame import MainFrame


class OpenSave(MainFrame):
    def __init__(self, master):
        super().__init__(master)
        self.file_name = ""
        self.init_ui()

    def init_ui(self):
        super().init_ui()
        Button(self, text="Открыть", command=self.open_file).pack(anchor=NW, padx=5, pady=5)
        Button(self, text="Сохранить", command=self.save_file).pack(anchor=NW, padx=5, pady=5)

    def open_file(self):
        file_name = fd.askopenfilename(filetypes=(("PNG files", "*.png"),
                                                  ("JPG files", "*.jpg"),
                                                  ("All files", "*.*")),
                                       defaultextension='',
                                       initialfile=self.file_name
                                       )
        if file_name != "":
            self.file_name = file_name
            with Image.open(file_name) as img:
                img.load()
                self.master.master.refresh_img(img)
                self.save()

    def save_file(self):
        self.file_name = fd.asksaveasfilename(filetypes=(("PNG files", "*.png"),
                                                         ("JPG files", "*.jpg"),
                                                         ("All files", "*.*")),
                                              defaultextension='',
                                              initialfile=self.file_name
                                              )
        if self.file_name != "":
            self.master.master.img.save(self.file_name)
