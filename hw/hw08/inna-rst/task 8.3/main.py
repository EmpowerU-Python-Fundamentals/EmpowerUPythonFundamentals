from m_area import *

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

def print_area(shape, area):
    print(f"The area of the {shape} is {area:.2f}")

def main():
    """
    Main program that allows user to choose shape and calculate its area.
    """
    name_shapes= {1: "rectangle", 2: "triangle", 3: "circle"}

    print("=== Area Calculator ===")
    print("Choose a shape to calculate its area:")
    for key, value in name_shapes.items():
        print(f"{key}. {value.capitalize()}")
    print("4. Exit")

    while True:
        try:
            choice = input("\nEnter your choice (1-4): ").strip()

            match choice:
                case "1":
                    print("\n--- Rectangle Area ---")
                    width = get_positive_number("Enter the width of the rectangle: ")
                    height = get_positive_number("Enter the height of the rectangle: ")
                    print_area(name_shapes[int(choice)], get_area_rectangle(width, height))
                case "2":
                    print("\n--- Triangle Area ---")
                    base = get_positive_number("Enter the base of the triangle: ")
                    height = get_positive_number("Enter the height of the triangle: ")
                    print_area(name_shapes[int(choice)], get_area_triangle(base, height))
                case "3":
                    print("\n--- Circle Area ---")
                    radius = get_positive_number("Enter the radius: ")
                    print_area(name_shapes[int(choice)], get_area_circle(radius))
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