import random

_difficulty = -1
_secret_number = -1
_guess = -1


def generate_number():
    global _difficulty

    return random.randint(1, _difficulty)


def get_guess_from_user():
    while True:
        guess = input('Please choose a number from 1 to ' + str(_difficulty) + ': ')

        if not guess.isnumeric() or int(guess) < 1 or int(guess) > 5:
            print('Invalid Difficulty')
            continue

        break

    return int(guess)


def compare_results():
    global _guess

    return _secret_number == _guess


def play(difficulty):
    global _difficulty, _secret_number, _guess

    _difficulty = difficulty
    _secret_number = generate_number()
    _guess = get_guess_from_user()

    return compare_results()
