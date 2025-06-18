# basic calculator using tkinter with ttk theme
# import tkinter as tk
from tkinter import *
from tkinter import ttk


def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(screen.get()))
            screen.set(result)
        except:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)


root = Tk()
root.title("Basic Calculator w/ ttk")

style = ttk.Style()
style.theme_use("clam")  # 'alt', 'default', 'classic'
# style.theme_use("alt")
# style.theme_use("default")
# style.theme_use("classic")

screen = StringVar()
entry = ttk.Entry(root, textvariable=screen, font="Arial 20")
entry.pack(fill=BOTH, ipadx=8)

button_frame = ttk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"],
]

for row in buttons:
    frame = ttk.Frame(button_frame)
    frame.pack()
    for btn in row:
        button = ttk.Button(frame, text=btn)
        button.pack(side=LEFT, padx=2, pady=2)
        button.bind("<Button-1>", click)

root.mainloop()
