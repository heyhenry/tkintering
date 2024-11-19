import tkinter as tk

class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

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

    def show_page(self, cont):
        page = self.pages[cont]
        page.tkraise()

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        hello = tk.Label(self, text='Hello, This is the Login Page!')
        home_redirect = tk.Button(self, text='Home Page', command=lambda:self.controller.show_page(HomePage))

        hello.pack()
        home_redirect.pack()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        hello = tk.Label(self, text='Hello, This is the Home Page.')
        login_redirect = tk.Button(self, text='Login Page', command=lambda: self.controller.show_page(LoginPage))

        hello.pack()
        login_redirect.pack()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()