# calc 4
import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + number)

root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, width=30, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
]

row_val = 1
col_val = 0

for button_text in buttons:
    button = tk.Button(
        root,
        text=button_text,
        padx=20,
        pady=20,
        command=lambda b=button_text: button_click(b),
    )
    button.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
