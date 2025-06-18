# gui_scale.py
from tkinter import *

root = Tk()
root.title("Widget - Scale")

ver = Scale(root, from_=0, to=50)
ver.pack()

hor = Scale(root, from_=1, to=100, orient=HORIZONTAL)
hor.pack()

root.mainloop()
