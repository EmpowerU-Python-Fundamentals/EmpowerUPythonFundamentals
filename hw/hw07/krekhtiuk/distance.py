import math
def distance(x1, y1, x2, y2):
    d= math.sqrt((x2 - x1)**2 + (y2-y1)**2)
    return round(d,2)
print(distance(10,20,30,40))