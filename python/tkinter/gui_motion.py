# gui_motion.py
from tkinter import *

# tracking mouse movement function
def motion_tracking(event):
    motion_display.config(text=f'Mouse location: x={event.x}, y={event.y}')
    return

def left_click(event):
    click_display.config(text=f'You clicked LEFT button at x={event.x}, y={event.y}')

def middle_click(event):
    click_display.config(text=f'You clicked MIDDLE button at x={event.x}, y={event.y}')

def right_click(event):
    click_display.config(text=f'You clicked RIGHT button at x={event.x}, y={event.y}')

def scroll_up(event):
    click_display.config(text=f'Scrolled UP at x={event.x}, y={event.y}')

def scroll_down(event):
    click_display.config(text=f'Scrolled DOWN at x={event.x}, y={event.y}')

def scroll_wheel(event):
    click_display.config(text=f'SCROLLED at x={event.x}, y={event.y}')

def left_button_release(event):
    release_display.config(text=f'LEFT button released at x={event.x}, y={event.y}')

def middle_button_release(event):
    release_display.config(text=f'MIDDLE button released at x={event.x}, y={event.y}')

def right_button_release(event):
    release_display.config(text=f'RIGHT button released at x={event.x}, y={event.y}')

root = Tk()
root.geometry("300x200")  # Set initial window size

Label(root, text='Move the mouse around').pack()

motion_display = Label(root, text='')
motion_display.pack()

click_display = Label(root, text='')
click_display.pack()

release_display = Label(root, text='')
release_display.pack()

double_display = Label(root, text='')
double_display.pack()

root.bind("<Motion>", motion_tracking)
root.bind("<Button-1>", left_click)
root.bind("<Button-2>", middle_click)
root.bind("<Button-3>", right_click)
root.bind("<ButtonRelease-1>", left_button_release)
root.bind("<ButtonRelease-2>", middle_button_release)
root.bind("<ButtonRelease-3>", right_button_release)
# root.bind("<Button-4>", scroll_up)  # for LINUX only
# root.bind("<Button-5>", scroll_down)    # for LINUX only
root.bind("<MouseWheel>", scroll_wheel)  # for WINDOWS and MAC
root.bind("<Double-Button-1>", lambda e: double_display.config(text=f'Double LEFT clicked at x={e.x}, y={e.y}'))
root.bind("<Double-Button-2>", lambda e: double_display.config(text=f'Double MIDDLE clicked at x={e.x}, y={e.y}'))
root.bind("<Double-Button-3>", lambda e: double_display.config(text=f'Double RIGHT clicked at x={e.x}, y={e.y}'))
root.mainloop()
