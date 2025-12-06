full_dot = '●'
empty_dot = '○'

def put_dots(stat):
    str = ''
    for _ in range(stat):
        str += full_dot
    for _ in range(10 - stat):
        str += empty_dot
    return str

def create_character(character_name, strength, intelligence, charisma):
    if not isinstance(character_name, str):
        return 'The character name should be a string'
    elif len(character_name) > 10:
        return 'The character name is too long'
    elif character_name.find(' ') > 0:
        return 'The character name should not contain spaces'
    elif not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers'
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    elif (strength + intelligence + charisma) != 7:
        return 'The character should start with 7 points'
    else:
        string = (character_name + '\nSTR ' + put_dots(strength) + '\nINT ' + put_dots(intelligence) + '\nCHA ' + put_dots(charisma))
        return string
    
print (create_character("ren", 4, 2, 1))