# gui_font.py
from tkinter import *
from tkinter import font


def increase():
    font_adjustable.config(size=font_adjustable.actual()["size"] + 2)


def decrease():
    font_adjustable.config(
        size=max(8, font_adjustable.actual()["size"] - 2)
    )  # min = 8


root = Tk()
root.title("Tkinter GUI Font")

font_normal = font.Font(
    family='Source Code Pro',
    size=20,
    weight='normal'
)

font_bold = font.Font(
    family='Times New Roman',
    size=18,
    weight=font.BOLD
)

font_italic = font.Font(
    family='Noto Sans Lao',
    size=25,
    slant='italic'
)

font_underline = font.Font(
    family='Courier New',
    size=30,
    underline=1
)

font_overstrike = font.Font(
    family='Arial',
    size=22,
    overstrike=1
)

font_adjustable = font.Font(
    family='Times',
    size=12,
)

L0 = Label(root)
L0.configure(
    text='ກຳນົດ Font ໂດຍກົງ',
    font=("Noto Sans Lao Looped", "16", "bold italic overstrike underline")
)
L0.pack()

L1 = Label(root)
L1.configure(
    text='normal font',
    font=font_normal
)
L1.pack()

L2 = Label(root)
L2.configure(
    text='BOLD font',
    font=font_bold
)
L2.pack()

L3 = Label(root)
L3.configure(
    text='italic font',
    font=font_italic
)
L3.pack()

L4 = Label(root)
L4.configure(
    text='underline',
    font=font_underline
)
L4.pack()

L5 = Label(root)
L5.configure(
    text='overstrike',
    font=font_overstrike
)
L5.pack()

inc = Button(root, text='Increase font size by 2', command=increase).pack()
inc = Button(root, text='Decrease font size by 2', command=decrease).pack()

L6 = Label(root, text='Adjustable', font=font_adjustable).pack()

root.mainloop()
