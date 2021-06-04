import re

def count_words(sentence):
    
    word_list = re.findall('\w+\'\w+|[A-Za-z1-9]+', sentence)

    dictionary = {}
    for word in word_list:
        word = word.lower()
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
        
    return dictionary
