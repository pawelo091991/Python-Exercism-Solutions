def sum_of_multiples(limit, multiples):

    # Store numbers that can be divided by multiples
    number_list = []

    # Check if multiples are not empty list
    if multiples:
        # Check any number between lowest multiple and limit
        for number1 in range(min(multiples), limit):
            # Divide by each multiple
            for number2 in multiples:
                # Don't divide by 0!
                if number2 == 0:
                    continue
                # Check if division is possible
                elif number1%number2 == 0:
                    # Add number to list
                    number_list.append(number1)
                    break
    
    # return sum of numbers 
    return sum(number_list)

