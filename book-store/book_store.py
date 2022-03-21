DISCOUNTS = [1, .95, .9, .8, .75]
def total(basket):
    if len(basket) == 0:
        return 0
    groups = []
    while len(basket) != 0:
        basket_set = set(basket)
        for member in basket_set:
            basket.remove(member)
        groups.append(len(basket_set))
        
    while {5, 3}.issubset(groups):
        groups.remove(5)
        groups.remove(3)
        groups += [4, 4]
    while {2, 3}.issubset(groups):
        groups.remove(2)
        groups.remove(3)
        groups += [4, 1]
    return sum([800 * group * DISCOUNTS[group - 1] for group in groups])