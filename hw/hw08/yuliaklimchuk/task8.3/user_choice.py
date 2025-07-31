from calculation_areas import calculating_area_circle, calculating_area_rectangle, calculating_area_triangle

figure = input("Which shape do you want to calculate the area of (rectangle, triangle, or circle)?    ")

match (figure.lower().strip()):
    case "rectangle":
        a = int(input("Enter the length of side a: "))
        b = int(input("Enter the length of side b: "))
        print(f"Area of a rectangle = {calculating_area_rectangle(a,b)}")
    case "triangle":
        a = int(input("Enter the length of side: "))
        h = int(input("Enter the height: "))
        print(f"Area of a triangle = {calculating_area_triangle(h,a)}")
    case "circle":
        r = int(input("Enter the radius of the circle "))
        print(f"Area of a circle = {calculating_area_circle(r)}")
    case _:
        print("Invalid input")