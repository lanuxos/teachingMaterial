# gui_scrollbar.py
from tkinter import *

root = Tk()
root.title('Widget - Scrollbar')

sc1 = Scrollbar(root)
sc1.pack(side=RIGHT, fill=Y)

lb1 = Listbox(root, yscrollcommand=sc1.set)

for i in range(1, 100):
    lb1.insert(END, 'LINE' + str(i))

lb1.pack()

sc1.config(command=lb1.yview)

root.mainloop()
