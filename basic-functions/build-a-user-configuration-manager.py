'''
Docstring for scripts.build-a-user-configuration-manager

A basic user configuration manager that allows adding, updating, deleting, and viewing user settings.
Further enhancements can include validation of settings, persistence to a file or database, and a user interface.
'''
test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}

# add setting function
def add_setting(settings:dict, key_value_pair:tuple):
    '''
    Docstring for add_setting
    
    :param settings: Settings dictionary with key-value pairs
    :param key_value_pair: a tuple type key-val pair to be added to settings
    '''
    # changing keys-values to lowercase
    to_lower_pair = tuple(item.lower() if isinstance(item, str) else item for item in key_value_pair)
    key = to_lower_pair[0]
    value = to_lower_pair[1]

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else :
        settings[str(key)] = value
        return f"Setting \'{key}\' added with value \'{value}\' successfully!"
    
print(add_setting(test_settings, ('power', 'on')))
print(test_settings)

# update setting function
def update_setting(settings:dict, update_key_val:tuple):
    '''
    Docstring for update_setting
    
    :param settings: Settings dictionary with key-value pairs
    :param update_key_val: a tuple type key-val pair to be updated in settings
    '''
    # changing key-value to lowercase
    update_pair = tuple(item.lower() if isinstance(item, str) else item for item in update_key_val)
    key = update_pair[0]
    value = update_pair[1]

    if key in settings:
        settings[str(key)] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else :
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

print(update_setting(test_settings, ('theme','blue')))
print(test_settings)

# delete setting function
def delete_setting(settings:dict, to_delete_key:str):
    '''
    Docstring for delete_setting
    
    :param settings: Settings dictionary with key-value pairs
    :param to_delete_key: key to be deleted from settings
    '''
    # changing key to lowercase
    key = to_delete_key.lower()

    if key in settings:
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else :
        return "Setting not found!"

print(delete_setting(test_settings, 'thEme'))
print(test_settings)

empty_settings = {}

# view setting function
def view_settings(settings:dict):
    '''
    Docstring for view_settings
    
    :param settings: Settings dictionary with key-value pairs to be verify and shown in a formatted way
    '''
    if settings == {}:
        return 'No settings available.'
    else :
        result_settings = ''
        for key, value in settings.items():
            key_capitalized = key.capitalize()
            result_settings += f'\n{key_capitalized}: {value}'
    
    return f"Current User Settings:"+ result_settings + '\n'

print('\n',view_settings(empty_settings))
print('\n')
print(view_settings(test_settings))
print(test_settings)