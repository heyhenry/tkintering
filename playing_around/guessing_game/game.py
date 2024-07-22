import random
import tkinter as tk

root = tk.Tk()
root.title('Guessing Game')

status = tk.StringVar()

def change_status():
    status.set('Pee')

def reset():
    game_screen.destroy()

game_screen = tk.Frame(root)
game_screen.grid(row=0, column=0)

title_lbl = tk.Label(game_screen, text='Testers')
status_btn = tk.Button(game_screen, text='Poop', command=change_status)
reset_btn = tk.Button(game_screen, text='Reset All')



root.mainloop()