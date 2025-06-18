# gui_pannedwindow.py
from tkinter import *

pw1 = PanedWindow()
pw1.pack(fill=BOTH, expand=1)
left = Entry(pw1, bd=5)
pw1.add(left)

pw2 = PanedWindow(pw1, orient=VERTICAL)
pw1.add(pw2)
top = Scale(pw2, orient=HORIZONTAL)
pw2.add(top)

mainloop()
