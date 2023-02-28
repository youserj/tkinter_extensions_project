from src.tKot import Icon
from PIL import Image
import tkinter as tk
from data import images

root = tk.Tk()
but = Icon(master=root,
           pillow_image=Image.frombytes('RGB', (100, 100), images.connected),
           text="message"
           )
but.place(relx=0.1, rely=0.1, relheight=0.8)
root.mainloop()
