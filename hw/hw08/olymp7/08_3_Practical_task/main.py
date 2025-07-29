import area

def main():
    print("Choose a shape:", "1 - Rectangle", "2 - Triangle", "3 - Circle")

    shape = input("Enter number of shape: ")

    if shape == "1":
        type_of_shape = "rectangle"
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        result = area.rect_area(length, width)

    elif shape == "2":
        type_of_shape = "triangle"
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        result = area.triangle_area(base, height)

    elif shape == "3":
        type_of_shape = "circle"
        radius = float(input("Enter radius: "))
        result = round(area.circle_area(radius), 2)

    else:
        print("Incorrect number of shape!!!")
        return

    print(f"The area of {type_of_shape} is {result}")

if __name__ == "__main__":
    main()