import math

def rectangle_area(length, width):
    """Calculate area of a rectangle."""
    return length * width

def triangle_area(base, height):
    """Calculate area of a triangle."""
    return 0.5 * base * height

def circle_area(radius):
    """Calculate area of a circle."""
    return math.pi * radius ** 2

def main():
    print("Choose shape: rectangle / triangle / circle")
    choice = input("Your choice: ").strip().lower()

    if choice == "rectangle":
        l = float(input("Length: "))
        w = float(input("Width: "))
        print("Area:", rectangle_area(l, w))
    elif choice == "triangle":
        b = float(input("Base: "))
        h = float(input("Height: "))
        print("Area:", triangle_area(b, h))
    elif choice == "circle":
        r = float(input("Radius: "))
        print("Area:", circle_area(r))
    else:
        print("Unknown shape")

if __name__ == "__main__":
    main()