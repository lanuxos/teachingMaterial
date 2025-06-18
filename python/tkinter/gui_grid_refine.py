# gui_grid.py
from tkinter import *

root = Tk()
root.title("Geometry - .grid()")

# open in fullscreen w/o title bar
# root.attributes('-fullscreen', True)
# open in maximum window w/ title bar
root.state('zoomed')

# Configure grid weights for responsive resizing
# grid_rowconfigure(index, weight=1, uniform='rows')
# default weight value is 0 (do not scale along with window), 1 scale along, 2 twice
for i in range(4):  # 4 rows
    root.grid_rowconfigure(i, weight=1, uniform="rows")
    root.grid_columnconfigure(i, weight=1, uniform="cols")
# Row 0
b1 = Button(root, text="1-row_0-col_0")
b1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
b2 = Button(root, text="2-row_0-col_1")
b2.grid(row=0, column=1, columnspan=2, sticky="nsew", padx=5, pady=5)
b3 = Button(root, text="3-row_0-col_3")
b3.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)

# Row 1
b4 = Button(root, text="4-row_1-col_0")
b4.grid(row=1, column=0, rowspan=2, sticky="nsew", padx=5, pady=5)
b5 = Button(root, text="5-row_1-col_1")
b5.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
b6 = Button(root, text="6-row_1-col_2")
b6.grid(row=1, column=2, columnspan=2, rowspan=2, sticky="nsew", padx=5, pady=5)

# Rows 2-3
b7 = Button(root, text="7-row_2-col_1")
b7.grid(row=2, column=1, rowspan=2, sticky="nsew", padx=5, pady=5)

# Row 3
b8 = Button(root, text="8-row_3-col_0")
b8.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
b9 = Button(root, text="9-row_3-col_2")
b9.grid(row=3, column=2, columnspan=2, sticky="nsew", padx=5, pady=5)

root.bind(
    "<F11>",
    lambda e: root.attributes("-fullscreen", not root.attributes("-fullscreen")),
)

root.mainloop()
