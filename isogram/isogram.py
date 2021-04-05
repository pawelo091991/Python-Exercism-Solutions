def is_isogram(string):
    
    letter = list()

    for char in string.lower():
        if char.isalpha() and char in letter:
            return False
        else:
            letter.append(char)

    return True
