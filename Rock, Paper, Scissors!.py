import random

options = {'Rock': 'Paper', 'Paper': 'Scissors', 'Scissors': 'Rock'}
           
def move(option, strikes):  
    rand_option = random.choice(list(options.keys()))
    if rand_option == option:
        print('[Gamebot] Tie! (%s = %s)' % (option, rand_option))
        return strikes  # Tie
    elif rand_option == options[option]:
        print('[Gamebot] Loss! (%s < %s)' % (option, rand_option))
        return strikes - 1  # Loss
    else:
        print('[Gamebot] Win! (%s > %s)' % (option, rand_option))
        return strikes + 1 # Win
    
def valid_input(prompt, valid_values, cast_value_to_int=False):
    while True:
        value = input(prompt + ' (Type "EXIT" to Exit): ')
        if value.upper() == 'EXIT':
            print('[Gamebot] Exiting...')
            exit()
        elif cast_value_to_int:
            try:
                value = int(value)
            except:
                print('[Gamebot] Invalid Input Type - Expected an Integer (!)')
        if value not in valid_values:
            print('[Gamebot] Invalid Value (!)')
        else:
            return value

if __name__ == '__main__':
    # Pre-Game
    moves = 0
    strikes = 6
    
    # Game
    print('Welcome to ROCK-PAPER-SCISSORS!\n')
    while True:
        print('[Gamebot] Strikes: %d, Moves: %d' % (strikes, moves))
        option = valid_input('[Gamebot] Select Option (1 Rock, 2 Paper, 3 Scissors)', ['1', '2', '3'])
        option = list(options.keys())[int(option) - 1]
        strikes = move(option, strikes)
        if strikes == 0:
            print('[Gamebot] Game Over!, Moves: %d' % moves)
            break
        moves += 1
