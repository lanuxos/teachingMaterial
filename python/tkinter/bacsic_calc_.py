from tkinter import *
from tkinter import font


def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(END, current + str(number))


def clear_function():
    display.delete(0, END)


def calc():
    try:
        express = display.get()
        result = eval(express)
        display.delete(0, END)
        display.insert(0, result)
    except:
        display.delete(0, END)
        display.insert(0, "Error")


root = Tk()
root.title("WE DO IT! Calculator")


for i in range(5):  # 5 rows
    root.grid_rowconfigure(
        i, 
        weight=1, 
        uniform="rows"
        )
for i in range(4):  # 4 cols
    root.grid_columnconfigure(
        i, 
        weight=1, 
        uniform="cols"
        )

display = Entry(
    root, width=30, 
    borderwidth=5, 
    justify=RIGHT, 
    )
display.grid(
    row=0, 
    column=0, 
    columnspan=3, 
    padx=10, 
    pady=10, 
    sticky="nsew")

clear_button = Button(
    root, text="C", 
    command=clear_function, 
    
)
clear_button.grid(
    row=0,
    column=3,
    sticky="nsew",
    padx=10,
    pady=10,
)

b7 = Button(
    root,
    text="7",
    padx=20,
    pady=20,
    command=lambda: button_click("7"),
)
b7.grid(
    row=1, 
    column=0, 
    padx=5, 
    pady=5
    )

b8 = Button(
    root,
    text="8",
    padx=20,
    pady=20,
    command=lambda: button_click("8"),
)
b8.grid(
    row=1, 
    column=1, 
    padx=5, 
    pady=5
    )

b9 = Button(
    root,
    text="9",
    padx=20,
    pady=20,
    command=lambda: button_click("9"),
)
b9.grid(
    row=1, 
    column=2, 
    padx=5, 
    pady=5
    )

b_divide = Button(
    root,
    text="/",
    padx=20,
    pady=20,
    command=lambda: button_click("/"),
)
b_divide.grid(
    row=1, 
    column=3, 
    padx=5, 
    pady=5
    )

b4 = Button(
    root,
    text="4",
    padx=20,
    pady=20,
    command=lambda: button_click("4"),
)
b4.grid(
    row=2, 
    column=0, 
    padx=5, 
    pady=5
    )

b5 = Button(
    root,
    text="5",
    padx=20,
    pady=20,
    command=lambda: button_click("5"),
)
b5.grid(
    row=2, 
    column=1, 
    padx=5, 
    pady=5
    )

b6 = Button(
    root,
    text="6",
    padx=20,
    pady=20,
    command=lambda: button_click("6"),
)
b6.grid(
    row=2, 
    column=2, 
    padx=5, 
    pady=5
    )

b_multiply = Button(
    root,
    text="*",
    padx=20,
    pady=20,
    command=lambda: button_click("*"),
)
b_multiply.grid(
    row=2, 
    column=3, 
    padx=5, 
    pady=5
    )

b1 = Button(
    root,
    text="1",
    padx=20,
    pady=20,
    command=lambda: button_click("1"),
)
b1.grid(
    row=3, 
    column=0, 
    padx=5, 
    pady=5
    )

b2 = Button(
    root,
    text="2",
    padx=20,
    pady=20,
    command=lambda: button_click("2"),
)
b2.grid(
    row=3, 
    column=1, 
    padx=5, 
    pady=5
    )

b3 = Button(
    root,
    text="3",
    padx=20,
    pady=20,
    command=lambda: button_click("3"),
)
b3.grid(
    row=3, 
    column=2, 
    padx=5, 
    pady=5
    )

b_minus = Button(
    root,
    text="-",
    padx=20,
    pady=20,
    command=lambda: button_click("-"),
)
b_minus.grid(
    row=3, 
    column=3, 
    padx=5, 
    pady=5
    )

b0 = Button(
    root,
    text="0",
    padx=20,
    pady=20,
    command=lambda: button_click("0"),
)
b0.grid(
    row=4, 
    column=0, 
    padx=5, 
    pady=5
    )

b_point = Button(
    root,
    text=".",
    padx=20,
    pady=20,
    command=lambda: button_click("."),
)
b_point.grid(
    row=4, 
    column=1, 
    padx=5, 
    pady=5
    )

b_equal = Button(
    root, text="=", 
    padx=20, 
    pady=20, 
    command=calc, 
    
    )
b_equal.grid(
    row=4, 
    column=2, 
    padx=5, 
    pady=5
    )

b_plus = Button(
    root,
    text="+",
    padx=20,
    pady=20,
    command=lambda: button_click("+"),
)
b_plus.grid(
    row=4, 
    column=3, 
    padx=5, 
    pady=5
    )

root.mainloop()
