import tkinter as tk
from PIL import Image, ImageTk


class Icon(tk.Button):
    p_im: Image.Image | None
    im: ImageTk.PhotoImage | None

    def __init__(self, *args,
                 pillow_image: Image = None):
        super(Icon, self).__init__(*args)
        self.p_im = pillow_image
        self.im = None
        self.bind("<Configure>", self.__handle_configure)

    def __handle_configure(self, e: tk.Event):
        """auto change image size"""
        if self.p_im:
            h = self.winfo_height()
            """current button height"""
            self.im = ImageTk.PhotoImage(self.p_im.resize((h, h)))
            self.configure(image=self.im, width=h)
