def area_rectangle():
    """Calculates the area of a rectangle"""
    print("Area of rectangle = length * width.")
    
    while True:
        a_input = input("Enter length: ")
        b_input = input("Enter width: ")

        if a_input.replace('.', '', 1).isdigit() and b_input.replace('.', '', 1).isdigit():
            a = float(a_input)
            b = float(b_input)
            area = a * b
            print(f"The area of rectangle = {area}")
            break
        else:
            print("Error, please enter a number.")
            
def area_triangle():
    """Calculates the area of a triangle"""
    print("Area of triangle = 0,5 * a * h")
    while True:
        a_input = input("Enter base: ")
        h_input = input("Enter height: ")
        
        if a_input.replace('.', '', 1).isdigit() and h_input.replace('.', '', 1).isdigit():
            a = float(a_input)
            h = float(h_input)
            area = 0.5 * a * h
            print(f"The area of triangle = {area}")
            break
        else:
            print("Error, please enter a number.")
                   
def area_circle():
    """Calculates the area of a circle"""
    print("Area of circle = pi * r ** 2")
    while True:
        pi = 3.14
        r_input = input("Enter radius: ")
        
        if r_input.replace('.', '', 1).isdigit():
            r = float(r_input)
            area = pi * r ** 2
            print(f"The area of circle = {area}")
            break
        else:
            print("Error, please enter a number.")
                  
print("="*74)
print("Let's calculate an area of geometric figure: rectangle, triangle or circle")
print("="*74)

while True:
    user_input = input("Enter a type of geometry figure area you want to find.").lower()
    if user_input == "rectangle":
        area_rectangle()
    elif user_input == "triangle":
        area_triangle()
    elif user_input == "circle":
        area_circle()
        break
    else:
        print("Error please enter rectangle, triangle or circle")
        