full_dot = '●'
empty_dot = '○'

def create_character(name, strenght, intelligence, charisma):
    # Naming validation
    if not isinstance(name, str):
        return 'The character name should be a string'

    elif name == '':
        return 'The character should have a name'

    elif len(name) > 10:
        return 'The character name is too long'


    elif not name.isalpha():
        return 'The character name should not contain spaces'

    # stats validation
    elif not isinstance(strenght, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers'

    elif strenght < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'

    elif strenght > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'

    elif strenght + intelligence + charisma != 7:
        return 'The character should start with 7 points'
    else :
        strenght = full_dot * strenght + empty_dot*(10 - strenght)
        intelligence = full_dot * intelligence + empty_dot*(10 - intelligence)
        charisma = full_dot * charisma + empty_dot*(10 - charisma)

    return f"{name}\nSTR {strenght}\nINT {intelligence}\nCHA {charisma}"

x = create_character('rggfgg', 4, 2, 1)
print(x)
