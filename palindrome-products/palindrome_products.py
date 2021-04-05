def products(min_factor, max_factor):
    palindrome_list = list()
    for x in range(min_factor, max_factor+1):
        for y in range(x, max_factor+1):
            if str(x*y) == str(x*y)[::-1]:
                palindrome_list.append([x,y])  

    return palindrome_list

def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Incorrect input")

    try:
        product = products(min_factor, max_factor)
        value = max([x*y for x,y in product])
        factors = [[x,y] for x,y in product if x*y == value]
        return value, factors
    except ValueError:
        return None, []

def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Incorrect input")

    try:
        product = products(min_factor, max_factor)
        value = min([x*y for x,y in product])
        factors = [[x,y] for x,y in product if x*y == value]
        return value, factors
    except ValueError:
        return None, []

