import math

def area_rectangle(a, b):
    return a * b

def area_triangle(a, b):
    return 0.5 * a * b

def area_circle(r):
    return math.pi * r ** 2

def calc():
    print("Choose shape to calculate area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Enter the choice (1/2/3): ")

    if choice == "1":
        a = float(input("Enter width: "))
        b = float(input("Enter height: "))
        print("Area of rectangle:", area_rectangle(a, b))

    elif choice == "2":
        a = float(input("Enter base: "))
        b = float(input("Enter height: "))
        print("Area of triangle:", area_triangle(a, b))

    elif choice == "3":
        r = float(input("Enter radius: "))
        print("Area of circle:", area_circle(r))

    else:
        print("Invalid choice")

calc()