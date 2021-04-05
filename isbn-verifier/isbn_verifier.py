import re

def is_valid(isbn):

    if re.match(r'[0-9]{1}-?[0-9]{3}-?[0-9]{5}-?[0-9X]{1}', isbn) == None:
        return False

    isbn = isbn.replace('-','')

    if len(isbn) > 10:
        return False

    isbn = [int(char.replace('X', '10')) for char in isbn]

    if (isbn[0]*10 + isbn[1]*9 + isbn[2]*8 + isbn[3]*7 + isbn[4]*6
    + isbn[5]*5 + isbn[6]*4 + isbn[7]*3 + isbn[8]*2 + isbn[9]*1) % 11 == 0:
        return True

    else:
        return False