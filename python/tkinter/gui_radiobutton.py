# gui_radiobutton.py
from tkinter import *

root = Tk()
root.title('Widget - Radiobutton')

var = IntVar()

rb1 = Radiobutton(root, text='Female', value=1, variable=var)
rb1.pack()
rb2 = Radiobutton(root, text='Male', value=2, variable=var)
rb2.pack()

root.mainloop()
