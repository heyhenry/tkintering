# Resources used: 
# creating listboxes: https://www.geeksforgeeks.org/python-tkinter-listbox-widget/
# centering home title: https://stackoverflow.com/questions/70974175/with-tkinter-grid-method-i-want-to-center-the-labels 

import tkinter as tk
import json
import os

class Entry:
    def __init__(self, title, type, chapsread, readstat):
        self.title = title
        self.type = type
        self.chapsread = chapsread
        self.readstat = readstat

entries = {}


# new entry popup function
def new_entry_popup():
    new_entry = tk.Toplevel(home_frame, bg='lightyellow')
    new_entry.title('New Entry')
    new_entry.geometry('300x300')
    
    new_entry_title = tk.Label(new_entry, text='Reading Logger | New Entry', bg='lightyellow')
    new_entry_title.grid(row=0, columnspan=2)

    ne_title = tk.Label(new_entry, text='Title:', bg='lightyellow')
    ne_type = tk.Label(new_entry, text='Type:', bg='lightyellow')
    ne_chapread = tk.Label(new_entry, text='Chapters Read:', bg='lightyellow')
    ne_readstat = tk.Label(new_entry, text='Reading Status:', bg='lightyellow')

    ne_title_entry = tk.Entry(new_entry)
    ne_type_entry = tk.Entry(new_entry)
    ne_chapread_entry = tk.Entry(new_entry)
    ne_readstat_entry = tk.Entry(new_entry)

    submit_entry = tk.Button(new_entry, text='Add Entry')

    ne_title.grid(row=1, column=0)
    ne_type.grid(row=2, column=0)
    ne_chapread.grid(row=3, column=0)
    ne_readstat.grid(row=4, column=0)

    ne_title_entry.grid(row=1, column=1)
    ne_type_entry.grid(row=2, column=1)
    ne_chapread_entry.grid(row=3, column=1)
    ne_readstat_entry.grid(row=4, column=1)

    submit_entry.grid(row=5, columnspan=2)


# initial tkinter setup
root = tk.Tk()
root.title('Reading Logger')
root.geometry('300x300')

# home
home_frame = tk.Frame(root, bg='lightblue')
home_frame.pack(expand=True, fill='both')

# center (to be done)
home_title = tk.Label(home_frame, text='Reading Logger | Home', bg='lightblue')
home_title.grid(row=0, columnspan=2)

# left side
entries_lbl = tk.Label(home_frame, text='Entries', bg='lightblue')
entries_lbl.grid(row=1, column=0)

entries_lb = tk.Listbox(home_frame)
entries_lb.grid(row=2, column=0)

# right side
new_entry_btn = tk.Button(home_frame, text='New Entry', command=new_entry_popup)
new_entry_btn.grid(row=1, column=1, padx=10)
update_entry_btn = tk.Button(home_frame, text='Update Entry')
update_entry_btn.grid(row=2, column=1, padx=10)


root.mainloop()