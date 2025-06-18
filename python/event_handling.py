# event_handling.py
from tkinter import *

root = Tk()
root.title('Event Handling')
root.geometry('300x150')

def key_handling(event):
    print(event.char, event.keysym, event.keycode)
    character = event.char
    key = event.keysym
    code = event.keycode
    character_label.config(text=f'You pressed:\t {character}')
    key_label.config(text=f'You pressed:\t {key}')
    code_label.config(text=f"key code is:\t {code}")

character_label = Label(root, text="Press any key...")
character_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

key_label = Label(root, text='')
key_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

code_label = Label(root, text='')
code_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)

root.bind("<Key>", key_handling)

root.mainloop()
