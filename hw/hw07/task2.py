import math
def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * radius ** 2

def user_area():
    while True:
        print("\nChoose shape to calculate area:")
        print("1. Rectangle")
        print("2. Triangle")
        print("3. Circle\n")
        
        choice = input("Enter 1, 2, or 3: ").strip()
        print()
        
        if choice not in {'1', '2', '3'}:
            print("\n>>>>>>>>>>>       Invalid choice        >>>>>>>>>>>>\n>>>>>>>>>>>   Please enter 1, 2, or 3   >>>>>>>>>>>>\n")
            continue  
        try:
            if choice == '1':
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                print(f"\nRectangle area: {rectangle_area(length, width)}\n")
            elif choice == '2':
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                print(f"\nTriangle area: {triangle_area(base, height)}\n")
            elif choice == '3':
                radius = float(input("Enter radius: "))
                print(f"\nCircle area: {circle_area(radius)}\n")
            break
        except ValueError:
            print("\n>>>>>>>>>>>       Invalid number input       >>>>>>>>>>>>\n>>>>>>>>>>>   Please enter numeric values    >>>>>>>>>>>>\n")
if __name__ == "__main__":
    user_area()