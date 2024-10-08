import tkinter as tk

class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        main_window = tk.Frame(self)
        main_window.pack(side='top', fill='both', expand=True)

        main_window.grid_rowconfigure(0, weight=1)
        main_window.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Initialize StringVars for username and password
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        for F in (LoginPage, ProfilePage):
            frame = F(main_window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nswe')

        self.show_frame(LoginPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        loginpage_title = tk.Label(self, text='TooKao Login Page')
        username_title = tk.Label(self, text='Username:')
        username_entry = tk.Entry(self, textvariable=controller.username)
        password_title = tk.Label(self, text='Password:')
        password_entry = tk.Entry(self, textvariable=controller.password)

        login_submit = tk.Button(self, text='Login', command=lambda: controller.show_frame(ProfilePage))

        loginpage_title.grid(row=0, columnspan=2)
        username_title.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)
        password_title.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)
        login_submit.grid(row=3, columnspan=2)

class ProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Directly use the StringVar for the label
        profile_title = tk.Label(self, textvariable=controller.username, font=("Verdana", 20))
        profile_title.grid(row=0, column=0)

        btn = tk.Button(self, text='Logout', command=lambda: controller.show_frame(LoginPage))
        btn.grid(row=1, column=0)

# Driver Code
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
