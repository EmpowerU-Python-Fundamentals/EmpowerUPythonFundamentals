from geometry_areas import area_rectangle, area_triangle, area_circle

def main():
    print("Enter a type of geometry figure, area you want to find:")
    print("rectangle", "triangle", "circle")

    choice = input("Your choice: ").lower()
    if choice == "rectangle":
        a = float(input("Enter the side a: "))
        b = float(input("Enter the side b: "))
        print("Area of a rectangle:", area_rectangle(a, b))

    elif choice == "triangle":
        a = float(input("Enter the base a: "))
        h = float(input("Enter height h: "))
        print("Area of a triangle:", area_triangle(a, h))

    elif choice == "circle":
        r = float(input("Enter radius r: "))
        print("Area of a circle:", area_circle(r))

    else:
        print("Wrong choice.")

if __name__ == "__main__":
    main()