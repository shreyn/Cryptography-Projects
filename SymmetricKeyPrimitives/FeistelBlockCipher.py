from PRG import PRG


def xor_bits(a, b):
    return ''.join(['0' if x == y else '1' for x, y in zip(a, b)])

def round_function(part, key):
    return xor_bits(part, key) #can be anything (doesn't have to be invertible, for simplicity is just XOr)

def feistel_encrypt(message, round_keys):
    L, R = message[:4], message[4:]
    for k in round_keys:
        newL = R
        newR = xor_bits(L, round_function(R, k))
        L, R = newL, newR
    return L + R

def feistel_decrypt(ciphertext, round_keys):
    L, R = ciphertext[:4], ciphertext[4:]
    for k in round_keys[::-1]:
        newR = L
        newL = xor_bits(R, round_function(L,k))
        L, R = newL, newR
    return L + R

if __name__ == "__main__":
    message = '10110110' #8 bits
    key = PRG(8) # master key of 8 bits
    round_keys = [key[i:i+4] for i in range(4)] #overlapping, derived from main key, length of 4 (half of 8)

    print("Plaintext:   ", message)
    ciphertext = feistel_encrypt(message, round_keys)
    print("Ciphertext:  ", ciphertext)
    decrypted = feistel_decrypt(ciphertext, round_keys)
    print("Decrypted:   ", decrypted)