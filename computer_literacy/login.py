import tkinter as tk
from tkinter import ttk
# from tkinter import PhotoImage
import json
from PIL import ImageTk, Image

# resize an image to your liking (WxH)
def resize_image(image_path, new_size):
    # open the image using PIL
    with Image.open(image_path) as img:
        # resize the image using image.LANCZOS for high-quality resizing *Note. image.LANCZOS is not a required parameter
        resized_img = img.resize(new_size)
        return resized_img

root = tk.Tk()
root.title('Login Page')
root.geometry('300x150')

username = tk.StringVar()
password = tk.StringVar()
uncensor_pressed = True
close_eye_icon_resized = resize_image('closed_eye.png', (15, 15))
closed_eye_icon = ImageTk.PhotoImage(close_eye_icon_resized)
open_eye_icon_resized = resize_image('opened_eye.png', (15, 15))
opened_eye_icon = ImageTk.PhotoImage(open_eye_icon_resized)

# def validate_login():

def test():
    login_frame.destroy()
    profile_frame.pack()

# censoring and uncensoring password upon click
def uncensor_password():
    global uncensor_pressed
    if uncensor_pressed:
        password_entry.config(show='')
        uncensor_entry.config(image=closed_eye_icon)
        uncensor_pressed = False
    else:
        password_entry.config(show='*')
        uncensor_entry.config(image=opened_eye_icon)
        uncensor_pressed = True

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
uncensor_entry = tk.Button(login_frame, image=opened_eye_icon, command=uncensor_password)
uncensor_entry.grid(row=2, column=2)

login = ttk.Button(login_frame, text='Login', command=test)
login.grid(row=3, columnspan=2)

profile_frame = ttk.Frame(root)
profile_frame.pack()
profile_frame.pack_forget()

profile_title = ttk.Label(profile_frame, text='Welcome User!')
profile_title.pack()

root.mainloop()