import time
from RSA import key_generation
import random
from sympy import nextprime




## initial values/keys ##
p = nextprime(2**512) #very large numbers (so time taken is noticeable)
q = nextprime(2**513)
e = 65537
public_key, private_key = key_generation(p, q, e)
_, d = private_key  # for reference
_, n = public_key

## SquareAndMultiply with timing ##
def timed_square_and_multiply(base, exponent, mod):
    base = base % mod
    res = 1

    start_time = time.perf_counter()  #start time

    while exponent > 0:
        if exponent % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exponent = exponent // 2

    end_time = time.perf_counter() #stop time
    time_taken = end_time - start_time

    return res, time_taken


## Attempting decryption (also returns time taken) ##
def decryption_machine(ciphertext, private_key):
    d, n = private_key
    m, t = timed_square_and_multiply(ciphertext, d, n)
    return t #the attacker can only sees the time (not the actual m)


def simulate_attacker(public_key, private_key, trials=100):
    times = []
    for _ in range(trials):
        m = random.randint(2, n - 1)
        c = pow(m, public_key[0], public_key[1])  #encryption
        t = decryption_machine(c, private_key) #only gets the time from decryption
        times.append(t)
    return times

# === Run simulation ===
if __name__ == "__main__":
    observed_times = simulate_attacker(public_key, private_key)
    print("Sample observed decryption times:")
    for i, t in enumerate(observed_times[:10]):
        print(f"Ciphertext {i+1}: time = {t:.4f} units")
