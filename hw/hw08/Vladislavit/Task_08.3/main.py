from math import pi, pow
import areas

def main():
    """Main program that asks user which figure area to calculate"""
    print("Area Calculator")
    print("Choose which figure's area you want to calculate:")
    print("1 - Rectangle")
    print("2 - Triangle") 
    print("3 - Circle")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        # Rectangle area calculation
        print("\nRectangle area calculation (S = a * b)")
        a = float(input("Enter length (a): "))
        b = float(input("Enter width (b): "))
        area = areas.rectangle_area(a, b)
        print(f"Area of rectangle: {area}")
        
    elif choice == '2':
        # Triangle area calculation  
        print("\nTriangle area calculation (S = 0.5 * h * a)")
        h = float(input("Enter height (h): "))
        a = float(input("Enter base (a): "))
        area = areas.triangle_area(h, a)
        print(f"Area of triangle: {area}")
        
    elif choice == '3':
        # Circle area calculation
        print("\nCircle area calculation (S = π * r²)")
        r = float(input("Enter radius (r): "))
        area = areas.circle_area(r)
        print(f"Area of circle: {area}")
        
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()