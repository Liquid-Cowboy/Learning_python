full_dot = '●'
empty_dot = '○'

def validate_name(character_name):
    if not isinstance(character_name, str):
        print('The character name should be a string.')
        return False
    elif len(character_name) > 10:
        print('The character name is too long.')
        return False
    elif character_name.find(' ') > 0:
        print('The character name should not contain spaces.')
        return False
    else:
        return True
    
def validate_atributes(strength, intelligence, charisma):
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        print('All stats should be integers.')
        return False
    elif strength < 1 or intelligence < 1 or charisma < 1:
        print('All stats should be no less than 1.')
        return False
    elif strength > 4 or intelligence > 4 or charisma > 4:
        print('All stats should be no more than 4.')
        return False
    elif (strength + intelligence + charisma) != 7:
        print('The character should start with 7 points.')
        return False   
    else:
        return True

def put_dots(stat):
    str = ''
    for _ in range(stat):
        str += full_dot
    for _ in range(10 - stat):
        str += empty_dot
    return str

def create_character():
    character_name = input('Please enter a character name: ')
    while not validate_name(character_name):
        character_name = input('Please enter a character name: ')
    strength, intelligence, charisma = int(input('Strength: ')), int(input('Intelligence: ')), int(input('Charisma: '))
    while not(validate_atributes(strength, intelligence , charisma)):
        strength, intelligence, charisma = int(input('Strength: ')), int(input('Intelligence: ')), int(input('Charisma: '))
    print(character_name + '\nSTR ' + put_dots(strength) + '\nINT ' + put_dots(intelligence) + '\nCHA ' + put_dots(charisma), end='')

create_character()