# gui_listbox.py
from tkinter import *

root = Tk()
root.title('Widget - Listbox')

lb1 = Listbox(root)
lb1.insert(1, 'Python')
lb1.insert(2, 'Programming')
lb1.insert(3, 'GUI')
lb1.pack()

root.mainloop()
