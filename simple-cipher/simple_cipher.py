class Cipher:

    key = list()
    
    def __init__(self, key=None):
        pass

    def encode(self, text):
        for char in text:
          if char.isalpha() == True:
                char = chr((ord(char) - 97 + 2) % 26 + 97)
                self.key.append(char)
        return self.key

    def decode(self, text):
        pass
