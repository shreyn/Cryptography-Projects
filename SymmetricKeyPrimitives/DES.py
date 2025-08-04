from PRG import PRG


message = '10101010101010101010101010101010' #32 bits
key = PRG(56)
round_keys = [key[i:i+48] for i in range(16)] # 16 rounds


def xor_bits(a, b):
    return ''.join(['0' if x == y else '1' for x, y in zip(a, b)])


def round_function(part, k):
    return something

def encryption(message, round_keys):
    L, R = message[:16], message[16:]
    for k in round_keys:
        newL = R
        newR = xor_bits(L,round_function(R, k))
        L, R = newL, newR
    
    return R + L

def decryption(ciphertext, round_keys):
    L, R = ciphertext[:16], ciphertext[16:]
    for k in round_keys:
        newR = L
        newL = xor_bits(R, round_function(L,k))
        L, R = newL, newR
    return L + R