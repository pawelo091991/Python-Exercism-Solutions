gift_list = [
        "",
        "a Partridge in a Pear Tree",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming"
]

number_list = [
        "",
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth"
]

def recite_day(verse):

    # Create gift list for the verse, if-else construction to resolve the unnecessary "and" for verse == 1 
    gifts = ", ".join(gift_list[verse:1:-1]) + ", and " + gift_list[1] if verse > 1 else gift_list[1]

    return f"On the {number_list[verse]} day of Christmas my true love gave to me: {gifts}." 


def recite(start_verse, end_verse):
    return [recite_day(verse) for verse in range(start_verse, end_verse+1)]
