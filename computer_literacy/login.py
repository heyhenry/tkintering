import tkinter as tk
from tkinter import ttk
import json

root = tk.Tk()
root.title('Login Page')
root.geometry('300x150')

username = tk.StringVar()
password = tk.StringVar()

# def validate_login():

def test():
    login_frame.destroy()
    profile_frame.pack()

login_frame = ttk.Frame(root)
login_frame.pack()

page_title = ttk.Label(login_frame, text='Login', font=('Copperplate Gothic Bold', 16))
page_title.grid(row=0, columnspan=2)

username = ttk.Label(login_frame, text='Username:')
username.grid(row=1, column=0)
username_entry = ttk.Entry(login_frame)
username_entry.grid(row=1, column=1)

password = ttk.Label(login_frame, text='Password:')
password.grid(row=2, column=0)
password_entry = ttk.Entry(login_frame, show='*')
password_entry.grid(row=2, column=1)

login = ttk.Button(login_frame, text='Login', command=test)
login.grid(row=3, columnspan=2)

profile_frame = ttk.Frame(root)
profile_frame.pack()
profile_frame.pack_forget()

profile_title = ttk.Label(profile_frame, text='Welcome User!')
profile_title.pack()

root.mainloop()