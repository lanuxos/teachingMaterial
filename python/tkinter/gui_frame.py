# gui_frame.py
from tkinter import *

root = Tk()
root.title("Widget - Frame")

frame = Frame(root, bg='lightgreen')
frame.pack()

frame_label = Label(frame, text='FRAME').pack()
frame_entry = Entry(frame).pack()
frame_button = Button(frame, text='BTN').pack()

root_label = Label(root, text='ROOT').pack()

root.mainloop()