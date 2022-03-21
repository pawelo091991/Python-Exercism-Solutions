import math

def primes(limit):
    arr = [True] * (limit+1)
    for i in range (2, int(math.sqrt(limit))+1):
        if arr[i] == True:
            for j in range(2*i, limit+1, i):
                arr[j] = False

    return [idx for idx in range(2, limit + 1) if arr[idx] == True]
