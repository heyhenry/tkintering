import tkinter as tk
from tkinter import ttk

# initial tkinter setup
root = tk.Tk()
root.title('Reading Logger')
root.geometry('300x300')

# tabbing system initiate
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# tabbing outline
home_frame = tk.Frame(notebook, bg='lightblue')
add_entry_frame = tk.Frame(notebook, bg='lightyellow')

home_frame.pack()
add_entry_frame.pack()

notebook.add(home_frame, text='Home')
notebook.add(add_entry_frame, text='Add Entry')

# home section



# add entry section

root.mainloop()