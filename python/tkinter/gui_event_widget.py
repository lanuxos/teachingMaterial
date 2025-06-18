from tkinter import *


def on_button_click(event):
    clicked_button = event.widget  
    print(f"You clicked: {clicked_button['text']}")


root = Tk()
root.title("Event.widget Example")

button1 = Button(root, text="Button 1")
button1.pack(pady=5)
button1.bind("<Button-1>", on_button_click)  

button2 = Button(root, text="Button 2")
button2.pack(pady=5)
button2.bind("<Button-1>", on_button_click)

button3 = Button(root, text="Button 3")
button3.pack(pady=5)
button3.bind("<Button-1>", on_button_click)

root.mainloop()
