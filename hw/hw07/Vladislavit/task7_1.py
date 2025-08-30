def find_largest(a, b):
    if a > b:
        return a
    else:
        return b


import math

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_circle_area(radius):
    return math.pi * radius ** 2


def count_characters(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def main():
    print("=== Task 1: Find Largest Number ===")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    largest = find_largest(num1, num2)
    print(f"The largest number is: {largest}\n")
    
    print("=== Task 2: Area Calculator ===")
    print("Choose a shape:")
    print("1. Rectangle")
    print("2. Triangle") 
    print("3. Circle")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = calculate_rectangle_area(length, width)
        print(f"Area of rectangle: {area}")
        
    elif choice == "2":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = calculate_triangle_area(base, height)
        print(f"Area of triangle: {area}")
        
    elif choice == "3":
        radius = float(input("Enter radius: "))
        area = calculate_circle_area(radius)
        print(f"Area of circle: {area}")
        
    else:
        print("Invalid choice!")
    
    print("\n=== Task 3: Character Counter ===")
    test_string = "hello"
    result = count_characters(test_string)
    print(f"Input: \"{test_string}\"")
    print(f"Output: {result}")

    user_string = input("\nEnter your own string to count characters: ")
    user_result = count_characters(user_string)
    print(f"Character count for \"{user_string}\": {user_result}")


if __name__ == "__main__":
    main()