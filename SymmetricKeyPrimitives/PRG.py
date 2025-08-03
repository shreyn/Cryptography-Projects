"""
1. Input is a truly random string (seed)
2. Output length 
3. Cryptographic hash function - SHA256 (for now, treat as black box)
4. Counter - since the way we expand is by hashing the same seed over and over again, we need something that makes it different, but still traceable and reversible.
- So we concatenate the counter at the end of the seed
"""
import hashlib
import secrets

def PRG(desired_bits):
    seed = secrets.token_bytes(16) #128 bits
    output = b'' 
    desired_bytes = (desired_bits + 7) // 8

    for i in range((desired_bytes+31)//32):
        counter = i.to_bytes(4, 'big')
        data = seed + counter
        digest = hashlib.sha256(data).digest()
        output += digest

    result = output[:desired_bytes] #making it the desired length
    return ''.join(f'{byte:08b}' for byte in result) #converting bytes to bits


if __name__ == '__main__':
    res = PRG(512)
    print(res)
    print(str(len(res)) + ' bits')