from calculating_area import areaOfRectangle, areaOfTriangle, areaOfCircle

userChoise = input("Write the number of the shape whose area you want to calculate:\n1. Rectangle\n2. Triangle\n3. Circle\n")

if userChoise == "1":
    a = int(input("Enter the length of the rectangle: "))
    b = int(input("Enter the width of the rectangle: "))

    print(areaOfRectangle(a, b))
elif userChoise == "2":
    a = int(input("Enter the length of the side: "))
    h = int(input("Enter the length of the height drawn to this side: "))

    print(areaOfTriangle(a, h))
elif userChoise == "3":
    r = int(input("Enter the area of the circle: "))

    print(areaOfCircle(r))
else:
    print("The number you entered is incorrect. Please try again.")