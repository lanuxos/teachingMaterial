# digital_clock.py

from tkinter import *
from time import strftime
from turtle import update

def update_time():
    current_time = strftime('%Y/%m/%d | %H:%M:%S %p')
    display.config(text=current_time)
    display.after(1000, update_time)  # Update every second

root = Tk()
root.title("Digital Clock")

display = Label(root, font=('Courier', 40, 'bold'), background='black', foreground='cyan')
display.pack(anchor='center', fill='both', expand=True)

update_time() 

root.mainloop()  