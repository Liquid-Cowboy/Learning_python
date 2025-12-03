import random
limit = 10
reset = '\033[00m'
rock = '\033[38;5;94mRock\033[00m'
paper = '\033[38;5;62mPaper\033[00m'
scissors = '\033[38;5;168mScissors\033[00m'
brown = '\033[38;5;94m'
blueish = '\033[38;5;62m'
pinkish = '\033[38;5;168m'
red = '\033[38;5;196m'
green = '\033[92m'

def result(bet, bot):
    if bet == bot:
        return "draw"
    winning = {1:0, 2:1, 0:2}
    return "player" if winning[bet] == bot else "bot"

def main():
    while True:
        try:
            best_of = int(input (f'Welcome to {green}Rock, Paper, Scissors{reset}!\nPlease chose how long the game will last (to the best of 1 - {limit}): '))
        except (ValueError):
            print (f'{red}*ERROR*   Value must be a digit between 1 and {limit}.{reset}')
            continue
        if 1 <= best_of <= limit:
            battle(best_of)
            while True:
                again = input ('Do you want to play again? (y/n) ')
                if again == 'n':
                    return
                elif again != 'y':
                    print ('Please enter a valid answer.')
                    break
        else:
            print (f'{red}Value must be between 1 and {limit}.{reset}')
        
main()