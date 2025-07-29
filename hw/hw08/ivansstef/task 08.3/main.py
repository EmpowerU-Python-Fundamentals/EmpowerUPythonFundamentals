from calculate import *

def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")

print("Choose a shape to calculate area:")
print("1 - Rectangle")
print("2 - Triangle")
print("3 - Circle")

choice = input("Your choice (1/2/3): ")

if choice == "1":
    a = read_float("Enter side a: ")
    b = read_float("Enter side b: ")
    result = area_rectangle(a, b)
    print("Area of rectangle:", round(result, 2))

elif choice == "2":
    a = read_float("Enter base a: ")
    h = read_float("Enter height h: ")
    result = area_triangle(a, h)
    print("Area of triangle:", round(result, 2))

elif choice == "3":
    r = read_float("Enter radius r: ")
    result = area_circle(r)
    print("Area of circle:", round(result, 2))

else:
    print("Invalid choice. Please try again.")
