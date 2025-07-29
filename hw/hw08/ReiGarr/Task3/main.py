import module

choice = input("Enter shape (1 - rectangle, 2 - triangle, 3 - circle): ")

if choice == "1":
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    print("Rectangle area:", module.area_rectangle(a, b))

elif choice == "2":
    h = float(input("Enter height h: "))
    a = float(input("Enter base a: "))
    print("Trianle area:", module.area_triangle(h, a))

elif choice == "3":
    r = float(input("Enter radius r: "))
    print("Circle area:", module.area_circle(r))

else:
    print("Invalid shape")