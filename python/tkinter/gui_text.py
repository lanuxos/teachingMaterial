# gui_text.py
from tkinter import *

root = Tk()
root.title('Widget - Text')

tx = Text(root)
tx.pack()

# tx.insert(END, "First line of text")
# tx.insert(END, "\nSecond line of text")

root.mainloop()
