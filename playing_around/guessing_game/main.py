import random
import tkinter as tk

root = tk.Tk()
root.title('Numbers Guessing Game')

randnum = random.randint(1, 10)
player_choice = tk.StringVar()
ai_choice = tk.StringVar()
ai_choice_generation = random.randint(1, 10)
verdict = tk.StringVar()

# game summary vars
game_summary_title = tk.StringVar()
random_num_showcase = tk.StringVar()
player_verdict = tk.StringVar()
ai_verdict = tk.StringVar()

def game_results():
    submit_choice.grid_forget()

    if ai_choice_generation == randnum:
        verdict.set('The AI has won!')
    elif player_choice.get() == str(randnum):
        verdict.set('The player has won!')
    elif ai_choice_generation == randnum and player_choice.get() == str(randnum):
        verdict.set('Tie, both parties won!')
    else:
        verdict.set('Noone won!')    
    
    game_summary_func()
    reset_btn.grid(row=7, columnspan=2)

def game_summary_func():
    player_num = player_choice.get()

    game_summary_title.set('== Game Summary ==')
    player_verdict.set(f'Player selected the number {player_num}')
    ai_verdict.set(f'AI selected the number {ai_choice_generation}')
    random_num_showcase.set(f'The random number generated was {randnum}')

def reset():
    global randnum
    global ai_choice_generation
    randnum = random.randint(1, 10)
    ai_choice_generation = random.randint(1, 10)

    player_choice.set('')
    ai_choice.set('')
    verdict.set('')

    game_summary_title.set('')
    random_num_showcase.set('')
    player_verdict.set('')
    ai_verdict.set('')

    submit_choice.grid(row=2, columnspan=2, pady=10)

game_screen = tk.Frame(root)
game_screen.grid(row=0, column=0)

game_title = tk.Label(game_screen, text='Numbers Guessing Game', font=('Maven Black Pro', 16))
player_lbl = tk.Label(game_screen, text="Player's Guess:")
player_entry = tk.Entry(game_screen, textvariable=player_choice)
submit_choice = tk.Button(game_screen, text='Run the Round!', command=game_results)

verdict_lbl = tk.Label(game_screen, textvariable=verdict)
game_summary = tk.Label(game_screen, textvariable=game_summary_title)
player_summary = tk.Label(game_screen, textvariable=player_verdict)
ai_summary = tk.Label(game_screen, textvariable=ai_verdict)
randnum_summary = tk.Label(game_screen, textvariable=random_num_showcase)

reset_btn = tk.Button(game_screen, text='Reset', command=reset)

game_title.grid(row=0, columnspan=2, padx=10)
player_lbl.grid(row=1, column=0)
player_entry.grid(row=1, column=1)
submit_choice.grid(row=2, columnspan=2, pady=10)

verdict_lbl.grid(row=2, columnspan=2)
game_summary.grid(row=3, columnspan=2)
player_summary.grid(row=4, columnspan=2)
ai_summary.grid(row=5, columnspan=2)
randnum_summary.grid(row=6, columnspan=2, pady=(0, 10))

reset_btn.grid(row=7, columnspan=2)
reset_btn.grid_forget()

root.mainloop()

# todo next time:
# add a restart button to set game state back to start