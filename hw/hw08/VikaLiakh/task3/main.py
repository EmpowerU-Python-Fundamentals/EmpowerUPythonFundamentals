from areas import circle_area, triangle_area, rectangle_area

while True:
    
    area_to_calculate = input("Enter area to calculate (circle, rectangle or triangle) or 'exit' to stop: ")

    if area_to_calculate == "circle":
        radius = float(input("Enter radius of circle : "))
        print (f"Area of cirle with radius {radius} = {circle_area (radius)}")
    
    elif area_to_calculate == "rectangle":
        a = float(input("Enter rectangle's length - a: "))   
        b =  float(input("Enter rectangle's width - b: "))  
        print (f"Area of rectangle with length {a} and width {b} = {rectangle_area(a, b)}")
    
    elif area_to_calculate == "triangle":
        a = float(input("Enter lendth of side a: "))
        h = float(input("Enter height of a triangle - h : "))
         
        print (f"Area of triangle with side {a} and heigth {h} = {triangle_area(a,h)} ") 
    
    elif area_to_calculate == "exit":
        print("Goodbye!")
        break 
    else:
        print("I could not recognize your figure. Please check your input aqain")