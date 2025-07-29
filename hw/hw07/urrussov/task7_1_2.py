def area_of_rectangle(length, width):
    """This function calculate and return area of rectangle"""

    return length * width


def area_of_triangle(base, height):
    """This function calculate and return area of triangle"""

    return (base * height) / 2


def area_of_circle(radius):
    """This function calculate and return area of circle"""

    return 3.14 * (radius**2)


fig = input(
    "Write the area of which shape you want to calculate? (RECTANGLE, TRIANGLE, CIRCLE): "
)


if fig.upper() == "RECTANGLE":
    l = float(input("Enter a length of rectangle in cm: "))
    w = float(input("Enter a width of rectangle in cm: "))
    result = area_of_rectangle(l, w)
    print(f"The area of rectangle is {result} cm^2")
elif fig.upper() == "TRIANGLE":
    b = float(input("Enter a base of triangle in cm: "))
    h = float(input("Enter a height of triangle in cm: "))
    result = area_of_triangle(b, h)
    print(f"The area of triangle is {result} cm^2")
elif fig.upper() == "CIRCLE":
    r = float(input("Enter a radius of circle in cm: "))
    result = area_of_circle(r)
    print(f"The area of circle is {result} cm^2")
else:
    print("You didn't enter right shape. Try again!")
