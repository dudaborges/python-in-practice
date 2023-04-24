import time
from random import choice

print('''Your options:
[0] Rock
[1] Paper
[2] Scissors
''')
options = ['Rock', 'Paper', 'Scissors']
move = int(input('Whats your move?'))
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO')
time.sleep(0.5)
optionComputer = choice(options)
print('The computer threw {}'.format(optionComputer))

if(move == 1):
    move = 'Rock'
elif(move == 2):
    move = 'Paper'
elif(move == 3):
    move = 'Scissors'
else:
    print('[ERROR]')
print('The player threw {}'.format(move))

if(move == optionComputer):
    print('Game draw')
elif(optionComputer == 'Rock'):
    if(move == 'Paper'):
        print('Player is the winner')
    elif(move == 'Scissors'):
        print('Computer is the winner')
elif (optionComputer == 'Paper'):
    if(move == 'Rock'):
        print('Computer is the winner')
    elif(move == 'Scissors'):
        print('Player is the winner')
elif(optionComputer == 'Scissors'):
    if (move == 'Rock'):
        print('Player is the winner')
    elif (move == 'Paper'):
        print('Computer is the winner')
else:
    print('[ERROR]')
