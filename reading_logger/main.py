# Resources used: 
# creating listboxes: https://www.geeksforgeeks.org/python-tkinter-listbox-widget/
# centering home title: https://stackoverflow.com/questions/70974175/with-tkinter-grid-method-i-want-to-center-the-labels 

import tkinter as tk
from tkinter import ttk

# initial tkinter setup
root = tk.Tk()
root.title('Reading Logger')
root.geometry('300x300')

# home
home_frame = tk.Frame(root, bg='lightblue')
home_frame.pack(expand=True, fill='both')

home_title = tk.Label(home_frame, text='Reading Logger | Home', bg='lightblue')
home_title.grid(row=0, column=0)

entries_lbl = tk.Label(home_frame, text='Entries', bg='lightblue')
entries_lbl.grid(row=1, column=0)

entries_lb = tk.Listbox(home_frame)
entries_lb.grid(row=2, column=0)

root.mainloop()