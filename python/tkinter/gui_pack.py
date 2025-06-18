# gui_pack.py
from tkinter import *

root = Tk()
root.title('Geometry Management - Pack()')
root.geometry("400x500")

b0 = Button(root, relief=RAISED, text="0_expand_false")
b0.pack(padx=5, pady=10, expand=False)
b1 = Button(root, relief=RAISED, text="1_expand_true")
b1.pack(padx=5, pady=10, expand=True)
b2 = Button(root, relief=RAISED, text="2_fill_x")
b2.pack(padx=5, pady=10, fill=X)
b3 = Button(root, relief=RAISED, text="3_fill_y")
b3.pack(padx=5, pady=10, fill=Y)
b4 = Button(root, relief=RAISED, text="4_fill_both")
b4.pack(padx=5, pady=10, fill=BOTH)
b5 = Button(root, relief=RAISED, text="5_side_top")
b5.pack(padx=5, pady=10, side=TOP)
b6 = Button(root, relief=RAISED, text="6_side_bottom")
b6.pack(padx=5, pady=10, side=BOTTOM)
b7 = Button(root, relief=RAISED, text="7_side_left")
b7.pack(padx=5, pady=10, side=LEFT)
b8 = Button(root, relief=RAISED, text="8_side_right")
b8.pack(padx=5, pady=10, side=RIGHT)
b9 = Button(root, relief=RAISED, text="9padx_ipady")
b9.pack(padx=5, pady=10, ipadx=25,ipady=15 )

root.mainloop()