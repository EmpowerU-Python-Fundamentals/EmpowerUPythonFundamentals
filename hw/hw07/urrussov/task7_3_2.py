import math

def distance(x1, y1, x2, y2):
    """Calculate a distance between two points"""
    distans = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(distans, 2)