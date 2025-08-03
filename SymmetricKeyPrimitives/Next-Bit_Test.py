"""
Yao's Next-Bit Test
- simple logistic regression trained on true random bitstring
- model tries to predict the next bit
- compares accuracy of true random to the PRG, 
"""


import secrets
from PRG import PRG
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score



def build_dataset(bitstring, window):
    X, y = ([], [])

    for i in range(len(bitstring)-window):
        prefix = bitstring[i:i+window]
        next_bit = bitstring[i+window]

        X.append([int(b) for b in prefix])
        y.append(int(next_bit))

    return X, y

def training_model(num_samples=20, bitstring_len=512, window=16):
    X, y = ([], [])
    
    for i in range(num_samples):
        random_bits = ''.join(secrets.choice('01') for _ in range(bitstring_len))
        Xtrain, ytrain = build_dataset(random_bits, window)
        X.extend(Xtrain)
        y.extend(ytrain)

    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    return model

def evaluate_model(model, bitstring_generator, window=16, bitstring_len=512):
    bitstring = bitstring_generator(bitstring_len)
    X_test , y_test = build_dataset(bitstring, window)
    
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    return acc


def random_bitstring(n=512):
    return ''.join(secrets.choice('01') for _ in range(n))

def prg_bitstring(n=512):
    return PRG(n)


if __name__ == '__main__':
    trials = 30
    acc_random_total = 0
    acc_prg_total = 0

    for i in range(trials):
        model = training_model(num_samples=100, window=16)
        acc_random = evaluate_model(model, random_bitstring, window=16)
        acc_prg = evaluate_model(model, prg_bitstring, window=16)
        acc_random_total += acc_random
        acc_prg_total += acc_prg
        print(f"[Trial {i+1}] Random: {acc_random:.3f}, PRG: {acc_prg:.3f}")

    print("\n--- Average Accuracy Over Trials ---")
    print(f"Average accuracy on truly random bits: {acc_random_total / trials:.3f}")
    print(f"Average accuracy on PRG output:        {acc_prg_total / trials:.3f}")
