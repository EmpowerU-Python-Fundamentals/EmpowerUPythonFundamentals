from area_func import rectangle_area, triangle_area, circle_area

def main():
    print("Choose a shape to calculate area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print("Area of rectangle:", rectangle_area(length, width))

    elif choice == '2':
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print("Area of triangle:", triangle_area(base, height))

    elif choice == '3':
        radius = float(input("Enter radius: "))
        print("Area of circle:", circle_area(radius))

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
