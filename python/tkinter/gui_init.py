# gui_init.py
# from tkinter import *
# root = Tk()
import tkinter

root = tkinter.Tk()

# root.title("First Python GUI with Tkinter")
# root.geometry("800x600")  # Set initial window size
# root.config(background="#DCD6F7")
# root.config(bg='lightgreen')
# # open in fullscreen w/o title bar
# root.attributes('-fullscreen', True)
# # open in maximum window w/ title bar
# root.state("zoomed")

tkinter.Button(root, text='Quit', command=root.destroy).pack()

root.mainloop()
