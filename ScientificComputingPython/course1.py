# Learn String Manipulation by Building a Cipher

text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

def vigenere(message: str, key: str, direction: int = 1) -> str:
    """
    Encrypts or decrypts a message using the Vigenère cipher.

    Parameters:
    - message (str): The message to be encrypted or decrypted.
    - key (str): The encryption/decryption key.
    - direction (int, optional): The direction of the cipher. Use 1 for encryption and -1 for decryption. Default is 1.

    Returns:
    - str: The encrypted or decrypted message.
    """
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')
