import tkinter as tk
import random
import time


def shake(window):
    x = window.winfo_x()
    y = window.winfo_y()

    for _ in range(5):
        x_offset = random.randint(-10, 10)
        y_offset = random.randint(-10, 10)
        window.geometry(f"+{x + x_offset}+{y + y_offset}")
        window.update()
        time.sleep(0.05)

    window.geometry(f"+{x}+{y}")


root = tk.Tk()
root.geometry("300x200")

shake_button = tk.Button(root, text="Shake Me!", command=lambda: shake(root))
shake_button.pack(pady=50)

root.mainloop()
