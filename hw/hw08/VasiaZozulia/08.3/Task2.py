import figures_area as fa

print("\t\tAttantion! Only positive integers are allowed!")
choice = int(input("Which shape's area do you want to calculate?\n(1 - Rectangle, 2 - Triangle, 3 - Cirle): "))

match choice:
    case 1:
        print("Rectangle")
        width = int(input("What is the width of the rectangle? "))
        length = int(input("What is the length of the rectangle? "))
        print(f"The area of the rectangle with sides ({width}, {length})  is {fa.area_rectangle(width, length)}")
    case 2:
        print("Triangle")
        first_side = int(input("What is the first side of the triangle? "))
        print("Additional parameters!")
        height = int(input("What is the perpendicular distance from the third side to the opposite vertex? "))
        print("The area of the triangle is")
        print(f"The first side and the height {fa.area_triangle_side_height(first_side, height)}")
    case 3:
        print("Circle")
        radius = int(input("What is the radius of the cirle? "))
        print(f"The area of the cirlce is {fa.area_circle(radius)}")
    case _:
        print("Exit. Only 1, 2, 3 are allowed!")