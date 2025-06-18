# calc 5
import tkinter as tk

def button_click_function(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + number)

def button_clear_function():
    display.delete(0, tk.END)

def button_operation_function(operator):
    global first_number
    global math_operation
    first_number = float(display.get())
    math_operation = operator
    display.delete(0, tk.END)

def button_equal_function():
    second_number = float(display.get())
    display.delete(0, tk.END)
    if math_operation == "+":
        display.insert(0, first_number + second_number)
    elif math_operation == "-":
        display.insert(0, first_number - second_number)
    elif math_operation == "*":
        display.insert(0, first_number * second_number)
    elif math_operation == "/":
        if second_number == 0:
            display.insert(0, "Error!")
        else:
            display.insert(0, first_number / second_number)

root = tk.Tk()
root.title("WE DO IT! Calculator")

for i in range(5):  # 5 rows
    root.grid_rowconfigure(i, weight=1, uniform="rows")
for i in range(4):  # 4 cols
    root.grid_columnconfigure(i, weight=1, uniform="cols")

display = tk.Entry(root, width=30, borderwidth=5)
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

button_clear_function_widget = tk.Button(
    root, text="C", command=button_clear_function
)
button_clear_function_widget.grid(row=0, column=3, sticky="nsew", padx=10, pady=10,)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
]

row_val = 1
col_val = 0

for button_text in buttons:
    if button_text == "=":
        button = tk.Button(
            root, text=button_text, padx=20, pady=20, command=button_equal_function,
        )
    elif button_text in ["+", "-", "*", "/"]:
        button = tk.Button(
            root,
            text=button_text,
            padx=20,
            pady=20,
            command=lambda op=button_text: button_operation_function(op),
        )
    else:
        button = tk.Button(
            root,
            text=button_text,
            padx=20,
            pady=20,
            command=lambda num=button_text: button_click_function(num),
        )
    button.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
        if row_val == 5:  # = button
            col_val = 2

root.mainloop()
