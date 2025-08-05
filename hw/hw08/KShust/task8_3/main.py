import task8_3

choice = input("Enter your choice ( 1.Rectangle, 2.Triangle, 3.Circle )")
if choice == "1":
    a = int(input("Enter length: "))
    b = int(input("Enter width: "))
    area = task8_3.a_rec(a, b)
    print(f"Area of rectangle: {area}")
elif choice == "2":
    m = int(input("Enter the base: "))
    h = int(input("Enter height: "))
    area = task8_3.a_tri(m, h)
    print(f"Area of triangle: {area}")
elif choice == "3":
    r = int(input("Enter the radius: "))
    area = task8_3.a_cir(r)
    print(f"Area of circle: {area}")
else:
    print("Invalid choice.")