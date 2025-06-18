# gui_checkbutton.py
from tkinter import *

root = Tk()
root.title('Widget - Checkbutton')

var = IntVar()

cb1 = Checkbutton(root, text='Check Me', variable=var)
cb1.pack()

root.mainloop()
