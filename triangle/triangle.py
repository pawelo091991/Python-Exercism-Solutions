def equilateral(sides):
    if 0 not in sides and len(set(sides)) == 1:
        return True
    else:
        return False


def isosceles(sides):
    sorted_sides = sorted(sides)
    if (sorted_sides[0] + sorted_sides[1]) > sorted_sides[2] and len(set(sides)) <= 2:
        return True
    else:
        return False


def scalene(sides):
    sorted_sides = sorted(sides)
    if (sorted_sides[0] + sorted_sides[1]) > sorted_sides[2] and len(set(sides)) == 3:
        return True
    else:
        return False
