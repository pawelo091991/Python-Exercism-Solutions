def count_words(sentence):

    for sign in '-.,\n:_!&@$%^&':
        sentence = sentence.replace(sign, ' ')

    sentence = sentence.lower()
    word_list = sentence.split()

    d = {}
    for word in word_list:
        while word[0] == "'" and word[-1] == "'":
            word = word[1:-1]
        d[word] = d.get(word, 0) + 1

    return d
