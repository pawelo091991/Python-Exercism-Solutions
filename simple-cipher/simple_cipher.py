from random import randrange, seed
from random import random

class Cipher:
    
    key = ""
    
    def __init__(self, key=None):
        if key is None:
            seed(1)
            for i in range(0,100):
                self.key += chr(randrange(97,122))
        else:
            for char in key:
                self.key = key

    def encode(self, text):
        encodeStr = ""
        for i in range(0, len(text)):
            if text[i].isalpha() == True:
                encodeStr += chr((ord(text[i]) - 97 + ord(self.key[i%len(self.key)]) - 97) % 26 + 97)
        return encodeStr

    def decode(self, text):
        decodeStr = ""
        for i in range(0, len(text)):
            if text[i].isalpha() == True:
                decodeStr += chr((ord(text[i]) - 97 - (ord(self.key[i%len(self.key)]) - 97)) % 26 + 97)
        return decodeStr
