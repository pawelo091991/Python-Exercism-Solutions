def abbreviate(words):
    return ''.join([letter.upper()[0] for letter in words.replace('-', ' ').replace('_', '').split()])
