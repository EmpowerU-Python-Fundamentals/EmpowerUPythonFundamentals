
def circle(R):
        S = 3.1415*R**2
        print(f"Area of circle is ", S)

def rectangle(d,h):
        S = d * h
        print(f"Area of rectangle is ", S)

def triangle(h,b):
        S = (h*b)/2
        print(f"Area of triangle is ", S)




a = input("enter the name of the shape ")

if a == "circle":
    R =float(input("Enter please radius "))
    
    S =circle(R)
elif a == "rectangle":
    d = float(input("Enter please width "))
    h = (input("Enter please height "))
    
    S=rectangle(d,h)
elif a == "triangle":
    h = float(input("Enter please height "))
    b = float(input("Enter the length of the side to which the perpendicular height is perpendicular "))
    S=circle(h,b)
else:
    print("Unknown shape")
        
        