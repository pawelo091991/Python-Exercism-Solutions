def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands lenght aren't the same\n")

    return sum([ch1 != ch2 for ch1,ch2 in zip(strand_a, strand_b)])
    
