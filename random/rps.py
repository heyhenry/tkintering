import tkinter as tk
import random 

root = tk.Tk()
root.title('Rock Paper Scissors')

# variables
moves = ['rock', 'paper', 'scissors']
player = tk.StringVar()
ai_player = tk.StringVar()
result = tk.StringVar()
turns = tk.StringVar()
winner = tk.StringVar()

# process playe move and start game
def chosen_move(move : str):
    player.set(move)
    play_game()

# game logic
def play_game():
    
    global result, winner
    ai_player.set(random.choices(moves))
    
    if player.get() == ai_player.get():
        result.set("It's a draw!")
        winner.set('No winner')
    elif player.get() == 'rock' and ai_player.get() == 'scissors':
        result.set('Player has won!')
        winner.set('Player')
    elif player.get() == 'scissors' and ai_player.get() == 'paper':
        result.set('Player has won!')
        winner.set('Player')
    elif player.get() == 'paper' and ai_player.get() == 'rock':
        result.set('Player has won!')
        winner.set('Player')
    else:
        result.set('Player has lost!')
        winner.set('AI Player')
    
main_screen = tk.Frame(root)
main_screen.pack(padx=20, pady=20)

# title
rps_title = tk.Label(main_screen, text='Rock.. Paper.. Scissors!')
rps_title.grid(row=0, columnspan=4)

# player move
player_move = tk.Label(main_screen, text='Select a move:')
player_move.grid(row=1, column=0)
rock_option = tk.Button(main_screen, text='Rock', command=lambda:chosen_move('rock'))
rock_option.grid(row=1, column=1)
paper_option = tk.Button(main_screen, text='Paper', command=lambda:chosen_move('paper'))
paper_option.grid(row=1, column=2)
scissors_option = tk.Button(main_screen, text='Scissors', command=lambda:chosen_move('scissors'))
scissors_option.grid(row=1, column=3)

# result
result_title = tk.Label(main_screen, text='Result:')
result_title.grid(row=2, columnspan=4)
result_display = tk.Label(main_screen, textvariable=result)
result_display.grid(row=3, column=0)

# game summary
game_summary_title = tk.Label(main_screen, text='Game Summary:')
game_summary_title.grid(row=4, columnspan=4)
pmd_title = tk.Label(main_screen, text="Player's Move: ")
pmd_title.grid(row=5, column=0)
player_move_display = tk.Label(main_screen, textvariable=player)
player_move_display.grid(row=5, column=1)
amd_title = tk.Label(main_screen, text="AI Player's Move: ")
amd_title.grid(row=6, column=0)
ai_move_display = tk.Label(main_screen, textvariable=ai_player)
ai_move_display.grid(row=6, column=1)
wd_title = tk.Label(main_screen, text='Winner: ')
wd_title.grid(row=7, column=0)
winner_display = tk.Label(main_screen, textvariable=winner)
winner_display.grid(row=7, column=1)

root.mainloop()