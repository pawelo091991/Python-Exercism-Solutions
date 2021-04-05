def slices(series, length):

    N = len(series)
    if N <= 0 or length > N or length <= 0:
        raise ValueError("Lenght must be equal or lower than lenght of series")
    return [series[i : length+i] for i in range(N-length+1)]
