# gui_geometry.py
from tkinter import *

root = Tk()
root.geometry("300x300")

# .pack()
pack_frame = Frame(root, bg="lightpink", pady=5)
pack_frame.pack(fill="x")
Button(pack_frame, text="File").pack(side="left")
Button(pack_frame, text="About").pack(side="left")

# .grid()
grid_frame = Frame(root, bg="lightgreen", pady=5)
grid_frame.pack(fill="x")
Label(grid_frame, text="Username:").grid(row=0, column=0)
Entry(grid_frame).grid(row=0, column=1)
Label(grid_frame, text="Password:").grid(row=1, column=0)
Entry(grid_frame).grid(row=1, column=1)

# .place()
place_frame = Frame(root, height=50, bg="lightyellow", pady=5)
place_frame.pack(fill="x")
Button(place_frame, text="Submit").place(relx=0.75, rely=0.5)

root.mainloop()
