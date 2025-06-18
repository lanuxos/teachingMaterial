# gui_canvas.py
from tkinter import *

root = Tk()
root.title('Widget - Canvas')

cv = Canvas(root, width=100, height=100)
cv.pack()

cv.create_rectangle(7, 7, 90, 90)
cv.create_line(7,7,45,45)
cv.create_arc(45,45,85,85)
cv.create_oval(25,50,50,75)

root.mainloop()
