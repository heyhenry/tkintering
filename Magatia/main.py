import tkinter as tk
from tkinter import ttk

font_choice = 'Microsoft JhengHei'
backup_font_choice = 'Maven Pro'


root = tk.Tk()
root.title('Magatia App')
s = ttk.Style()
s.configure('.', font=(font_choice, 11))

tab_system = ttk.Notebook(root)
tab_system.pack(fill='both', expand=1)
main_window = ttk.Frame(tab_system)
tab_system.add(main_window, text='Main')
search_window = ttk.Frame(tab_system)
tab_system.add(search_window, text='Search')

# main window
top_win = tk.Frame(main_window)
left_win = tk.Frame(main_window)
leftbot_win = tk.Frame(main_window)
right_win = tk.Frame(main_window)
rightbot_win = tk.Frame(main_window)

top_win.grid(row=0, columnspan=2)
left_win.grid(row=1, column=0)
leftbot_win.grid(row=2, column=0)
right_win.grid(row=1, column=1)
rightbot_win.grid(row=2, column=1)

# top_win 
title_lbl = ttk.Label(top_win, text='Magatia', font=(font_choice, 21))
slogan_lbl = ttk.Label(top_win, text='~ Record your growing wisdom with us ~')

title_lbl.grid(row=0, column=0)
slogan_lbl.grid(row=1, column=0)

# left_win
entries_lb = tk.Listbox(left_win)
entries_sb = ttk.Scrollbar(left_win, command=entries_lb.yview)
entries_lb.config(yscrollcommand=entries_sb.set)
entries_lb.pack(side='left', fill='both', expand=True)
entries_sb.pack(side='right', fill='y')

# leftbot_win
add_entry_btn = ttk.Button(leftbot_win, text='Add Entry')
update_entry_btn = ttk.Button(leftbot_win, text='Update Entry')
remove_entry_btn = ttk.Button(leftbot_win, text='Delete Entry')

add_entry_btn.pack()
update_entry_btn.pack()
remove_entry_btn.pack()

root.mainloop()