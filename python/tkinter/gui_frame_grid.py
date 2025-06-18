# gui_frame_grid.py
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('ໂປຣແກຣມຂຽນດ້ວຍພາສາ Python')

frame = ttk.Frame(root, padding="2 3 4 5", cursor="trek")
frame.grid(column=0, row=0, sticky=(N, W, E, S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

ttk.Label(frame, text='ຂໍ້ຄວາມ/Label').grid(column=0, row=0)
ttk.Button(frame, text='ປຸ່ມກົດ/Button').grid(column=1, row=0)
ttk.Checkbutton(frame, text='ປຸ່ມຕິກ/checkbox').grid(column=2, row=0)
ttk.Button(frame, text='ປິດ/Quit', command=root.destroy).grid(column=2, row=1)

root.mainloop()
