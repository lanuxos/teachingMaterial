# counterClick.py
import glob
from tkinter import *
from tkinter import font


def font_resize(event):
    resize = max(8, int(event.height / 13))
    dynamic_font.configure(size=resize)


save_state = False
def save_info():
    global save_state
    if not save_state:
        save_state = True
        a.config(state='disabled')
        goal.config(state='disabled')
        b.config(state='disabled')
        save.config(text='Saved')
    else:
        save_state = False
        a.config(state='normal')
        goal.config(state='normal')
        b.config(state='normal')
        save.config(text='Save')

a_score = 0
b_score = 0
def increase(team):
    global a_score
    global b_score
    if (team == 'a'):
        a_score += 1
        a_sco.config(text=a_score)
    elif (team == 'b'):
        b_score += 1
        b_sco.config(text=b_score)

def decrease(team):
    global a_score, b_score
    if team == 'a':
        a_score -= 1
        if (a_score < 0):
            a_score = 0
        a_sco.config(text=a_score)
    elif team == 'b':
        b_score = max(0, b_score - 1)
        b_sco.config(text=b_score)

root = Tk()
root.title('Counter Click')

dynamic_font = font.Font(family="Noto Sans Lao", size=14)

for i in range(3):  # 3 rows
    root.grid_rowconfigure(i, weight=1, uniform="rows")
for i in range(6):  # 6 cols
    root.grid_columnconfigure(i, weight=1, uniform="cols")

a_lab = Label(root, text='ຊື່ທີມ A', width=20, font=dynamic_font)
a_lab.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

sco_lab = Label(root, text='ຄະແນນເຕັມ', width=10, font=dynamic_font)
sco_lab.grid(row=0, column=2, padx=5, pady=5, sticky='nsew')

sav_lab = Label(root, text='ບັນທຶກຄ່າ', width=10, font=dynamic_font)
sav_lab.grid(row=0, column=3, padx=5, pady=5, sticky='nsew')

b_lab = Label(root, text='ຊື່ທີມ B', width=20, font=dynamic_font)
b_lab.grid(row=0, column=4, columnspan=2, padx=5, pady=5, sticky='nsew')

a = Entry(root, width=20, font=dynamic_font, justify='center')
a.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

goal = Entry(root, width=10, font=dynamic_font, justify='center')
goal.grid(row=1, column=2, padx=5, pady=5, sticky='nsew')

save = Button(root, text='Save', width=10, font=dynamic_font, command=save_info)
save.grid(row=1, column=3, padx=5, pady=5, sticky='nsew')

b = Entry(root, width=20, font=dynamic_font, justify='center')
b.grid(row=1, column=4, columnspan=2, padx=5, pady=5, sticky='nsew')

a_inc = Button(root, text='-', width=10, font=dynamic_font, command=lambda: decrease('a'))
a_inc.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')

a_sco = Label(root, text='0', width=10, bg='lightblue', font=dynamic_font)
a_sco.grid(row=2, column=1, padx=5, pady=5, sticky='nsew')

a_dec = Button(root, text='+', width=10, font=dynamic_font, command=lambda: increase('a'))
a_dec.grid(row=2, column=2, padx=5, pady=5, sticky='nsew')

b_inc = Button(root, text='-', width=10, font=dynamic_font, command=lambda: decrease('b'))
b_inc.grid(row=2, column=3, padx=5, pady=5, sticky='nsew')

b_sco = Label(root, text="0", width=10, bg="lightpink", font=dynamic_font)
b_sco.grid(row=2, column=4, padx=5, pady=5, sticky='nsew')

b_dec = Button(root, text='+', width=10, font=dynamic_font, command=lambda: increase('b'))
b_dec.grid(row=2, column=5, padx=5, pady=5, sticky='nsew')

root.bind("<Configure>", font_resize)

root.mainloop()
