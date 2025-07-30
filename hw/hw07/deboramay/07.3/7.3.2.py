import math
def distance(x1, y1, x2, y2):
    """
    Calculates the distance between two points
    """
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)


#Test:
print(distance(1, 1, 2, 2))