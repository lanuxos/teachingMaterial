# gui_combobox.py
from tkinter import *
from tkinter import ttk


def select(event):
    selected_item = combo_box.get()
    label.config(text="You have selected: " + selected_item)


root = Tk()
root.title("Widget - Combobox")

# Create a label
label = Label(root, text="Select one option below")
label.pack(pady=10)

# Create a Combobox widget
combo_box = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combo_box.pack(pady=5)

# Set default value
combo_box.set("Option 1")

# Bind event to selection
combo_box.bind("<<ComboboxSelected>>", select)

root.mainloop()