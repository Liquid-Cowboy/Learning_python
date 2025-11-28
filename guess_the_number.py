import re
import random
import sys

def limits():
    while True:
        user_input = input('Enter minimum and maximum value to guess: ')
        numbers = re.split('[| ]', user_input.strip())
        
        if len(numbers) == 2 and numbers[0].isdigit() and numbers[1].isdigit():
            min = int(numbers[0])
            max = int(numbers[1])
            if int(min) < int(max):
                break
        print('One or more of the values is incorrect. Minimum must be lower than maximum and values have to be digits and separated by a \' \' or a \'|\'. ')
    return (min, max)

def play_game():
    min, max = limits()
    n = random.randint(min,max)
    tries = (max-min) // 5 + 1

    while tries:
        guess = int(input(f'Guess a number (You have {tries} guesses left.) -> '))
        if guess == n:
            print('CORRECT!!! *YOU WON*')
            return        
        tries -= 1       
        if guess > n:
            print(f'Guess again. Number is lower than {guess}.')
        elif guess < n:
            print(f'Guess again. Number is higher than {guess}.')
    print('You lost...')
while True:
    play_game()
    again = input("Do you want to play again? (y/n): ").lower()
    if again != 'y':
        sys.exit()