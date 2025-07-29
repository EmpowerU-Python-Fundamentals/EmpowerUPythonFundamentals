import area_calculation as area

shape = input("Input a shape to calculate the area (support only rectangle, triangle and circle): \n").lower()
if shape=="rectangle":
    length = float(input("Input the length of the rectangle: \n" ))
    width = float(input("Input the width of the rectangle: \n" ))
    area_value = area.calculate_rectangle_area(length, width)
    print(f"The area of the rectangle is: {area_value}")
elif shape=="triangle":
    height = float(input("Input the height of the triangle: \n" ))
    base = float(input("Input the base of the triangle: \n" ))    
    area_value = area.calculate_triangle_area(height, base)
    print(f"The area of the triangle is: {area_value}")
elif shape=="circle":
    radius = float(input("Input the radius of the circle: \n" ))
    area_value= area.calculate_circle_area(radius)
    print(f"The area of the circle is: {area_value}")
else:
    print(f"{shape} shape is unsupported by our program")