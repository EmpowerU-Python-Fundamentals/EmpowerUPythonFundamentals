
from .areas import rectangle_area, triangle_area, circle_area

def main():
    print("1. Rectangle\n2. Triangle\n3. Circle")
    choice = input("Select figure (1-3): ")
    
    if choice == "1":
        a = float(input("Enter width: "))
        b = float(input("Enter length: "))
        print("Area:", rectangle_area(a, b))
    elif choice == "2":
        h = float(input("Enter height: "))
        a = float(input("Enter base: "))
        print("Area:", triangle_area(h, a))
    elif choice == "3":
        r = float(input("Enter radius: "))
        print("Area:", circle_area(r))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
