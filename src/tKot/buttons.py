import tkinter as tk
from PIL import Image, ImageTk


class Icon(tk.Widget):
    p_im: Image.Image | None
    im: ImageTk.PhotoImage | None
    info: str | None

    def __init__(self, master=None, **kw):
        self.p_im = kw.pop("pillow_image", None)
        if kw.pop("with_fix", None):
            kw["indicatoron"] = False
            tk.Widget.__init__(self, master, "checkbutton", kw)
        else:
            tk.Widget.__init__(self, master, "button", kw)
        self.im = None
        self.bind("<Configure>", self.__handle_configure)

    def __handle_configure(self, e: tk.Event):
        """auto change image size"""
        if self.p_im:
            h = self.winfo_height()
            """current button height"""
            self.im = ImageTk.PhotoImage(self.p_im.resize((h, h)))
            self.configure(image=self.im, width=h)
