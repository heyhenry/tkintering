import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Login Page')

page_title = ttk.Label(root, text='Login', font=('Copperplate Gothic Bold', 16))
page_title.grid(row=0, columnspan=2)

username = ttk.Label(root, text='Username:')
username.grid(row=1, column=0)
username_entry = ttk.Entry(root)
username_entry.grid(row=1, column=1)

password = ttk.Label(root, text='Password:')
password.grid(row=2, column=0)
password_entry = ttk.Entry(root)
password_entry.grid(row=2, column=1)

login = ttk.Button(root, text='Login')
login.grid(row=3, columnspan=2)

root.mainloop()