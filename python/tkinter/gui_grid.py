# gui_grid.py
from tkinter import *

root = Tk()
root.title(".grid()")

# row 1
b7 = Button(root, text='7')
b7.grid(row=0, column=0, padx=5, pady=5, ipadx=10, ipady=10, sticky='nsew')
b8 = Button(root, text='8')
b8.grid(row=0, column=1, padx=5, pady=5, ipadx=10, ipady=10, sticky='nsew')
b9 = Button(root, text='9')
b9.grid(row=0, column=2, padx=5, pady=5, ipadx=10, ipady=10, sticky='nsew')
b_div = Button(root, text='/')
b_div.grid(row=0, column=3, padx=5, pady=5, ipadx=10, ipady=10, sticky='nsew')
# row 2
b4 = Button(root, text='4')
b4.grid(row=1, column=0, padx=5, pady=5, ipadx=10, ipady=10, sticky='nsew')
b5 = Button(root, text='5')
b5.grid(row=1, column=1, padx=5, pady=5, ipadx=10, ipady=10, sticky='nsew')
b6 = Button(root, text='6')
b6.grid(row=1, column=2, padx=5, pady=5, ipadx=10, ipady=10, sticky='nsew')
b_mul = Button(root, text='X')
b_mul.grid(row=1, column=3, padx=5, pady=5, ipadx=10, ipady=10, sticky='nsew')
# row 3
b1 = Button(root, text='1')
b1.grid(row=2, column=0, padx=5, pady=5, ipadx=10, ipady=10, sticky='nsew')
b2 = Button(root, text='2')
b2.grid(row=2, column=1, padx=5, pady=5, ipadx=10, ipady=10, sticky='nsew')
b3 = Button(root, text='3')
b3.grid(row=2, column=2, padx=5, pady=5, ipadx=10, ipady=10, sticky='nsew')
b_sub = Button(root, text='-')
b_sub.grid(row=2, column=3, padx=5, pady=5, ipadx=10, ipady=10, sticky='nsew')
# row 4
b0 = Button(root, text='0')
b0.grid(row=3, column=0, padx=5, pady=5, ipadx=10, ipady=10, sticky='nsew')
b_equ = Button(root, text='=')
b_equ.grid(row=3, column=1, columnspan=2, padx=5, pady=5, ipadx=10, ipady=10, sticky='nsew')
b_plu = Button(root, text='+')
b_plu.grid(row=3, column=3, padx=5, pady=5, ipadx=10, ipady=10, sticky='nsew')

root.mainloop()
