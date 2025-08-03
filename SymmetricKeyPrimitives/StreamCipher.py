from PRG import PRG
import secrets


def XOR_bytes(a,b):
    return bytes([a[i]^b[i] for i in range(len(a))]) # '^' is NOT exponentiation !! 0^0 = 0, 1^0 = 1 

def bitstring_to_bytes(bitstring):
    return bytes(int(bitstring[i:i+8], 2) for i in range(0, len(bitstring), 8))

def encrypt(message, pseudo_key):
    ciphertext = XOR_bytes(message, pseudo_key)
    return ciphertext

def decrypt(ciphertext, pseudo_key):
    plaintext = XOR_bytes(ciphertext, pseudo_key)
    return plaintext


if __name__ == '__main__':
    message = b"hello"

    keystream_bits = PRG(len(message) * 8)
    
    pseudo_key = bitstring_to_bytes(keystream_bits)

    ciphertext = encrypt(message, pseudo_key)
    
    decrypted = decrypt(ciphertext, pseudo_key)

    print("Original Message:", message)
    print("Ciphertext (hex):", ciphertext.hex())
    print("Decrypted:", decrypted)
