# gui_pack_anchor.py
from tkinter import *

root = Tk()
root.title("Pack() Anchor Examples")
root.geometry("500x400")


# Create a frame with a border to visualize the allocated space
def create_frame(text, anchor_position):
    frame = Frame(root, bd=2, relief="groove", padx=10, pady=10)
    label = Label(frame, text=f"Anchor {anchor_position}", bg="lightblue")

    # Use pack with the specified anchor
    label.pack(anchor=anchor_position, expand=True)

    # Add descriptive text
    Label(frame, text=text).pack()
    return frame


# North-West(Top-left) Anchor
nw_frame = create_frame("Sticks to top-left", "nw")
nw_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

# North (Top) Anchor
n_frame = create_frame("Sticks to top", "n")
n_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

# North-East (Top-Right) Anchor
ne_frame = create_frame("Sticks to top-right", "ne")
ne_frame.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

# West (Left) Anchor
w_frame = create_frame("Sticks to left", "w")
w_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

# Center Anchor
center_frame = create_frame("Sticks to centered", "center")
center_frame.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

# East (Right) Anchor
e_frame = create_frame("Sticks to right", "e")
e_frame.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

# South-West (Bottom-left) Anchor
sw_frame = create_frame("Sticks to bottom-left", "sw")
sw_frame.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

# South (Bottom) Anchor
s_frame = create_frame("Sticks to bottom", "s")
s_frame.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

# South-East (Bottom-right) Anchor
se_frame = create_frame("Sticks to bottom-right", "se")
se_frame.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

# Configure grid weights
for i in range(3):
    root.grid_columnconfigure(i, weight=1)
for i in range(3):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
