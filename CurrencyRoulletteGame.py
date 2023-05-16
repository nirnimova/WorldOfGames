import requests
import random

# Where USD is the base currency you want to use
_exchangeRateURL = 'https://v6.exchangerate-api.com/v6/45292d251627b2a2274ca2e2/latest/USD'
_difficulty = -1
_randomCost = -1
_rate = -1
_interval = []
_guess = -1


def get_money_interval():
    global _difficulty, _randomCost, _rate

    response = requests.get(_exchangeRateURL)
    data = response.json()
    _rate = data['conversion_rates']['ILS']
    _randomCost = random.randint(1, 101)
    totalValue = _rate * _randomCost

    return [totalValue - (5 - _difficulty), totalValue + (5 - _difficulty)]


def get_guess_from_user():
    global _randomCost

    return input(f'Please enter your guess for {_randomCost} USD in ILS: ')


def is_guess_equal():
    return _interval[0] <= float(_guess) <= _interval[1]


def play(difficulty):
    global _difficulty, _interval, _guess, _randomCost, _rate

    print('Currency Roulette - try and guess the value of a random amount of USD in ILS')

    _difficulty = difficulty
    _interval = get_money_interval()
    _guess = get_guess_from_user()

    print(f'The answer is {_rate * _randomCost}, your guess was {_guess}')

    return is_guess_equal()