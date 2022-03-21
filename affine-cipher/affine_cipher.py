from math import pow
LETTER_BASE = ord('a')
ALPHABET_LEN = 26
def encode(plain_text, a, b):
    _ = inverse(a)  # Validate the coprime
    encoded = "".join([chr(LETTER_BASE + ((a * (ord(x) - LETTER_BASE) + b) % ALPHABET_LEN))
                      if x.isalpha() else x for x in plain_text.lower() if x.isalnum()])
    return " ".join([encoded[i:i+5] for i in range(0, len(encoded), 5)])
def decode(ciphered_text, a, b):
    a_inverse = inverse(a)
    return "".join([chr(LETTER_BASE + (int(a_inverse * (ord(y) - LETTER_BASE - b))) % ALPHABET_LEN) if y.isalpha() else y for y in ciphered_text.lower() if y.isalnum()])
def inverse(a):
    result = [x for x in range(1, ALPHABET_LEN) if a*x % ALPHABET_LEN == 1]
    if len(result) >= 1:
        return result[0]
    else:
        raise ValueError("a and m must be coprime.")