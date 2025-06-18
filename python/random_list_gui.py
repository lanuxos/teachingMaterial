from tkinter import *
from random import choice


def pick_winner():
    input_text = name_entry.get()
    names = [name.strip() for name in input_text.split(",") if name.strip()]

    if not names:
        result_label.config(text="❌ Please enter at least one name.")
        return
    
    list_length = len(names)
    pick_button.config(text=f"Pick 1 Winner from ({list_length} names)")

    winner = choice(names)
    result_label.config(text=f"🎉 Winner: {winner} 🎉")


# Create main window
root = Tk()
root.title("Random Winner Picker")
root.geometry("400x200")

# Entry for names
Label(root, text="Enter names separated by commas (e.g. Alice,Bob,Charlie):").pack(
    pady=5
)
name_entry = Entry(root, width=50)
name_entry.pack(pady=5)

# Button to pick winner
pick_button = Button(root, text="Pick a Winner", command=pick_winner)
pick_button.pack(pady=10)

# Label to show result
result_label = Label(root, text="", font=("Helvetica", 14, "bold"))
result_label.pack(pady=10)

root.bind("<Return>", lambda event: pick_winner())  # Allow pressing Enter to pick a winner

root.mainloop()
