'''

'''

from PRG import PRG


def xor_bits(a, b):
    return ''.join(['0' if x == y else '1' for x, y in zip(a, b)])

#### Round Key ####
PC1 = [ #64 bits -> 56 bits (just drops 8 bits)
    57, 49, 41, 33, 25, 17, 9,
     1, 58, 50, 42, 34, 26, 18,
    10,  2, 59, 51, 43, 35, 27,
    19, 11,  3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
     7, 62, 54, 46, 38, 30, 22,
    14,  6, 61, 53, 45, 37, 29,
    21, 13,  5, 28, 20, 12, 4
]

ROTATIONS = [ #how much the C,D rotate per round
    1, 1, 2, 2, 2, 2, 2, 2,
    1, 2, 2, 2, 2, 2, 2, 1
]

PC2 = [ #56 (C and D halves) -> 48
    14, 17, 11, 24,  1,  5,
     3, 28, 15,  6, 21, 10,
    23, 19, 12,  4, 26,  8,
    16,  7, 27, 20, 13,  2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

def left_rotate(bits, n):
    return bits[n:] + bits[:n]

def generate_round_keys(key):
    round_keys = []
    keys56 = ''.join([key[i-1] for i in PC1])
    C, D = keys56[:28], keys56[28:] # 2 halfs
    for i in range(16): #16 rounds
        shift = ROTATIONS[i]
        C = left_rotate(C, shift)
        D = left_rotate(D, shift)
        CD = C + D # 56
        keys48 = ''.join([CD[i-1] for i in PC2 ])
        round_keys.append(keys48)
    return round_keys


#### Round Function ####

E_TABLE = [ #expantion - duplicates half the bits
    32,  1,  2,  3,  4,  5,
     4,  5,  6,  7,  8,  9,
     8,  9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32,  1
]

# Full 8 S-boxes (each is a 4x16)
S_BOXES = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

P_TABLE = [ #permutation (1th bit -> 16, etc)
    16, 7, 20, 21,
    29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2,  8, 24, 14,
    32, 27,  3,  9,
    19, 13, 30,  6,
    22, 11,  4, 25
]


def round_function(part, k):
    # 1. expansion (E-box): 32bits -> 48 bits. DIFFUSION
    expanded = ''.join([part[i-1] for i in E_TABLE]) #ith bit in part, in the fixed order of the E_TABLE
    # 2. XOR with round key
    mixed = xor_bits(expanded, k)
    # 3. Substitution (S-box): nonlinear function. Substitutes 8 chunks of 6-bits -> 4 bits. CONFUSION
    chunks = [mixed[i:i+6] for i in range(0, 48, 6)] # 8 chunks
    sbox_output = '' #becomes 32 bits
    for i in range(8):
        chunk = chunks[i]
        row = int(chunk[0] + chunk[5], 2) #first and last are the row index
        col = int(chunk[1:5], 2) #middle 1-4 bits are the column index
        val = S_BOXES[i][row][col] #from the table
        sbox_output += f'{val:04b}' #conver the val to 4-bit binary
    # 4. Permutation (P-box): Diffusion (spreads out the 4 bits influenced by each S-box, so that next round, the same 4 bits aren't together again)
    permuted = ''.join([sbox_output[i-1] for i in P_TABLE])
    return permuted

def encryption(message, round_keys):
    L, R = message[:32], message[32:]
    for k in round_keys:
        newL = R
        newR = xor_bits(L,round_function(R, k))
        L, R = newL, newR
    
    return R + L

def decryption(ciphertext, round_keys):
    L, R = ciphertext[:32], ciphertext[32:]
    for k in round_keys[::-1]:
        newL = R
        newR = xor_bits(L, round_function(R,k))
        L, R = newL, newR
    return L + R



if __name__ == '__main__':
    message = '1010101010101010101010101010101010101010101010101010101010101010' #64 bits
    print('Message: ' + message)
    key = PRG(64)
    round_keys = generate_round_keys(key)
    ciphertext = encryption(message, round_keys)
    print('Ciphertext: ' + ciphertext)
    plaintext = decryption(ciphertext, round_keys)
    print('Plaintext: ' + plaintext)
    print('Does message = plaintext?: ' + str((message == plaintext)))