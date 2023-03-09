def is_valid_triangle(sides):
    if (sides.count(0) > 0):
        return False
    return (sides[0] + sides[1] >= sides[2]) and (sides[1] + sides[2] >= sides[0]) and (sides[0] + sides[2] >= sides[1])

def equilateral(sides):
    return (sides.count(sides[0]) == 3) and is_valid_triangle(sides)


def isosceles(sides):
    return (sides.count(sides[0]) >= 2 or sides.count(sides[1]) >= 2) and is_valid_triangle(sides)


def scalene(sides):
    return (len(set(sides)) == 3) and is_valid_triangle(sides)