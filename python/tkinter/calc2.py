# calc 2
import tkinter as tk

def button_clicked(event):
    print("\nBUTTON_CLICKED!!!")

root = tk.Tk()
root.title("Basic Widget Grid Layout + Event")

label_instruction = tk.Label(root, text="Click on:")
label_instruction.grid(row=0, column=0)

button = tk.Button(root, text="Me")
button.bind("<Button-1>", button_clicked)
button.grid(row=0, column=1)

root.mainloop()
