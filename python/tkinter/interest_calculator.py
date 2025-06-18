# interest_calculator.py
from tkinter import *
from tkinter import ttk

def interest_calc_function(*args):
    try:
        p = float(principal.get())
        i = float(interest.get())
        d = int(duration.get())
        result =(p * (i) / 100) * (d / 365)
        earn.set(format(result, ',.2f')+' ກີບ')
    except:
        earn.set('Error')

root = Tk()
root.title('ຄຳນວນດອກເບ້ຍ')

frame = ttk.Frame(root, padding='2 3 4 5')
frame.grid(column=0, row=0, sticky=(N, W, E, S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

principal = StringVar()
interest = StringVar()
duration = StringVar()
earn = StringVar()

ttk.Label(frame, text='ເງິນຕົ້ນ (ກີບ)').grid(column=0, row=0, sticky=E)
principal_entry = ttk.Entry(frame, textvariable=principal)
principal_entry.grid(column=1, row=0, sticky=(W, E))

ttk.Label(frame, text='ອັດຕາດອກເບ້ຍ (%)').grid(column=0, row=1, sticky=E)
interest_entry = ttk.Entry(frame, textvariable=interest)
interest_entry.grid(column=1, row=1, sticky=(W, E))

ttk.Label(frame, text='ໄລຍະເວລາ (ວັນ)').grid(column=0, row=2, sticky=E)
duration_entry = ttk.Entry(frame, textvariable=duration)
duration_entry.grid(column=1, row=2, sticky=(W, E))

ttk.Button(frame, text='ຄຳນວນ', command=interest_calc_function).grid(column=0, row=3, sticky=(W, E))

ttk.Label(frame, textvariable=earn).grid(column=1, row=3, sticky=(E))

principal_entry.focus()
root.bind('<Return>', interest_calc_function)

root.mainloop()
