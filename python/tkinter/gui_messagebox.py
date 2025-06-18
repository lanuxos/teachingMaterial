# gui_messagebox.py
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Widget - Message Box")

Label(root, text="Message Box").pack()

messagebox.showinfo("Information", "Show Info Message Box")

messagebox.showwarning("Warning", "Show Warning Message Box")

messagebox.showerror("Error", "Show Error Message Box")

messagebox.askquestion("Are you sure?", "Confirm Message Box")

messagebox.askokcancel("Want to continue?", "Confirm Cancel Message Box")

messagebox.askyesno("Find the value?", "Yes or No Message Box")


messagebox.askretrycancel("Try again?", "Try again or cancel Message Box")

root.mainloop()
