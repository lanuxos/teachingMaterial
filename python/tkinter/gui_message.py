# gui_message.py
from tkinter import *

root = Tk()
root.title("Widget - Message")
root.geometry("300x200")  # Set initial window size

display_message = "Display long message on screen and adjust the message format automatically, suit for display long text more than label widget that suit for short text"

ms = Message(root, text=display_message)
# ms.config(bg='lightblue')
ms.pack()

root.mainloop()
