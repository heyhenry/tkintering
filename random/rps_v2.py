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
on_main = True

# outside of functions to be able to execute it's sub-commands appropriately (.forget, .pack)
summary_screen = tk.Frame(root)

# display the main screen (game screen/starting screen)
def run_main():
    
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
        
        # hides the main screen in lieu of the summary screen
        main_screen.forget()
        run_summary()

    # process playe move and start game
    def chosen_move(move : str):
        player.set(move)
        play_game()

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

    # hides the summary screen and its widgets
    summary_screen.forget()

    def run_summary():
        
        # makes the summary screen and its widgets visible
        summary_screen.pack(padx=20, pady=20)

        # game summary
        game_summary_title = tk.Label(summary_screen, text='Game Summary:')
        game_summary_title.grid(row=0, columnspan=4)
        pmd_title = tk.Label(summary_screen, text="Player's Move: ")
        pmd_title.grid(row=1, column=0)
        player_move_display = tk.Label(summary_screen, textvariable=player)
        player_move_display.grid(row=1, column=1)
        amd_title = tk.Label(summary_screen, text="AI Player's Move: ")
        amd_title.grid(row=2, column=0)
        ai_move_display = tk.Label(summary_screen, textvariable=ai_player)
        ai_move_display.grid(row=2, column=1)
        wd_title = tk.Label(summary_screen, text='Winner: ')
        wd_title.grid(row=3, column=0)
        winner_display = tk.Label(summary_screen, textvariable=winner)
        winner_display.grid(row=3, column=1)
        restart_btn = tk.Button(summary_screen, text='Restart Game', command=run_main)
        restart_btn.grid(row=4, columnspan=2)

# initially starts with the main screen when program opens
run_main()

root.mainloop()