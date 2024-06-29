import tkinter as tk
from tkinter import ttk

# initial tkinter setup
root = tk.Tk()
root.title('Reading Logger')
root.geometry('300x300')

# home
home_frame = tk.Frame(root, bg='lightblue')
home_frame.pack(expand=True, fill='both')

home_title = tk.Label(home_frame, text='Reading Logger | Home')
home_title.pack()





root.mainloop()