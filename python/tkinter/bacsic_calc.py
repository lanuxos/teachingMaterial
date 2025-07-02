# basic_calc.py
'''
UI
button_click
clear_button
calculate
keypress
font_resize
'''
from tkinter import *
from tkinter import font


def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(END, current + str(number))


def button_clear_function():
    display.delete(0, END)


def calc():
    try:
        express = display.get()
        result = eval(express)
        display.delete(0, END)
        display.insert(0, result)
    except:
        """
        eval("5 +")
        eval("5 / 0")
        ...
        """
        display.delete(0, END)
        display.insert(0, "Error")


def handle_keypress(event):
    # Number keys
    if event.char in '0123456789':
        button_click(event.char)
    # Operator keys
    elif event.char in '+-*/':
        button_click(event.char)
    # Decimal point
    elif event.char == '.':
        button_click('.')
    # Enter/Return for calculation
    elif event.keysym == 'Return' or 'KP_Enter':
        calc()
    # Escape for clear
    elif event.keysym == 'Escape':
        button_clear_function()
    # Backspace for deleting last character
    elif event.keysym == 'BackSpace':
        current = display.get()
        display.delete(0, END)
        display.insert(0, current[:-1])


def font_resize(event):
    # resize = max(10, int(event.height / 10))
    resize = max(10, min(48, int(event.height // 5)))
    dynamic_font.configure(size=resize)
    event.widget.config(
        pady=resize // 2, padx=resize // 2, ipady=resize // 2, ipadx=resize // 2
    )


root = Tk()
root.title("WE DO IT! Calculator")

dynamic_font = font.Font(family="Noto Sans Lao", size=12)

for i in range(5):  # 5 rows
    root.grid_rowconfigure(i, weight=1, uniform="rows")
for i in range(4):  # 4 cols
    root.grid_columnconfigure(i, weight=1, uniform="cols")

display = Entry(root, width=30, borderwidth=5, font=dynamic_font)
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

button_clear_function_widget = Button(
    root, text="C", command=button_clear_function, font=dynamic_font
)
button_clear_function_widget.grid(
    row=0,
    column=3,
    sticky="nsew",
    padx=10,
    pady=10,
)

b7 = Button(root, text='7', padx=20, pady=20, command=lambda x='7': button_click(x), font=dynamic_font)
b7.grid(row=1, column=0, padx=5, pady=5)

b8 = Button(root, text='8', padx=20, pady=20, command=lambda x='8': button_click(x), font=dynamic_font)
b8.grid(row=1, column=1, padx=5, pady=5)

b9 = Button(root, text='9', padx=20, pady=20, command=lambda x='9': button_click(x), font=dynamic_font)
b9.grid(row=1, column=2, padx=5, pady=5)

b_divide = Button(root, text='/', padx=20, pady=20, command=lambda x='/': button_click(x), font=dynamic_font)
b_divide.grid(row=1, column=3, padx=5, pady=5)

b4 = Button(root, text='4', padx=20, pady=20, command=lambda x='4': button_click(x), font=dynamic_font)
b4.grid(row=2, column=0, padx=5, pady=5)

b5 = Button(root, text='5', padx=20, pady=20, command=lambda x='5': button_click(x), font=dynamic_font)
b5.grid(row=2, column=1, padx=5, pady=5)

b6 = Button(root, text='6', padx=20, pady=20, command=lambda x='6': button_click(x), font=dynamic_font)
b6.grid(row=2, column=2, padx=5, pady=5)

b_multiply = Button(root, text='*', padx=20, pady=20, command=lambda x='*': button_click(x), font=dynamic_font)
b_multiply.grid(row=2, column=3, padx=5, pady=5)

b1 = Button(root, text='1', padx=20, pady=20, command=lambda x='1': button_click(x), font=dynamic_font)
b1.grid(row=3, column=0, padx=5, pady=5)

b2 = Button(root, text='2', padx=20, pady=20, command=lambda x='2': button_click(x), font=dynamic_font)
b2.grid(row=3, column=1, padx=5, pady=5)

b3 = Button(root, text='3', padx=20, pady=20, command=lambda x='3': button_click(x), font=dynamic_font)
b3.grid(row=3, column=2, padx=5, pady=5)

b_minus = Button(root, text='-', padx=20, pady=20, command=lambda x='-': button_click(x), font=dynamic_font)
b_minus.grid(row=3, column=3, padx=5, pady=5)

b0 = Button(root, text='0', padx=20, pady=20, command=lambda x='0': button_click(x), font=dynamic_font)
b0.grid(row=4, column=0, padx=5, pady=5)

b_point = Button(root, text='.', padx=20, pady=20, command=lambda x='.': button_click(x), font=dynamic_font)
b_point.grid(row=4, column=1, padx=5, pady=5)

b_equal = Button(root, text="=", padx=20, pady=20, command=calc, font=dynamic_font)
b_equal.grid(row=4, column=2, padx=5, pady=5)

b_plus = Button(root, text='+', padx=20, pady=20, command=lambda x='+': button_click(x), font=dynamic_font)
b_plus.grid(row=4, column=3, padx=5, pady=5)

root.bind('<Key>', handle_keypress)
root.bind('<Configure>', font_resize)

root.mainloop()
