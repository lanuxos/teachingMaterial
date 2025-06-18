# gui_entry.py
from tkinter import *

def get_entry(event):
    print(e1.get())
    # print(e2.get())

def delete_entry():
    e1.delete(0, END) # Clear from index 0 to END
    # e2.delete(0, END)

def insert_entry():
    e1.insert(0, 'Hello Python') # Insert at index 0
    # e2.insert(0, 'Hello World')

root = Tk()
root.title('Widget - Entry')

e1 = Entry(root)
e1.config(
    selectbackground='black',
    selectforeground='cyan'
    )
e1.pack()

# e2 = Entry(root, selectbackground='red', selectforeground='yellow', selectborderwidth=5)
# e2.pack()

root.bind('<Return>', get_entry)
root.bind('<Escape>', lambda event: delete_entry()) # no need to pass event to delete_entry
root.bind('<Control-i>', lambda event: insert_entry())
root.mainloop()
