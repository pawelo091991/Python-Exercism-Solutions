def classify(number):

    if number <= 0:
        raise ValueError("Non positive value")

    tempNumber = number/2
    dividers = []

    while tempNumber > 0:
        if number % tempNumber == 0:
            dividers.append(tempNumber)
        
        tempNumber -= 1
    
    sumNumber = sum(dividers)

    if sumNumber == number:
        return "perfect"

    elif sumNumber > number:
        return "abundant"

    else:
        return "deficient"
