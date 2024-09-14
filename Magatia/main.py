import tkinter as tk
from tkinter import ttk

font_choice = 'Microsoft JhengHei'
backup_font_choice = 'Maven Pro'


root = tk.Tk()
root.title('Magatia App')
s = ttk.Style()
s.configure('.', font=(font_choice, 19))

tab_system = ttk.Notebook(root)
tab_system.pack()
main_window = ttk.Frame(tab_system)
tab_system.add(main_window, text='Main')
search_window = ttk.Frame(tab_system)
tab_system.add(search_window, text='Search')

root.mainloop()