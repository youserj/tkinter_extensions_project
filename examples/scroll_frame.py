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
fr.pack(side=tk.LEFT, fill=tk.BOTH, anchor=tk.W)  # both for decide available height of frame
fr.yscrollcommand = s.set
fr1 = tk.LabelFrame(fr, text="title1")
for i in range(2):
    tk.Radiobutton(fr1, text=f"___________________new#{i}").pack(anchor=tk.W)
    tk.Radiobutton(fr1, text=f"__________new#{i}").pack(anchor=tk.W)
fr2 = tk.LabelFrame(fr, text="title2")
for i in range(4):
    tk.Radiobutton(fr2, text=f"new#{i}").pack()
# for i in range(10):
#     tk.Label(fr, text=i)
# for i in range(10):
#     tk.Button(fr, text=F"button#{i}")
root.mainloop()
