from module import rectangle_area, triangle_area, circle_area

print("Choose figure: 1-rectangle, 2-triangle, 3-circle")
choice = input("Your choice: ")

if choice == "1":
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    print("Area of rectangle:", rectangle_area(a, b))

elif choice == "2":
    a = float(input("Enter base a: "))
    h = float(input("Enter height h: "))
    print("Area of triangle:", triangle_area(a, h))

elif choice == "3":
    r = float(input("Enter radius r: "))
    print("Area of circle:", circle_area(r))

else:
    print("Wrong choice!")
