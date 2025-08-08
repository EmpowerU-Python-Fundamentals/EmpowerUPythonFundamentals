# Import the area calculation functions from the area_calculator module
from area_calculator import (
    calculate_rectangle_area,
    calculate_triangle_area,
    calculate_circle_area,
)


def main():
    """
    Main function to interact with the user and calculate areas.
    """
    print("Welcome to the Area Calculator!")

    while True:
        print("\nWhich figure's area do you want to calculate?")
        print("1. Rectangle")
        print("2. Triangle")
        print("3. Circle")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            try:
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                area = calculate_rectangle_area(length, width)
                if area is not None:
                    print(f"The area of the rectangle is: {area:.2f}")
            except ValueError:
                print("Invalid input. Please enter numbers for length and width.")
        elif choice == "2":
            try:
                base = float(input("Enter the base of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                area = calculate_triangle_area(base, height)
                if area is not None:
                    print(f"The area of the triangle is: {area:.2f}")
            except ValueError:
                print("Invalid input. Please enter numbers for base and height.")
        elif choice == "3":
            try:
                radius = float(input("Enter the radius of the circle: "))
                area = calculate_circle_area(radius)
                if area is not None:
                    print(f"The area of the circle is: {area:.2f}")
            except ValueError:
                print("Invalid input. Please enter a number for the radius.")
        elif choice == "4":
            print("Exiting the Area Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
