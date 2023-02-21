import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Guess again, your number is too low')
        elif guess > random_number: 
            print('Guess again, your number is too high')
    print(f'{random_number} is the right number. Demand a promotion at work')

guess(10)