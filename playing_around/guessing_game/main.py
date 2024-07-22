import random
import tkinter as tk

root = tk.Tk()
root.title('Numbers Guessing Game')

# variables
randnum = random.randint(1, 10)
player_choice = tk.StringVar()
ai_choice = tk.StringVar()
ai_choice_generation = random.randint(1, 10)
verdict = tk.StringVar()

# game summary variables
game_summary_title = tk.StringVar()
random_num_showcase = tk.StringVar()
player_verdict = tk.StringVar()
ai_verdict = tk.StringVar()

# checking who won and displaying game summary details
def game_results():

    # hide submit button
    submit_choice.grid_forget()

    # logic to determine winner
    if ai_choice_generation == randnum:
        verdict.set('The AI has won!')
    elif player_choice.get() == str(randnum):
        verdict.set('The player has won!')
    elif ai_choice_generation == randnum and player_choice.get() == str(randnum):
        verdict.set('Tie, both parties won!')
    else:
        verdict.set('Noone won!')    
    
    game_summary_func()

    # show reset button
    reset_btn.grid(row=7, columnspan=2)

# detailed summary of game played
def game_summary_func():
    
    # retrieve player's answer
    player_num = player_choice.get()

    # showcase game details
    game_summary_title.set('== Game Summary ==')
    player_verdict.set(f'Player selected the number {player_num}')
    ai_verdict.set(f'AI selected the number {ai_choice_generation}')
    random_num_showcase.set(f'The random number generated was {randnum}')

# reset window to new game state
def reset():
    
    global randnum
    global ai_choice_generation
    
    # generate new random numbers
    randnum = random.randint(1, 10)
    ai_choice_generation = random.randint(1, 10)

    # reset all variables to nothing
    player_choice.set('')
    ai_choice.set('')
    verdict.set('')

    game_summary_title.set('')
    random_num_showcase.set('')
    player_verdict.set('')
    ai_verdict.set('')

    # re-show submit button
    submit_choice.grid(row=2, columnspan=2, pady=10)

# widgets
game_screen = tk.Frame(root)

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

# grid layout
game_screen.grid(row=0, column=0)

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

# hide reset button initially
reset_btn.grid_forget()

root.mainloop()

# todo next time:
# add a restart button to set game state back to start