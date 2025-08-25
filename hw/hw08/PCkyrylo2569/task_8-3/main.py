import module

area_type = input("Enter shape (1 - rectangle, 2 - triangle, 3 - circle): ")

match area_type:
    case "1":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = module.area_of_rectangle(length, width)
        print("Rectangle area:", area)
    case "2":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = module.area_of_triangle(base, height)
        print("Triangle area:", area)
    case "3":
        radius = float(input("Enter radius: "))
        area = module.area_of_circle(radius)
        print("Circle area:", area)
    case _:
        print("Invalid shape")