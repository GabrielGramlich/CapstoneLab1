import random as rnd

print('Computer is picking a number between (and including) 1 and 100')
number = rnd.randint(1, 100)

go = True
while go:
    guess = int(input('Guess the number: '))
    if guess < number:
        print('Too low.\n')
    elif guess == number:
        print('Correct!')
        go = False
    else:
        print('Too high.')
