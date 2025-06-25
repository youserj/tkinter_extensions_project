import tkinter as tk
from dataclasses import dataclass, field


@dataclass
class Toast:
    """ short information widget """
    master: tk.Misc
    duration: int = 3000
    color: str = "yellow"
    after_id: str = field(init=False, default=None)
    top: tk.Toplevel = field(init=False)

    def call(self, info: str):
        """ show info with deleting old instance """
        if self.after_id is not None:
            self.top.after_cancel(self.after_id)
            self.top.destroy()
        x, y = self.master.winfo_pointerxy()
        self.top = tk.Toplevel(self.master, width=0, height=0)
        self.top.wm_overrideredirect(True)
        self.top.geometry(F"+{x}+{y}")
        tk.Label(self.top, text=info, bg=self.color).pack()
        self.after_id = self.top.after(self.duration, self.top.destroy)
