# gui_widget.py
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('widget ໃນ tkinter')

frame = ttk.Frame(root, padding='5')
frame.grid()

ttk.Button(frame, text='Button').grid(column=0, row=0)
ttk.Checkbutton(frame, text='Checkbutton').grid(column=1, row=0)
ttk.Entry(frame).grid(column=2, row=0)
ttk.Label(frame, text='Label').grid(column=3, row=0)
ttk.LabelFrame(frame).grid(column=0, row=1)
ttk.Menubutton(frame, text='Menubutton').grid(column=1, row=1)
ttk.PanedWindow(frame).grid(column=2, row=1)
ttk.Radiobutton(frame, text='Radiobutton').grid(column=3, row=1)
ttk.Scale(frame, from_=0, to=100).grid(column=0, row=2)
ttk.Scrollbar(frame).grid(column=1, row=2)
ttk.Spinbox(frame, from_=1, to=5).grid(column=2, row=2)
ttk.Combobox(frame, text='Combobox').grid(column=3, row=2)
ttk.Notebook(frame).grid(column=0, row=3)
ttk.Progressbar(frame).grid(column=1, row=3)
ttk.Separator(frame).grid(column=2, row=3)
ttk.Sizegrip(frame).grid(column=3, row=3)
ttk.Treeview(frame).grid(columnspan=4, row=4)

root.mainloop()
