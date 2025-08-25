import area_task3

choice = input("Enter your choice (rectangle, triangle, circle)")
if choice == "rectangle":
        a = int(input("Enter length: "))
        b = int(input("Enter width: "))
        area = area_task3.area_rectangle(a, b)
        print(f"Area of rectangle: {area}")
elif choice == "triangle":
        m = int(input("Enter the base: "))
        h = int(input("Enter height: "))
        area = area_task3.area_triangle(m, h)
        print(f"Area of triangle: {area}")
elif choice == "circle":
        r = int(input("Enter the radius: "))
        area = area_task3.area_circle(r)
        print(f"Area of circle: {area}")
else:
        print("Invalid choice.")