def rect_area(length, width):
    area = length*width
    return area


def triangle_area(base, height):
    area = 0.5*base*height
    return area


def circle_area(radius):
    area = 3.14*(radius**2)
    return area


def main():
    print("Choose a shape:", "1 - Rectangle", "2 - Triangle", "3 - Circle")

    shape = input("Enter number of shape: ")

    if shape == "1":
        type_of_shape = "rectangle"
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        result = rect_area(length, width)

    elif shape == "2":
        type_of_shape = "triangle"
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        result = triangle_area(base, height)

    elif shape == "3":
        type_of_shape = "circle"
        radius = float(input("Enter radius: "))
        result = circle_area(radius)

    else:
        print("Incorrect number of shape!!!")
        return

    print(f"The area of {type_of_shape} is {result}")

if __name__ == "__main__":
    main()