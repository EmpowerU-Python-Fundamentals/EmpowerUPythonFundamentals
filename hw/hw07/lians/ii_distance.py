# Find the distance between points (x1, y1) and (x2, y2)

import math

def distance(x1, y1, x2, y2):
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return round(d, 2)