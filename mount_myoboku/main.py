import tkinter as tk
import json
import os
from user import UserInfo

user = {}

user_savefile = 'user_save.json'

class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.load_user_data()

        self.pages = {}

        for P in (LoginPage, HomePage):
            page = P(container, self)
            self.pages[P] = page
            page.grid(row=0, column=0, sticky='nswe')

        self.show_page(LoginPage)

    # show the selected page
    def show_page(self, cont):
        page = self.pages[cont]
        # change the size of screen based on page shown
        if page == self.pages[LoginPage]:
            self.geometry('800x800')
        else:
            self.geometry('1800x1000')
        page.tkraise()
    
    # load the user data
    def load_user_data(self):
        global user
        if os.path.exists(user_savefile):
            with open(user_savefile, 'r') as file:
                user_data = json.load(file)
                for u, u_info in user_data.items():
                    user[u] = UserInfo(u_info['password'])

    # custom serializer for json
    def custom_serializer(self, obj):
        if isinstance(obj, UserInfo):
            return {
                'password': obj.password
            }
        return obj

    # update the user data in the save file
    def save_user_data(self):
        user_object = json.dumps(user, indent=4, default=self.custom_serializer)
        with open(user_savefile, 'w') as outfile:
            outfile.write(user_object)

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller

        self.motivational_quotes = ['Just do it - Nike', 'Be the change you wanna see - Unknown', 'Show them all with your success - Unknown']
        self.password_var = tk.StringVar()
        self.confirm_password_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self, font=('helvetica', 32), text='Mount Myoboku')
        motivational_quote = tk.Label(self, font=('helvetica', 18), text='aosdjfaosdjfoajdfopjafopjasdofjaodfjad')
        self.password_title = tk.Label(self, font=('helvetica', 24), text='Password:')
        self.password = tk.Entry(self, font=('helvetica', 24), textvariable=self.password_var)
        self.confirm_password_title = tk.Label(self, font=('helvetica', 24), text='Confirm Password:')
        self.confirm_password = tk.Entry(self, font=('helvetica', 24), textvariable=self.confirm_password_var)
        self.error_message = tk.Label(self, font=('helvetica', 24), foreground='red')
        self.enter = tk.Button(self, font=('helvetica', 24), text="Enter Mount Myoboku")

        title.place(x=250, y=50)
        motivational_quote.place(x=200, y=150)

        # determine which layout to show based on whether password exists
        if user['user'].password:
            self.existing_user_layout()
        else:
            self.non_existing_user_layout()      

    # display this layout if user has already set a password
    def existing_user_layout(self):
        # clear slate widgets
        self.password_title.place_forget()
        self.password.place_forget()
        self.confirm_password_title.place_forget()
        self.confirm_password.place_forget()
        self.error_message.place_forget()
        self.enter.place_forget()

        # attach relevant function call
        self.enter.config(command=self.validate_existing_password)

        # place relevant widgets
        self.password_title.place(x=200, y=300)
        self.password.place(x=200, y=350)
        self.error_message.place(x=200, y=400)
        self.enter.place(x=200, y=500)

    # display this layout if user hasn't already set a password
    def non_existing_user_layout(self):
        # clean slate relevant widgets
        self.password_title.place_forget()
        self.password.place_forget()
        self.confirm_password_title.place_forget()
        self.confirm_password.place_forget()
        self.error_message.place_forget()
        self.enter.place_forget()

        # attach relevant function call
        self.enter.config(command=self.validate_new_password)

        # place relevant widgets
        self.password_title.place(x=200, y=250)
        self.password.place(x=200, y=300)
        self.confirm_password_title.place(x=200, y=400)
        self.confirm_password.place(x=200, y=450)
        self.error_message.place(x=200, y=500)
        self.enter.place(x=200, y=550)

    # ensure password and confirm password are correct before saving password
    def validate_new_password(self):
        self.error_message.config(text='')
        if self.password_var.get() != self.confirm_password_var.get():
            # display an error message if the passwords do not match
            self.error_message.config(text="Error: Password Inputs Don't Match.")
        else:
            # save password to the user's password attribute
            user['user'].password = self.password_var.get()
            # save the user data to the json file
            self.controller.save_user_data()
            # clear the password entry field
            self.password.delete(0, 'end')
            # display the relevant new layout/widgets
            self.existing_user_layout()

    # ensure that the given password matches the one saved in the user save file
    def validate_existing_password(self):
        self.error_message.config(text='')
        if self.password_var.get() != user['user'].password:
            # display an error message if the password does not match the saved password
            self.error_message.config(text='Error: Invalid Password.')
        else:
            # redirect to the home page when password is successfully entered
            self.controller.show_page(HomePage)
        
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        temp = tk.Label(self, text='This is the Home Page.') 
        temp.pack()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()