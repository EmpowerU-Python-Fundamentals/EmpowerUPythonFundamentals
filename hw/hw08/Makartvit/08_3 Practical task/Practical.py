from math import pi, pow  # use the real π and pow()


def area_rectangle(width, height):
    return width * height


def area_triangle(base, height):
    return 0.5 * base * height


def area_circle(radius):
    return pi * pow(radius, 2)
