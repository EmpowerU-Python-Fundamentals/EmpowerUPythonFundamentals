# Task 1. Write a function that returns the largest number of two numbers
# (use DocStrings documentation strings in the function).

def max_of_two_numbers(a, b):
    """
    Returns the larger of two numbers.
    """
    return a if a > b else b

a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
print("The larger number is:", max_of_two_numbers(a, b))


# Task 2. Write a program that calculates the area of a rectangle, triangle and circle
# (write three functions to calculate the area. And call them in the main program 
# depending on the user's choice).

import math 

def area_rectangle(length, width):
    """
    Calculates the area of a rectangle.
    """
    return length * width

def area_triangle(base, height):
    """
    Calculates the area of a triangle.
    """
    return 0.5 * base * height

def area_circle(radius):
    """
    Calculates the area of a circle.
    """
    return math.pi * radius ** 2

def main():
    print("Choose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    choice = input("Your choice (1/2/3): ")

    if choice == "1":
        length = float(input("Length: "))
        width = float(input("Width: "))
        print("Area of the rectangle:", area_rectangle(length, width))

    elif choice == "2":
        base = float(input("Base length: "))
        height = float(input("Height: "))
        print("Area of the triangle:", area_triangle(base, height))

    elif choice == "3":
        radius = float(input("Radius: "))
        print("Area of the circle:", area_circle(radius))

    else:
        print("Invalid choice.")
main()

# Task 3. Write a function that calculates the number of characters included in a given string
# input: "hello" 
# output: {"h":1, "e":1, "l":2, "o":1}

from collections import Counter

def char_frequency(s):
    """
    Counts the occurrences of each character in a string using Counter.
    """
    return dict(Counter(s))

text = input("Enter a string: ")
result = char_frequency(text)
print("Character frequency:", result)
main()


