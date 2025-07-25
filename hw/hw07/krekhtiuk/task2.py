def area_rectangle(a, b):
    return a*b
def area_triangle(m, h):
    return 0.5*m*h
def area_circle(r):
    return 3.14*r**2
def main():
    print("Choose a shape to calculate area.")
    print("rectangle")
    print("triangle")
    print("circle")
    choice = input("Enter your choice (rectangle, triangle, circle)")
    if choice == "rectangle":
        a = int(input("Enter length: "))
        b = int(input("Enter width: "))
        area = area_rectangle(a, b)
        print(f"Area of rectangle: {area}")
    elif choice == "triangle":
        m = int(input("Enter the base: "))
        h = int(input("Enter height: "))
        area = area_triangle(m, h)
        print(f"Area of triangle: {area}")
    elif choice == "circle":
        r = int(input("Enter the radius: "))
        area = area_circle(r)
        print(f"Area of circle: {area}")
    else:
        print("Invalid choice.")
main()