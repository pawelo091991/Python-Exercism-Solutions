def score(x, y):

    dist = (pow(x,2) + pow(y,2)) ** 0.5
    return {dist <= 1: 10, 1 < dist <= 5: 5, 5 < dist <= 10: 1}.get(True, 0)
