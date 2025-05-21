from math import gcd

def mod_inverse(e, phi):
    def extended_euclidean(a, b):
        if b == 0:
            return (a, 1, 0)
        else:
            g, x1, y1 = extended_euclidean(b, a%b)
            x = y1
            y = x1 - (a//b) * y1
            return (g, x, y)
    
    g, x, i = extended_euclidean(e, phi)
    if g != 1: raise Exception("Mod inv does not exist.")
    
    return x % phi

def key_generation(p, q, e):
    n = p * q #n is prod of two distinct primes
    phi = (p - 1) * (q - 1) #euler's totient function
    assert gcd(e, phi) == 1
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def square_and_multiply(base, exponent, mod):
    res = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:  #if the lowest bit is 1
            res = (res * base) % mod
        base = (base * base) % mod  #then, always square
        exponent = exponent // 2
    return res


def encrypt(m, public_key):
    e, n = public_key
    return square_and_multiply(m, e, n)

def decrypt(c, private_key):
    d, n = private_key
    return square_and_multiply(c, d, n)

if __name__ == "__main__":
    # set to large numbers
    p = 1000000007
    q = 1000000009
    e = 65537

    public_key, private_key = key_generation(p, q, e)

    print("Public key:", public_key)
    print("Private key:", private_key)

    # message
    m = 1203129
    c = encrypt(m, public_key)
    m_decrypted = decrypt(c, private_key)

    print("Original message:", m)
    print("Encrypted:", c)
    print("Decrypted:", m_decrypted)


