"""
This exercise stub and the test suite contain several enumerated constants.
 
Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).
 
You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3

def algo(sub , lst):
    len_sub = len(sub)
    for idx in range(0, len(lst) - len_sub +1):
        if sub == lst[idx : idx + len_sub]:
            return True
    return False
    
def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif len(list_one) > len(list_two):
        return SUPERLIST if len(list_two) == 0 or algo(list_two, list_one)  else UNEQUAL
    elif len(list_one) < len(list_two):
        return SUBLIST if len(list_one) == 0 or algo(list_one, list_two)  else UNEQUAL
    else:
        return UNEQUAL