def factors(value):
    divisor_list = list()
    divisor = 2
    while value != 1:
        if value % divisor != 0:
            divisor += 1
        else:
            value /= divisor
            divisor_list.append(divisor)

    return divisor_list
    
