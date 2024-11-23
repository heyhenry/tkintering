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
        title = tk.Label(self, text='Mount Myoboku', font=('helvetica', 48))
        title.place(x=700, y=50)
        motivational_quote = tk.Label(self, text='dfadfadfadfiasdfhaasdfhadfha', font=('helvetica', 18))
        motivational_quote.place(x=700, y=150)

        date_info = tk.Label(self, text='Date: 23rd November 2024', font=('helvetica', 18))
        date_info.place(x=50, y=50)
        time_info = tk.Label(self, text='Time: 04:47:02', font=('helvetica', 18))
        time_info.place(x=50, y=100)


        nav_workout = tk.Label(self, text='Add Workout', font=('helvetica', 18))
        nav_workout.place(x=1250, y=50)
        nav_divider_one = tk.Label(self, text='|', font=('helvetica', 18))
        nav_divider_one.place(x=1420, y=50)
        nav_stats = tk.Label(self, text='Check Stats', font=('helvetica', 18))
        nav_stats.place(x=1450, y=50)
        nav_divider_two = tk.Label(self, text='|', font=('helvetica', 18))
        nav_divider_two.place(x=1620, y=50)
        nav_logout = tk.Label(self, text='Logout', font=('helvetica', 18))
        nav_logout.place(x=1650, y=50)

        last_workout_date = tk.Label(self, text='Last Worked Out:', font=('helvetica', 24))
        goal_weight = tk.Label(self, text='Goal Weight:', font=('helvetica', 24))
        steps_taken_today = tk.Label(self, text='Steps Taken Today:', font=('helvetica', 24))
        steps_taken_total = tk.Label(self, text='Total Steps Taken:', font=('helvetica', 24))

        last_workout_date.place(x=250, y=300)
        goal_weight.place(x=250, y=400)
        steps_taken_today.place(x=250, y=500)
        steps_taken_total.place(x=250, y=600)

        why_doing = tk.Label(self, text='Why are you doing this?', font=('helvetica', 24))
        who_for = tk.Label(self, text='Who is this for?', font=('helvetica', 24))
        what_moves_you = tk.Label(self, text='What keeps you moving?', font=('helvetica', 24))
        selfish_reward = tk.Label(self, text="What's a selfish reward once you reach this goal?", font=('helvetica', 24))

        why_doing.place(x=1000, y=300)
        who_for.place(x=1000, y=400)
        what_moves_you.place(x=1000, y=500)
        selfish_reward.place(x=1000, y=600)
        
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()