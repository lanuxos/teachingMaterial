# basic calculator with tkinter classic tk module
import tkinter as tk


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


root = tk.Tk()
root.title("Calculator (tk)")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"],
]

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack()
    for btn in row:
        button = tk.Button(frame, text=btn, font="Arial 18", height=2, width=5)
        button.pack(side=tk.LEFT, padx=2, pady=2)
        button.bind("<Button-1>", click)

root.mainloop()
