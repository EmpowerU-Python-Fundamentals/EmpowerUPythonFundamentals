from models import calculate_triangle, calculate_rectangle, calculate_circle

shape = input("Write the area to be calculated - triangle, rectangle or circle: ")

if shape == "circle":
    radius = float(input("Add the area radius: "))
else:
    height = float(input("Add the area height: "))
    width = float(input("Add the area width: "))

(
    calculate_triangle(height, width)
    if shape == "triangle"
    else (
        calculate_rectangle(width, height)
        if shape == "rectangle"
        else calculate_circle(radius)
    )
)
