word = 'loser'
tries = 10
display = ["-"] * len(word)
guessed = set()

print ('Welcome to Hangman!')
print (f'You\'ll have {tries} tries, starting now...')
while tries > 0:
    print (" ".join(display)) #join, joins all elements of a list to a string separated by " "
    while True:
        guess = input ('Guess a letter: ').lower()
        if len(guess) == 1 and guess.isalpha():
            break
        print('Enter a single letter.')
    if guess in guessed:
         print('You already tried that letter.')
         tries -= 1
         continue
    guessed.add(guess)

    if guess in word:
        i = 0
        for i, letter in enumerate(word): #enumerate returns the index for i and the char to letter
            if guess == letter:
                display[i] = letter
        if "-" not in display:
            print (' '.join(display))
            print ('***YOU WIN***')
            break
        else:
            print(f'Correct! You have {tries} tries left.')
    else:
        tries -= 1
        print(f'Wrong. You have {tries} tries left.')
    
else:
    print (f'You\'ve been hanged. The word was: {word}.')
