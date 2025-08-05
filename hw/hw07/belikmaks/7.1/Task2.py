from math import pi

def rectangle_area(a, b):
    return a * b

def triangle_area(base, height):
    return  0.5 * base * height

def circle_area(r):
    return pi * r**2




choice = input("Choose the object: rectangle, triangle or circle: ")

if choice == 'rectangle':
    print(f"Rectangle area:{rectangle_area(1, 2)}")
elif choice == 'triangle':
    print(f"Triangle area: {triangle_area(3, 5.6)}")
elif choice == 'circle':
    print(f"Circle area: {circle_area(4)}")
else:
    print("Invalid input")