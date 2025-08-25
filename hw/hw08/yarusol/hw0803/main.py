from area_calculators import calculate_circle_area
from area_calculators import calculate_rectangle_area
from area_calculators import calculate_triangle_area

def ask_rectangle():
    """Asks characteristics of a rectangle and calculates it's area."""
    height = float(input("Enter the height of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    return calculate_rectangle_area(height, width)

def ask_triangle():
    """Asks characteristics of a triangle and calculates it's area."""
    height = float(input("Enter the height of the triangle: "))
    base = float(input("Enter the base of the triangle: "))
    return calculate_triangle_area(height, base)

def ask_circle():
    """Asks rarius of a circle and calculates it's area."""
    radius = float(input("Enter the radius of the circle: "))
    return calculate_circle_area(radius)


options = {
    "1": ("rectangle", ask_rectangle),
    "2": ("triangle", ask_triangle),
    "3": ("circle", ask_circle)
    }


print("")
print("Available figure types to calculate the area:")
for key, option in options.items():
    print(f"{key} - {option[0]}")

keys = options.keys()
choice = input("Enter your choice: ")
if choice not in keys:
    print(f"Invalid choice. Next time enter one of the following: {", ".join(keys)}")
    print()
    exit()

chosen = options.get(choice)
chosen_figure = chosen[0]
chosen_function = chosen[1]
print(f"The area of the {chosen_figure} is: {chosen_function}")
print()