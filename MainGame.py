from Live import load_game, welcome
from GuessGame import play as play_guess_game
from MemoryGame import play as play_memory_game
from CurrencyRoulletteGame import play as play_currency_game
from Score import add_score

print(welcome('Guy'))
user_inputs = load_game()
difficulty = int(user_inputs.get('difficulty'))

match int(user_inputs.get('chosen_game')):
    # Memory Game
    case 1:
        if play_memory_game(difficulty):
            add_score(difficulty)
            print('You won!')
        else:
            print('You lost!')
    # Guess Game
    case 2:
        if play_guess_game(difficulty):
            add_score(difficulty)
            print('You won!')
        else:
            print('You lost!')
    case 3:
        if play_currency_game(difficulty):
            add_score(difficulty)
            print('Close enough, You won!')
        else:
            print('You lost!')