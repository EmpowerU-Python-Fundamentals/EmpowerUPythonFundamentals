from formules import rectangle, triangle, circle

figure = input("Area of which figure do you want to calculate? \nWrite rectangle, triangle or circle\n")

if figure == "rectangle":
    a = int(input("Lenght = "))
    b = int(input("Width = "))
    print(f"Area of this rectangle: {rectangle(a, b)}")

elif figure == "triangle":
    a = int(input("Base = "))
    h = int(input("Height = "))
    print(f"Area of this triangle: {triangle(a, h)}")

elif figure == "circle":
    r = int(input("Radius = "))
    print(f"Area of this circle: {circle(r)}")

else:
    print("Invalid figure")