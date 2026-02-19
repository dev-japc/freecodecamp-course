def caesar(text, shift, encrypt=True):
    """
    This is an exercise from FreeCodeCamp python course in which we made a basic encryption program
    to learn how encryption works, but basically the idea was to use the knowledge learnt so far at that point
    related to variables, conditionals, logical operators, built-in functions, etc.
    """

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift

        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
        encrypted_text = text.translate(translation_table)
        return encrypted_text

    def encrypt(text, shift):
        return caesar(text, shift)

    def decrypt(text, shift):
        return caesar(text, shift, encrypt=False)
    encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
    decrypted_text = decrypt(encrypted_text, 13)
    print(decrypted_text)
