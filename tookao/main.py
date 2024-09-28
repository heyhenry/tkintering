# credited resouce: https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/
import tkinter as tk

class MainApp(tk.Tk):
    # init function for class MainApp
    def __init__(self, *args, **kwargs):
        
        # init function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        
        # creating a container
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initialise frames to an empty array
        self.frames = {}

        # iterate through tuple that consists of pages
        for F in (HomePage, SettingsPage, AboutPage):
            frame = F(container, self)
            # initialize frame of each page's object
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nswe')
        
        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        homepage_title = tk.Label(self, text='Welcome to the Home Page')
        homepage_title.grid(row=0, columnspan=2)

        settings_button = tk.Button(self, text='Go To Settings Page', command=lambda: controller.show_frame(SettingsPage))
        settings_button.grid(row=1, column=0)
        about_button = tk.Button(self, text='Go To About Page', command=lambda: controller.show_frame(AboutPage))
        about_button.grid(row=1, column=1)

class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        homepage_title = tk.Label(self, text='Welcome to the Settings Page')
        homepage_title.grid(row=0, columnspan=2)

        settings_button = tk.Button(self, text='Go To Home Page', command=lambda: controller.show_frame(HomePage))
        settings_button.grid(row=1, column=0)
        about_button = tk.Button(self, text='Go To About Page', command=lambda: controller.show_frame(AboutPage))
        about_button.grid(row=1, column=1)

class AboutPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        homepage_title = tk.Label(self, text='Welcome to the About Page')
        homepage_title.grid(row=0, columnspan=2)

        settings_button = tk.Button(self, text='Go To Home Page', command=lambda: controller.show_frame(HomePage))
        settings_button.grid(row=1, column=0)
        about_button = tk.Button(self, text='Go To Settings Page', command=lambda: controller.show_frame(SettingsPage))
        about_button.grid(row=1, column=1)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()



