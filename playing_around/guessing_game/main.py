import random

randnum = random.randint(1, 10)
ai = random.randint(1, 10)
player = int(input('Choose a number between 1 and 10.'))

def game_summary():
    print('== Game Summary ==')
    print(f'ai picked {ai}')
    print(f'player picked {player}')
    print(f'the random number was {randnum}')
    print('== === === ==')

if ai == randnum:
    print('ai won!')
elif player == randnum:
    print('player won!')
else:
    print(f'Noone won. The number in question was {randnum}')
    
game_summary()
