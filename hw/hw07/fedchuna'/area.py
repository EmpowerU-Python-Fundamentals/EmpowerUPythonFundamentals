def circle_area(radius):
    import math
    return math.pi * (radius ** 2)

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

input_choice = input("Choose a shape (circle, rectangle, triangle): ").strip().lower()

while input_choice not in ["circle", "rectangle", "triangle"]:
    print("Invalid choice. Please choose circle, rectangle, or triangle.")
    input_choice = input("Choose a shape (circle, rectangle, triangle): ").strip().lower()
if input_choice == "circle":
    input_radius = float(input("Enter the radius of the circle: "))
    print(f"Area of the circle: {circle_area(input_radius)} m²")

elif input_choice == "rectangle":
    input_length = float(input("Enter the length of the rectangle: "))
    input_width = float(input("Enter the width of the rectangle: "))
    print(f"Area of the rectangle: {rectangle_area(input_length, input_width)} m²")

elif input_choice == "triangle":
    input_base = float(input("Enter the base of the triangle: "))
    input_height = float(input("Enter the height of the triangle: "))
    print(f"Area of the triangle: {triangle_area(input_base, input_height)} m²")
