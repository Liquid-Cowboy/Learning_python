import re

while True:
    user_input = input('Enter minimum and maximum value to guess: ')
    numbers = re.split('[\\ ]', user_input.strip())
    
    if len(numbers) == 2 and numbers[0].isdigit() and numbers[1].isdigit():
        minimum = int(numbers[0])
        maximum = int(numbers[1])
        if int(minimum) < int(maximum):
            break
    print('One or more of the values is incorrect. Minimum must be lower than maximum and values have to be separated by a \' \' or a \'|\'. ')