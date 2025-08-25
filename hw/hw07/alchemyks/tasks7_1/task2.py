from math import sqrt
from math import pi


def rectangle_area(side_a, side_b):
    return side_a * side_b


def triangle_area(a, b, c):
    half_p = (a + b + c) / 2
    return sqrt(half_p * (half_p - a) * (half_p - b) * (half_p - c))


def circle_area(r):
    return pi * r**2



if __name__ == "__main__":
    choice = input("Calc area for rectangle:1, triangle:2, circle:3.\nTo do choice: ")
    match choice:
        case '1':
            a = int(input("Side a: "))
            b = int(input("Side b: "))
            print(rectangle_area(a, b))
        case '2':
            a = int(input("Side a: "))
            b = int(input("Side b: "))
            c = int(input("Side c: "))
            print(triangle_area(a, b, c))
        case '3':
            r = int(input("Radius: "))
            print(circle_area(r))
        case _:
            print(f'Figure with index {choice} not found')