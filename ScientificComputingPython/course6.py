import re
import secrets
import string

def generate_password(length: int = 16, nums: int = 1, special_chars: int = 1, uppercase: int = 1, lowercase: int = 1) -> str:
    """
    Generate a random password with specified constraints.

    Args:
        length (int): Length of the password. Default is 16.
        nums (int): Minimum number of digits. Default is 1.
        special_chars (int): Minimum number of special characters. Default is 1.
        uppercase (int): Minimum number of uppercase letters. Default is 1.
        lowercase (int): Minimum number of lowercase letters. Default is 1.

    Returns:
        str: The generated password.
    """
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password

if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)
