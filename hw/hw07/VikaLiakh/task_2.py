#TASK2
from math import sqrt, pi

def rectangle_area(length, width):
    '''This function calculates area of rectangle'''
    return round((length * width),1)

def triangle_area(side1, side2, side3):
    '''This function calculates area of triangle using Heron’s formula'''
    s = (side1 + side2 + side3) / 2 # calculation of semi-perimeter
    area = sqrt(s * (s - side1) * (s - side2) * (s - side3)) #Heron’s formula
    return round(area,1)

def circle_area (radius):
    '''This function calculates area of circle'''
    return round((pi * radius**2),1)
while True:
    
    area_to_calculate = input("Enter area to calculate (circle, rectangle or triangle) or 'exit' to stop: ")

    if area_to_calculate == "circle":
        radius = float(input("Enter radius of circle : "))
        print (f"Area of cirle with radius {radius} = {circle_area (radius)}")
    
    elif area_to_calculate == "rectangle":
        length = float(input("Enter rectangle's length: "))   
        width =  float(input("Enter rectangle's width: "))  
        print (f"Area of rectangle with length {length} and width {width} = {rectangle_area(length, width)}")
    
    elif area_to_calculate == "triangle":
        side1 = float(input("Enter lendth of side 1: "))
        side2 = float(input("Enter lendth of side 2: "))
        side3 = float(input("Enter lendth of side 3: "))  
        print (f"Are of triangle with sides {side1}, {side2}, {side3} = {triangle_area(side1,side2,side3)} ") 
    
    elif area_to_calculate == "exit":
        print("Goodbye!")
        break 
    else:
        print("I could not recognize your figure. Please check your input aqain")