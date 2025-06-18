# gui_treeview.py
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Widget - Treeview")

ttk.Label(root, text="Treeview - hierarchical").pack()

# Creating treeview window
tv = ttk.Treeview(root)
tv.pack()

# Inserting items to the treeview
# Inserting parent
tv.insert("", "0", "parent_1", text="Parent Treeview")

# Inserting child to parent
tv.insert("", "1", "child_1", text="First Child Treeview")
tv.insert("", "2", "child_2", text="Second Child Treeview")
tv.insert("", "end", "child_3", text="Third Child Treeview")

# Inserting item to children
tv.insert("child_1", "end", "Child_1_item_1", text="Child_1_item_1")
tv.insert("child_1", "end", "Child_1_item_2", text="Child_1_item_2")

tv.insert("child_2", "end", "Child_2_item_1", text="Child_2_item_1")
tv.insert("child_2", "end", "Child_2_item_2", text="Child_2_item_2")

tv.insert("child_3", "end", "Child_3_item_1", text="Child_3_item_1")
tv.insert("child_3", "end", "Child_3_item_2", text="Child_3_item_2")

# Placing each child items in parent widget
tv.move("child_1", "parent_1", "end")
tv.move("child_2", "parent_1", "end")
tv.move("child_3", "parent_1", "end")

root.mainloop()
