def verify_card_number(card_number):
    """
    Verify if a given card number is valid using the Luhn algorithm.

    The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers, 
    such as credit card numbers. The algorithm works as follows:
    1. Reverse the card number.
    2. Sum all digits in the odd positions (1st, 3rd, 5th, etc.).
    3. For digits in the even positions (2nd, 4th, 6th, etc.), double each digit. If the result is greater 
       than or equal to 10, sum the digits of the result (i.e., add the tens and units place digits).
    4. Sum all the results from steps 2 and 3.
    5. If the total modulo 10 is 0, the card number is valid.

    Args:
        card_number (str): The card number to be verified.

    Returns:
        bool: True if the card number is valid, False otherwise.
    """
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits

    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()