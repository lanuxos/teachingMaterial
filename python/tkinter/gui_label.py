# gui_label.py
from tkinter import *

root = Tk()
root.title('Widget - Label')

Label(root, text='LABEL ສະແດງຂໍ້ຄວາມ').pack()

# L1 = Label(root, text='LABEL ສະແດງຂໍ້ຄວາມ')
# L1.pack()

# Label(root, text='LABEL + COLOR', background='black', foreground='cyan').pack()

# L2 = Label(root)
# L2.config(
#     text='Label + Config',
#     bg='black',
#     fg='yellow'
# )
# L2.pack()

# L3 = Label(root, text='borderwidth', borderwidth=15, relief=RAISED).pack()

L4 = Label(root, text='width and height', height=10, width=20, relief=GROOVE).pack()

L5 = Label(root, text='underline', underline=3).pack()

root.mainloop()
