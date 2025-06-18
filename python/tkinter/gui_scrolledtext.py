# gui_scrolledtext.py
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

root = tk.Tk()
root.title("Widget - ScrolledText")

ttk.Label(
    root,
    text="Widget - ScrolledText",
    font=("Times New Roman", 15),
    background="green",
    foreground="white",
).pack()

st = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, width=40, height=10, font=("Times New Roman", 15)
)

st.pack()
st.focus()

root.mainloop()
