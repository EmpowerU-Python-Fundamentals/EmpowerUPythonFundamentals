import math

def area_rectangle(length, width):
    """Calculate area of a rectangle."""
    return round(length * width)

def area_triangle(base, height):
    """Calculate area of a triangle."""
    return round(0.5 * base * height)

def area_circle(radius):
    """Calculate area of a circle."""
    return round(math.pi * radius ** 2, 2)

# Main program
def main():
    choice = input("Choose shape (rectangle, triangle, circle): ").lower()

    if choice == "rectangle":
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print("Area of rectangle:", area_rectangle(l, w))

    elif choice == "triangle":
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print("Area of triangle:", area_triangle(b, h))

    elif choice == "circle":
        r = float(input("Enter radius: "))
        print("Area of circle:", area_circle(r))

    else:
        print("Invalid shape selected.")

if __name__ == "__main__":
    main()
