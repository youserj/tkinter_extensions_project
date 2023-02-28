import tkinter as tk
from src.tKot import ScrollFrame


root = tk.Tk()
root.geometry("300x100")  # need set for pack use, for grid not need
fr = ScrollFrame(master=root)
fr.pack(side=tk.LEFT)
s = tk.Scrollbar(root, orient=tk.VERTICAL, command=fr.yview)
s.pack(side=tk.RIGHT, expand=True, fill=tk.Y, anchor=tk.E)
fr.yscrollcommand = s.set
for i in range(100):
    tk.Label(fr, text=i)
for i in range(10):
    tk.Button(fr, text=F"button#{i}")
root.mainloop()
