# calc 3
import tkinter as tk

root = tk.Tk()
root.title("Calculator Layout")

display = tk.Entry(root, width=30, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

b7 = tk.Button(root, text='7', padx=20, pady=20)
b7.grid(row=1, column=0, padx=5, pady=5)

b8 = tk.Button(root, text='8', padx=20, pady=20)
b8.grid(row=1, column=1, padx=5, pady=5)

b9 = tk.Button(root, text='9', padx=20, pady=20)
b9.grid(row=1, column=2, padx=5, pady=5)

b_divide = tk.Button(root, text='/', padx=20, pady=20)
b_divide.grid(row=1, column=3, padx=5, pady=5)

b4 = tk.Button(root, text='4', padx=20, pady=20)
b4.grid(row=2, column=0, padx=5, pady=5)

b5 = tk.Button(root, text='5', padx=20, pady=20)
b5.grid(row=2, column=1, padx=5, pady=5)

b6 = tk.Button(root, text='6', padx=20, pady=20)
b6.grid(row=2, column=2, padx=5, pady=5)

b_multiply = tk.Button(root, text='*', padx=20, pady=20)
b_multiply.grid(row=2, column=3, padx=5, pady=5)

b1 = tk.Button(root, text='1', padx=20, pady=20)
b1.grid(row=3, column=0, padx=5, pady=5)

b2 = tk.Button(root, text='2', padx=20, pady=20)
b2.grid(row=3, column=1, padx=5, pady=5)

b3 = tk.Button(root, text='3', padx=20, pady=20)
b3.grid(row=3, column=2, padx=5, pady=5)

b_minus = tk.Button(root, text='-', padx=20, pady=20)
b_minus.grid(row=3, column=3, padx=5, pady=5)

b0 = tk.Button(root, text='0', padx=20, pady=20)
b0.grid(row=4, column=0, padx=5, pady=5)

b_point = tk.Button(root, text='.', padx=20, pady=20)
b_point.grid(row=4, column=1, padx=5, pady=5)

b_equal = tk.Button(root, text='=', padx=20, pady=20)
b_equal.grid(row=4, column=2, padx=5, pady=5)

b_plus = tk.Button(root, text='+', padx=20, pady=20)
b_plus.grid(row=4, column=3, padx=5, pady=5)

# buttons = [
#     "7", "8", "9", "/",
#     "4", "5", "6", "*",
#     "1", "2", "3", "-",
#     "0", ".", "=", "+",
# ]

# row_val = 1 # start from row 1, row 0 is display
# col_val = 0 # start from col 0-3, four columns

# for button_text in buttons:

#     button = tk.Button(root, text=button_text, padx=20, pady=20)
#     button.grid(row=row_val, column=col_val, padx=5, pady=5)

#     col_val += 1            # add 1 by 1 column [0-3]
#     if col_val > 3:         # until col_val bigger than 3
#         col_val = 0         # reset col_val to zero
#         row_val += 1        # add 1 more row

root.mainloop()