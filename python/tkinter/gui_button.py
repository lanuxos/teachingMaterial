# gui_button.py
from tkinter import *

root = Tk()
root.title('Widget - Button')

b1 = Button(root, text='ກົດປຸ່ມນີ້')
b1.pack()

b2 = Button(root)
b2.configure(
    text='BUTTON_2',
    activebackground='black',
    activeforeground='yellow',
    cursor='spider'
)
b2.pack()

# b3 = Button(root, bitmap='error')
# b3.pack()

# Button(text='FLAT_BUTTON', relief=FLAT).pack(pady=5)
# Button(text='RAISED_BUTTON', relief=RAISED).pack(pady=5)
# Button(text='SUNKEN_BUTTON', relief=SUNKEN).pack(pady=5)
# Button(text='GROOVE_BUTTON', relief=GROOVE).pack(pady=5)
# Button(text='RIDGE_BUTTON', relief=RIDGE).pack(pady=5)

root.mainloop()
