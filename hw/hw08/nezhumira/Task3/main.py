import area_calculations as ac

while True:
    print("Choose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print(f"Area of Rectangle = {ac.area_rectangle(length, width):.2f}")
        input("Please press Enter.")
    elif choice == "2":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print(f"Area of Triangle = {ac.area_triangle(base, height):.2f}")
        input("Please press Enter.")
    elif choice == "3":
        radius = float(input("Enter radius: "))
        print(f"Area of Circle = {ac.area_circle(radius):.2f}")
        input("Please press Enter.")
    elif choice == "4":
        break 
    else:
        input("Invalid choice. \nPlease press Enter.") 
