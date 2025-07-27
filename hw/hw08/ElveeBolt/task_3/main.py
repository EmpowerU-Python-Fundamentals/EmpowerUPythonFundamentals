from area import rectangle_area, circle_area, triangle_area

def main():
    print("Choose shape to calculate area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        print("Area:", rectangle_area(a, b))

    elif choice == "2":
        h = float(input("Enter height h: "))
        a = float(input("Enter base a: "))
        print("Area:", triangle_area(h, a))

    elif choice == "3":
        r = float(input("Enter radius r: "))
        print("Area:", circle_area(r))

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()