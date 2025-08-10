from areas import rectangle_area, triangle_area, circle_area

# Show menu to the user
print("Choose a shape to calculate the area:")
print("1 - Rectangle")
print("2 - Triangle")
print("3 - Circle")

choice = input("Your choice (1/2/3): ")
# Match user choice and call corresponding function
match choice:
    case "1":
        # Rectangle area
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        print("Rectangle area:", rectangle_area(length, width))

    case "2":
        # Triangle area
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        print("Triangle area:", triangle_area(base, height))

    case "3":
        # Circle area
        radius = float(input("Enter the radius: "))
        print("Circle area:", circle_area(radius))

    case _:
        # Invalid choice
        print("Invalid choice!")