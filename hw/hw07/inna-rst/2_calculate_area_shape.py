import math


def get_area_of_triangle(base, height):
    """
     Calculate the area of a triangle.

    Args:
        base (float): The base of the triangle
        height (float): The height of the triangle

    Returns:
        float: The area of the triangle
    """
    return 0.5 * base * height

def get_area_of_rectangle(width, height):
    """
    Get the area of a rectangle.

    Args:
        width (float): The width of the rectangle
        height (float): The height of the rectangle

    Returns:
        float: The area of the rectangle
    """
    return width * height

def get_area_of_circle(radius):
    """
    Get the area of a circle.

    Args:
        radius (float): The radius of the circle

    Returns:
        float: The area of the circle
    """
    return math.pi * radius ** 2


def get_positive_number(prompt):
    """
    Get a positive number from user input with validation.

    Args:
        prompt (str): The prompt message to display to the user

    Returns:
        float: A positive number entered by the user
    """
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

def main():
    """
    Main program that allows user to choose shape and calculate its area.
    """
    print("=== Area Calculator ===")
    print("Choose a shape to calculate its area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    print("4. Exit")

    while True:
        try:
            choice = input("\nEnter your choice (1-4): ").strip()

            match choice:
                case "1":
                    print("\n--- Rectangle Area ---")
                    width = get_positive_number("Enter the width of the rectangle: ")
                    height = get_positive_number("Enter the height of the rectangle: ")
                    print(f"The area of the rectangle is {get_area_of_rectangle(width, height):.2f}")
                case "2":
                    print("\n--- Triangle Area ---")
                    base = get_positive_number("Enter the base of the triangle: ")
                    height = get_positive_number("Enter the height of the triangle: ")
                    print(f"The area of the triangle is {get_area_of_triangle(base, height):.2f}")
                case "3":
                    print("\n--- Circle Area ---")
                    radius = get_positive_number("Enter the radius: ")
                    print(f"The area of the circle is: {get_area_of_circle(radius):.2f}")
                case "4":
                    print("Thank you for using Area Calculator!")
                    break
                case _:
                    print("Invalid choice. Please enter a number between 1 and 4.")

        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break


if __name__ == "__main__":
    main()