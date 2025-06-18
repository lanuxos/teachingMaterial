# gui_spinbox.py
from tkinter import *

root = Tk()
root.title('Widget - Spinbox')

sb = Spinbox(root, from_=1, to=5)
sb.pack()

root.mainloop()
