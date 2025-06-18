# gui_progressbar.py
from tkinter import *
from tkinter import ttk
import time


def start_progress():
    pg.start()
    # Simulate a task over time
    for i in range(101):
        time.sleep(0.05)
        pg["value"] = i
        # Update the GUI
        root.update_idletasks()
    pg.stop()


root = Tk()
root.title("Widget - ProgressBar")

# Create a progressbar widget
pg = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
pg.pack(pady=20)

# Button to start progress
start_button = Button(root, text="Click To Start Progress", command=start_progress)
start_button.pack(pady=10)

root.mainloop()
