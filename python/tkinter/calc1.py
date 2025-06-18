# calc 1
import tkinter as tk

root = tk.Tk()
root.title("Basic Widget")

label_name = tk.Label(root, text="Name:")
label_name.pack(side=tk.LEFT)

entry_name = tk.Entry(root)
entry_name.pack(side=tk.LEFT)

button_greet = tk.Button(root, text="Say Hi")
button_greet.pack()

root.mainloop()
