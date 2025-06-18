# gui_place.py
from tkinter import *

root = Tk()
root.geometry("300x300")

Button(root, text=".place() with x y").place(x=10, y=70)
Button(root, text=".place() with relx/y").place(relx=0.5, rely=0.5)

root.mainloop()