from collections import defaultdict
import re

def def_value():
    return 0

def count_words(sentence):
    
    word_regex = re.compile(
	r"""
			[0-9]+              # A number...
		|   [a-z]+ ' [a-z]+     # or a word with an apostrophe...
		|   [a-z]+              # or a word without an apostrophe.
	""",
	re.VERBOSE
    )
    
    results = word_regex.findall(sentence.lower())

    dictionary = defaultdict(def_value)

    for word in results:
        dictionary[word] += 1

    return dictionary
