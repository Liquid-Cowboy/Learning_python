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

def battle(best_of):
    player = 0
    house = 0
    for round in range(best_of):
        try:
            bet = int(input (f'{green}Round {round + 1}{reset} -> Chose between {brown}1. Rock{reset}, {blueish}2. Paper{reset}, {pinkish}3. Scissors{reset} (1-3) -> '))
        except (ValueError):
            print (f'{red}*ERROR*   Value must be a digit between 1 and 3.{reset}')
            round -= 1
            continue
        if 1 <= bet <= 3:
            bot = random.randint(1, 3)
            if bot == 1:
                if bet == 1:
                    print (f'   It\'s a draw. We both played {rock}.\n')
                elif bet == 2:
                    player += 1
                    print (f'   Darn\'it... you won! You played {paper}, I played {rock}.\n')
                else:
                    house += 1
                    print (f'   AHAH! I won! You played {scissors}, I played {rock}.\n')
            if bot == 2:
                if bet == 2:
                    print (f'   It\'s a draw. We both played {paper}.\n')
                elif bet == 3:
                    player += 1
                    print (f'   Darn\'it... you won! You played {scissors}, I played {paper}.\n')
                else:
                    house += 1
                    print (f'   AHAH! I won! You played {rock}, I played {paper}.\n')
            if bot == 3:
                if bet == 3:
                    print (f'   It\'s a draw. We both played {scissors}.\n')
                elif bet == 1:
                    player += 1
                    print (f'   Darn\'it... you won! You played {rock}, I played {scissors}.\n')
                else:
                    house += 1
                    print (f'   AHAH! I won! You played {paper}, I played {scissors}.\n')
        else:
            round -=1
            print ('Value must be between 1 and 3.')
    print ('The game has ended.')
    if house > player:
        print ('    MUAHAHAHAHAH! I WON!!! :\')')
    elif house < player:
        print ('    Aw man... You win... I\'m such a loser...')
    else:
        print ('    It\'s a draw!')


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