import tkinter as tk
import json
import os
from user import UserInfo

user = {}

user_savefile = 'user_save.json'

class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry('1800x1000')

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages = {}

        for P in (LoginPage, HomePage):
            page = P(container, self)
            self.pages[P] = page
            page.grid(row=0, column=0, sticky='nswe')

        self.show_page(LoginPage)

    # show the selected page
    def show_page(self, cont):
        page = self.pages[cont]
        page.tkraise()
    
    # load the user data
    def load_user(self):
        global user
        if os.path.exists(user_savefile):
            with open(user_savefile, 'r') as file:
                user_data = json.load(file)
                for u, u_info in user_data.items():
                    user[u] = UserInfo(u_info['password'])


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        self.controller.geometry('800x800')

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
        self.error_message = tk.Label(self, font=('helvetica', 24), text='dfjadfhasdhfasdhjfa', foreground='red')
        self.enter = tk.Button(self, font=('helvetica', 24), text="Enter Mount Myoboku")

        title.place(x=250, y=50)
        motivational_quote.place(x=200, y=150)

        # self.existing_user_layout()
        self.non_existing_user_layout()

    def existing_user_layout(self):
        self.password_title.place(x=200, y=300)
        self.password.place(x=200, y=350)
        self.error_message.place(x=200, y=400)
        self.enter.place(x=200, y=500)

    def non_existing_user_layout(self):
        self.password_title.place(x=200, y=250)
        self.password.place(x=200, y=300)
        self.confirm_password_title.place(x=200, y=400)
        self.confirm_password.place(x=200, y=450)
        self.error_message.place(x=200, y=500)
        self.enter.place(x=200, y=550)

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