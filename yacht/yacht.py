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

from enum import Enum

# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    
    result = 0

    if category == 0: 
        if len(set(dice)) == 1:
            result = 50
        else:
            result = 0


    elif category >= 1 and category <= 6:
        for number in dice:
            if number == category:
                result += category


    elif category == 7 or category == 8:
        types = list(set(dice))
        if len(types) == 1 and category == 8:
            for number in range(4):
                result += dice[number]

        elif len(types) == 1 and category == 7:
            result = 0

        elif len(types) > 2:
            result = 0

        else:
            print(types[0])
            dic = {types[0]: 0, types[1]: 0}
            for number in dice:
                dic[number] += 1

            if category == 7:
                if (dic[types[0]] == 2 and dic[types[1]] == 3) or (dic[types[0]] == 3 and dic[types[1]] == 2):
                    result = sum(dice)
                else:
                    result = 0
            
            else:
                if dic[types[0]] == 1 and dic[types[1]] == 4: 
                    result = types[1] * 4

                elif dict[types[0]] == 4 and dic[types[1]] == 1:
                    result = types[0] * 4

                else:
                    result = 0

    elif category == 9 or category == 10:
        if len(dice) != len(set(dice)):
            result = 0
        
        else:
            if category == 9 and all(x in set(dice) for x in [1,2,3,4,5]): 
                result = 30

            elif category == 10 and all(x in set(dice) for x in [2,3,4,5,6]):
                result = 30

            else:
                result = 0

    else:
        result = sum(dice)

    return result
    
                     