from shapes import rectangle_area, triangle_area, circle_area

choice_user = input("Which area do you want to calculate? (rectangle/triangle/circle): ").strip().lower()

if choice_user == "rectangle":
    a = float(input("Enter length (a): "))
    b = float(input("Enter width (b): "))
    print("Area of rectangle:", rectangle_area(a, b))

elif choice_user == "triangle":
    a = float(input("Enter base a: "))
    h = float(input("Enter height h: "))
    print("Area of triangle:", triangle_area(a, h))

elif choice_user == "circle":
    r = float(input("Enter radius r: "))
    print("Area of circle:", circle_area(r))

else:
    print("Unknown figure")
