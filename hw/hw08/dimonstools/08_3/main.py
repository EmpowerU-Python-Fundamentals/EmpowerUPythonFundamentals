import calculate

def main():
    print("Choose a shape to calculate the area:")
    print("1 - Rectangle")
    print("2 - Triangle")
    print("3 - Circle")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        a = float(input("Enter the length: "))
        b = float(input("Enter the width: "))
        print("Area of rectangle:", calculate.area_rectangle(a, b))
    
    elif choice == "2":
        a = float(input("Enter the base: "))
        h = float(input("Enter the height: "))
        print("Area of triangle:", calculate.area_triangle(a, h))

    elif choice == "3":
        r = float(input("Enter the radius: "))
        print("Area of circle:", calculate.area_circle(r))
    
    else:
        print("Invalid choice.")

# Run main function
if __name__ == "__main__":
    main()