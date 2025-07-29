def get_rectangle_area(length: float, width: float) -> float:
    """
    Calculates the area of a rectangle.
    """
    return length * width


def get_triangle_area(base: float, height: float) -> float:
    """
    Calculates the area of a triangle.
    """
    return 0.5 * base * height


def get_circle_area(radius: float) -> float:
    """
    Calculates the area of a circle.
    """
    return 3.14 * radius ** 2


def main():
    print("Choose a shape to calculate its area:", "1 - Rectangle", "2 - Triangle", "3 - Circle", sep="\n")

    choice = input("Enter the number (1/2/3): ")

    if choice == '1':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = get_rectangle_area(length, width)

    elif choice == '2':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = get_triangle_area(base, height)

    elif choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        area = get_circle_area(radius)

    else:
        print("Invalid choice.")
        return

    print(f"The area of the selected shape is: {round(area, 2)}")


# Run the main program
if __name__ == "__main__":
    main()
