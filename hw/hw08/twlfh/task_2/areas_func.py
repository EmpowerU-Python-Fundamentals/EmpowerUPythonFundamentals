import math

def area_rectangle(l, w):
    """Return the area of a rectangle."""
    return l * w

def area_circle(r):
    """Return the area of a circle."""
    return math.pow(r,2) * math.pi

def area_triangle(b,h):
    """Return the area of a triangle (using the simplest formula)."""
    return b * h / 2


def main_area(l=None, w=None, r=None, b=None,h=None):
    """Calculate area of rectangle, circle, or triangle based on given parameters.
    Parameters:
    length, width -- for rectangle;
    radius -- for circle;
    base, height -- for triangle;
    Returns:
    Area as a float or None if parameters are insufficient."""

    if r is not None:
        return area_circle(r)
    elif b is not None and h is not None:
        return area_triangle(b, h)
    elif l is not None and w is not None:
        return area_rectangle(l,w)