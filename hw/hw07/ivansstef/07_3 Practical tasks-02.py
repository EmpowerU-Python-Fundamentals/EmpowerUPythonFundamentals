# Code written by Ivan Savytsky
# Code reviewed for PEP 8 compliance by ChatGPT

import math

def distance(x1, y1, x2, y2):
    """Return the distance between two points rounded to 2 decimals."""
    try:
        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
    except ValueError:
        return "All coordinates must be numbers."

    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(dist, 2)

def main():
    print(distance(1, 2, 4, 6))        # 5.0
    print(distance(1, 1, 0, 0))        # 1.41
    print(distance("a", 2, 3, 4))      # Error

if __name__ == "__main__":
    main()
