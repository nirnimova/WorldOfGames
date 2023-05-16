import time
import random
import os

_difficulty = -1
_sequence = -1
_guess = -1


def generate_sequence():
    global _difficulty

    sequences = []
    for seq in range(_difficulty):
        sequences.append(str(random.randint(1, 101)))

    return ' '.join(sequences)


def get_list_from_user():
    return input('Please repeat sequence (with spaces between each number)')


def is_list_equal():
    return _sequence == _guess


def play(difficulty):
    global _difficulty, _sequence, _guess

    _difficulty = difficulty
    _sequence = generate_sequence()

    # Show and hide sequence from user
    print(_sequence)
    time.sleep(0.7)
    os.system('cls')

    _guess = get_list_from_user()

    return is_list_equal()