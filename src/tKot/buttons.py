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


class StatusIcon:
    __c: tk.Canvas
    c_id: int
    __current: int
    __im: ImageTk
    __h: int
    __w: int

    def __init__(self, canvas: tk.Canvas, images: dict[int, Image]):
        self.__c = canvas
        """ canvas for widget """
        self.__c_id = -1
        """ Image canvas ID. -1 if not place """
        self.__images = images
        self.__current = 0
        self.__h = 100
        """icon height"""
        self.__w = 100
        """icon width"""

    def get_status(self) -> int:
        return self.__current

    def set_status(self, value: int):
        self.__im = ImageTk.PhotoImage(self.__images[value].resize((self.__h, self.__w)))
        self.__c.create_image()
        self.__current = value

    def place(self, x: int, y: int):
        """ place on canvas by x and y """
        self.__coords = x, y
        """ x, y image coordinates """
        if self.__c != -1:
            self.__c.delete(self.__c_id)
        # self.__c.create_rectangle(x + self.__shadow_depth, y + self.__shadow_depth,
        #                                x + self.__size + self.__shadow_depth, y + self.__size + self.__shadow_depth,
        #                                width=0,
        #                                fill='grey')
        # self.__c_id = self.__c.create_image(x + self.__shadow_depth * int(self.__status), y + self.__shadow_depth * int(self.__status),
        #                                     anchor=tk.NW,
        #                                     image=self.__tk_image)
        self.__c_id = self.__c.create_image(x, y,
                                            anchor=tk.NW,
                                            image=self.__im)
