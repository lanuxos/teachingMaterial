# gui_buttonmenu.py
from tkinter import *

root = Tk()
root.title("Widget - Button Menu")

bm = Menubutton(root, text="Button-Menu")
bm.pack()

bm.menu = Menu(bm, tearoff=0)
bm["menu"] = bm.menu

menu_button_1_var = IntVar()
menu_button_2_var = IntVar()

bm.menu.add_checkbutton(label="menu_button_1", variable=menu_button_1_var)
bm.menu.add_checkbutton(label="menu_button_2", variable=menu_button_2_var)

bm.pack()

root.mainloop()
