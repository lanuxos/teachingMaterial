# gui_menu.py
from tkinter import *

root = Tk()
root.title("Widget - Menu")

menu_list = Menu(root)

root.config(menu=menu_list)

file_menu = Menu(menu_list)
# file_menu = Menu(menu_list, tearoff=0)    # upper dash line

menu_list.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

help_menu = Menu(menu_list)

menu_list.add_cascade(label="Help", menu=help_menu)

help_menu.add_command(label="About")

root.mainloop()
