# gui_grid_anchor.py
from tkinter import *

root = Tk()
root.title('Grid Anchor')

grid_frame = Frame(root, bd=2, relief="groove")
grid_frame.pack(fill="both", expand=True, padx=10, pady=5)

Label(grid_frame, text="grid() with sticky anchor:").grid(row=0, columnspan=3)

positions = [
    ("ANCHOR_NW", "nw", 1, 0),
    ("ANCHOR_N", "n", 1, 1),
    ("ANCHOR_NE", "ne", 1, 2),
    ("ANCHOR_W", "w", 2, 0),
    ("ANCHOR_CENTER", "", 2, 1),
    ("ANCHOR_E", "e", 2, 2),
    ("ANCHOR_SW", "sw", 3, 0),
    ("ANCHOR_S", "s", 3, 1),
    ("ANCHOR_SE", "se", 3, 2),
]

for text, anchor, row, col in positions:
    Label(grid_frame, text=text, bg="lightblue").grid(
        row=row, column=col, sticky=anchor, padx=5, pady=5
    )

# Configure grid weights
for i in range(4):
    grid_frame.grid_rowconfigure(i, weight=1)
for i in range(3):
    grid_frame.grid_columnconfigure(i, weight=1)

root.mainloop()
