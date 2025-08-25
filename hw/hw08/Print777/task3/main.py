from area import rectangle_area, triangle_area, circle_area

def main():
    print("Choose the figure to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        a = float(input("Enter the length (a): "))
        b = float(input("Enter the width (b): "))
        print(f"Rectangle area = {rectangle_area(a, b)}")

    elif choice == "2":
        base = float(input("Enter the base (a): "))
        height = float(input("Enter the height (h): "))
        print(f"Triangle area = {triangle_area(base, height)}")

    elif choice == "3":
        r = float(input("Enter the radius (r): "))
        print(f"Circle area = {circle_area(r)}")

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
