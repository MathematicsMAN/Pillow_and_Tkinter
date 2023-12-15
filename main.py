from tkinter import *
from tkinter import ttk
import sys
from setting import *
from PIL import Image
from pil_tk import WorkingWithImage
from _1open_save import OpenSave
from _2cut import Cut
from _3grey import Grey
from _4resize import Resize
from _5rgb import RGB
from _6monoсhrome import Monochrome
from _7focus import Focus
from _8blur import Blur
from _9mask import Mask


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.img = Image
        self.img_for_mask = Image
        self.load_img()
        self.notebook = ttk.Notebook(width=WIDTH_FRAME, height=HEIGHT_FRAME)
        self.picture_frame = WorkingWithImage()
        self.open_save_frame = OpenSave(self.notebook)
        self.cut_frame = Cut(self.notebook)
        self.grey_frame = Grey(self.notebook)
        self.resize_frame = Resize(self.notebook)
        self.rgb_frame = RGB(self.notebook)
        self.mono_frame = Monochrome(self.notebook)
        self.focus_frame = Focus(self.notebook)
        self.blur_frame = Blur(self.notebook)
        self.mask_frame = Mask(self.notebook)
        self.init_ui()

        self.mainloop()

    def set_geometry(self, width, height):
        self.geometry(f'{width}x{height}')

    def load_img(self):
        try:
            with Image.open('Cat1.png') as img:
                img.load()
            self.img = img
        except IOError:
            print("Unable to load image")
            sys.exit(1)

    def init_ui(self):
        self.title("Convert picture")
        self.notebook.place(x=5, y=5)
        self.picture_frame.place(x=5, y=HEIGHT_FRAME+28)
        self.open_save_frame.pack(fill=BOTH, expand=True)
        self.cut_frame.pack(fill=BOTH, expand=True)
        self.grey_frame.pack(fill=BOTH, expand=True)
        self.resize_frame.pack(fill=BOTH, expand=True)
        self.rgb_frame.pack(fill=BOTH, expand=True)
        self.mono_frame.pack(fill=BOTH, expand=True)
        self.focus_frame.pack(fill=BOTH, expand=True)
        self.blur_frame.pack(fill=BOTH, expand=True)
        self.mask_frame.pack(fill=BOTH, expand=True)
        self.notebook.add(self.open_save_frame, text="1.Open")
        self.notebook.add(self.cut_frame, text="2.Cut")
        self.notebook.add(self.grey_frame, text="3.Grey")
        self.notebook.add(self.resize_frame, text="4.Resize")
        self.notebook.add(self.rgb_frame, text="5.RGB")
        self.notebook.add(self.mono_frame, text="6.Monochrome")
        self.notebook.add(self.focus_frame, text="7.Focus")
        self.notebook.add(self.blur_frame, text="8.Blur")
        self.notebook.add(self.mask_frame, text="9.Mask")
        self.refresh_img(self.img)

    def refresh_img(self, img):
        self.img = img
        self.picture_frame.set_img(img)
        self.set_geometry(max(img.width, WIDTH_FRAME) + 10, img.height+HEIGHT_FRAME+10)

    def save_to_mask(self):
        self.img_for_mask = self.img


if __name__ == '__main__':
    MainWindow()
