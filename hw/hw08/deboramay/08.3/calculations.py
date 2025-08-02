import math

def area_rect(a, b):
    S = a * b
    return print(f"Площа прямокутника: {S}")

def area_tri(a, h):
    S = 0.5 * a * h
    return print(f"Площа трикутнкика: {S}")

def area_circle(r):
    S = math.pi * pow(r, 2)
    return print(f"Площа круга: {S}")

