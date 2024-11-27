import tkinter as tk
import json
import random

class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.current_page = tk.StringVar(value='a_page')

        self.pages = {}

        for P in (LoginPage, HomePage):
            page = P(container, self)
            self.pages[P] = page
            page.grid(row=0, column=0, sticky='nswe')

        self.show_page(LoginPage)

    def show_page(self, page):
        selected_page = self.pages[page]
        if self.current_page.get() != 'another_page':
            self.current_page.set('another_page')
        else:
            self.current_page.set('a_page')
        selected_page.tkraise()

    def generate_quote(self):
        with open('quotes.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            quotes = data['quotes']
            the_quote = random.choice(quotes)
            return f'{the_quote['quote']} ~ {the_quote['author']}'

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.create_widgets()

        self.controller.current_page.trace_add('write', lambda *args: self.display_a_quote(*args))

    def create_widgets(self):
        page_name = tk.Label(self, text='This is the Login Page.', font=('helvetica', 24))
        page_name.pack()
        self.motivational_quote = tk.Label(self, font=('helvetica', 18), wraplength=500)
        self.motivational_quote.pack()
        home_button = tk.Button(self, text='Go Home', font=('helvetica', 18), command=lambda:self.controller.show_page(HomePage))
        home_button.pack()

    def display_a_quote(self, *args):
        print(self.controller.generate_quote())
        self.motivational_quote.config(text=self.controller.generate_quote())

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        page_name = tk.Label(self, text='This is the home page', font=('helvetica', 24))
        page_name.pack()

        logout = tk.Label(self, text='Logout', font=('helvetica', 24))
        logout.pack()

        logout.bind("<Button-1>", lambda mouse_event: self.redirect_page(mouse_event, LoginPage))

    def redirect_page(self, mouse_event, page_choice):
        self.controller.show_page(page_choice)

if __name__ == '__main__':
    app = MainApp()
    app.mainloop()