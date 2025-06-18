# dynamic_font.py
from tkinter import *
from tkinter import font

# Create main window
root = Tk()
root.title("Dynamic Font Resizing")
root.geometry("400x200")  # Initial window size

dynamic_font = font.Font(family="Noto Sans Lao", size=12)

label = Label(root, text="ປັບຂະຫນາດຫນ້າຕ່າງ!", font=dynamic_font)
label.pack(expand=True, fill="both", padx=20, pady=20)


# Function to adjust font size based on window size
def resize_font(event):
    # Basic formula: font size = window height / some factor
    # You can adjust the divisor to control how quickly font scales
    new_size = max(8, int(event.height / 10))  # Set minimum font size
    dynamic_font.configure(size=new_size)

root.bind("<Configure>", resize_font)

root.mainloop()
