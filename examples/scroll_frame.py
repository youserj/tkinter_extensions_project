import tkinter as tk
from src.tKot import ScrollFrame


root = tk.Tk()
root.geometry("300x100")  # need set for pack use, for grid not need
fr_head = tk.Frame(master=root, relief=tk.RIDGE, borderwidth=4)
fr_head.pack(side=tk.TOP, fill=tk.X)
tk.Label(fr_head, text="head").pack()
fr = ScrollFrame(master=root)
s = tk.Scrollbar(root, orient=tk.VERTICAL, command=fr.yview)
s.pack(side=tk.LEFT, expand=True, fill=tk.Y, anchor=tk.W)
fr.pack(side=tk.LEFT, fill=tk.X, anchor=tk.W)
fr.yscrollcommand = s.set
fr1 = tk.LabelFrame(fr, text="title1")
for i in range(4):
    tk.Label(fr1, text=f"___________________new#{i}").pack()
fr2 = tk.LabelFrame(fr, text="title2")
for i in range(4):
    tk.Label(fr2, text=f"new#{i}").pack()
root.after(ms=2000, func=lambda: print(fr1.winfo_reqheight()))
for i in range(10):
    tk.Label(fr, text=i)
for i in range(10):
    tk.Button(fr, text=F"button#{i}")
root.mainloop()
