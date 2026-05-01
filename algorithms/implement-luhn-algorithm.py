import re

def verify_card_number(card_number):
    """
    Verify a card number using the Luhn algorithm.

    The Luhn algorithm is a checksum formula used to validate
    identification numbers like credit card numbers.

    It works by:
    1. Removing non-digit separators.
    2. Separating the final check digit from the rest of the number.
    3. Doubling every second digit from right to left.
    4. Summing the digits of any products greater than 9.
    5. Adding the check digit and verifying the total is divisible by 10.

    Args:
        card_number (str): The card number to validate, which may include spaces,
            hyphens, or underscores.

    Returns:
        str: 'VALID!' if the number passes the Luhn checksum, otherwise 'INVALID!'.
    """
    clean_number = re.sub(r'[-_ ]', '', card_number)

    check_digit = [int(clean_number[-1])]
    main_digits = clean_number[0:len(clean_number)-1]

    digits = [int(d) for d in main_digits]

    # Double every second digit starting from the rightmost of the main digits
    for i in range(len(digits) - 1, -1, -2):
        digits[i] *= 2

    # If doubling produces a two-digit number, sum its digits
    # Example: 16 -> 1 + 6 = 7
    sum_two_char_digits = [(n // 10 + n % 10) if n > 9 else n for n in digits]

    # Add the processed digits together with the original check digit
    card_number = sum_two_char_digits + check_digit
    card_number = sum(card_number)

    # A valid Luhn number has a total sum divisible by 10
    if card_number % 10 == 0:
        return 'VALID!'
    return 'INVALID!'

if __name__ == '__main__':
    # Example usage: check a few card numbers via the Luhn formula
    print(verify_card_number('453914889'))
    print(verify_card_number('1234 5678 9012 3456'))
    print(verify_card_number('1234 5678 9012 3456'))