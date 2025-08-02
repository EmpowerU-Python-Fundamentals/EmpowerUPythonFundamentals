import math

def rectangle_area(length, width):
    #Calculates area of a rectangle
    return length * width

def triangle_area(base, height):
    #Calculates area of a triangle
    return 0.5 * base * height

def circle_area(radius):
    #Calculates area of a circle
    return math.pi * radius ** 2

def main():
    print("Area Calculator")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print(f"Area of rectangle: {rectangle_area(length, width)}")
    elif choice == '2':
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print(f"Area of triangle: {triangle_area(base, height)}")
    elif choice == '3':
        radius = float(input("Enter radius: "))
        print(f"Area of circle: {circle_area(radius)}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
