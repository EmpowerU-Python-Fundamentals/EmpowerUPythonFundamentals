def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    import math
    return math.pi * radius ** 2

choice = input("Choose shape (rectangle, triangle, circle): ").lower()

if choice == "rectangle":
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area:", rectangle_area(l, w))
elif choice == "triangle":
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Area:", triangle_area(b, h))
elif choice == "circle":
    r = float(input("Enter radius: "))
    print("Area:", circle_area(r))
else:
    print("Invalid choice.")