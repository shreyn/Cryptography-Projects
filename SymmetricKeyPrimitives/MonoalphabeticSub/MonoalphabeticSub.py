import string
import random


ALPHABET = string.ascii_lowercase

def generate_random_key():
    letters = list(ALPHABET)
    random.shuffle(letters)
    return ''.join(letters)

def encryption(message, key):
    output = ''
    for letter in message.lower():
        pos = ALPHABET.find(letter)
        newLetter = key[pos]
        output += newLetter
    return output

def decryption(ciphertext, key):
    output = ''
    for letter in ciphertext:
        pos = key.find(letter)
        newLetter = ALPHABET[pos]
        output += newLetter
    return output


def main():
    message = 'hello'
    key = generate_random_key()
    print('Message: ' + message)
    ciphertext = encryption(message, key)
    print('Ciphertext: ' + ciphertext)
    plaintext = decryption(ciphertext, key)
    print('Plaintext: ' + plaintext)

if __name__ == '__main__':
    main()
