from math import pi, pow

def rectangle(a, b):
    """Gives area of a rectangle with both sides given."""
    area = a * b
    return f"Area of the rectangle with the sides {a = }, {b = } is equal to {area:.2f}."


def triangle(h, b):
    """Gives area of a triangle with three sides given."""
    area = 0.5 * h * b
    return f"Area of the triangle with the altitude {h = } and the base {b = } is equal to {area:.2f}."


def circle(r):
    """Gives area of a circle with radius given."""
    area =  pi * pow(r, 2)
    return f"Area of the circle with the radius {r = } is equal to {area:.2f}."
