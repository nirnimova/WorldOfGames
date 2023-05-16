def welcome(name):
    if not isinstance(name, str):
        name = 'stranger'

    return f'''
        Hello {name} and welcome to the World of Games (WoG).
            Here you can find many cool games to play.
    '''


def load_game():
    chosen_game = -1

    while True:
        chosen_game = input('''
            Please choose a game to play:
                1. Memory Game - a sequence of numbers will appear for 1 second and you have to
            guess it back
                2. Guess Game - guess a number and see if you chose like the computer
                3. Currency Roulette - try and guess the value of a random amount of USD in ILS
        ''')

        if not chosen_game.isnumeric() or int(chosen_game) < 1 or int(chosen_game) > 3:
            print('Invalid Game')
            continue

        break

    difficulty = -1

    while True:
        difficulty = input('Please choose game difficulty from 1 to 5: ')

        if not difficulty.isnumeric() or int(difficulty) < 1 or int(difficulty) > 5:
            print('Invalid Difficulty')
            continue

        break

    return {'chosen_game': chosen_game, 'difficulty': difficulty}

