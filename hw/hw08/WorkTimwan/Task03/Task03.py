import math

shape = input("enter name of shape ")


if shape =="circle":
    radius = float(input("enter radious "))
   
    area_circle = math.pi * radius * radius
    print(f"area circle = {area_circle }")
elif shape =="triangle":
    a = float(input("enter side 1 "))
    b = float(input("enter side 2 "))
    c = float(input("enter side 3 "))

    s = (a + b + c) / 2  
    area_triangle = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"area triangle = {area_triangle }")
elif shape =="rectangle":
    length = float(input("enter side 1 "))
    width = float(input("enter side 2 "))
    
    area_rectangle = length * width
    print(f"area rectangle = {area_rectangle }")
else:
    print("Incorect shape")




