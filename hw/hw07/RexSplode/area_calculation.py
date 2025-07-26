#!/usr/bin/env python3
import re as regex

def calc_circle_area(radius: float) -> float:
    PI = 3.14
    return PI * radius ** 2

def calc_triangle_area(base: float, height: float) -> float:
    return base * height * 0.5

def calc_rectangle_area(side1: float, side2: float) -> float:
    return side1 * side2


def is_not_number(param) -> bool:
    num_format = regex.compile(r'^-?(?:\d+\.\d+|\d+)$')
    isnumber = regex.match(num_format, param)
    return not isnumber


def ask_and_calc_circle_area():
    param = input("Enter circle radius\n")
    if is_not_number(param):
        print("This is not a number.")
    else:
        radius = float(param)
        print(f"The area of your circle is: {calc_circle_area(radius)}")
    

def ask_and_calc_triangle_area():
    param1 = input("Enter triangle base\n")
    param2 = input("Enter triangle height\n")

    if is_not_number(param1):
        print("The value you entered for base is not a number.")   
    elif is_not_number(param2):
        print("The value you entered for height is not a number")
    else:
        base = float(param1)
        height = float(param2)
        print(f"The area of your triangle is: {calc_triangle_area(base, height)}")

def ask_and_calc_rectangle_area():
    param1 = input("Enter the first side\n")
    param2 = input("Enter the second side\n")

    if is_not_number(param1):
        print("The value you entered for the first side is not a number.")   
    elif is_not_number(param2):
        print("The value you entered for the second side is not a number")
    else:
        side1 = float(param1)
        side2 = float(param2)
        print(f"The area of your triangle is: {calc_rectangle_area(side1, side2)}")





figure_name = input("Enter the figure name you want to calculate area for." \
" Variants: Circle, Triangle, Rectangle\n").lower()
match figure_name:
    case "circle":
        ask_and_calc_circle_area()
    case "rectangle":
        ask_and_calc_rectangle_area()
    case "triangle":
        ask_and_calc_triangle_area()
    case _:
        print("Unsupported figure type")

        


