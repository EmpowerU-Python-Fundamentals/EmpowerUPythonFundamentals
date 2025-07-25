import math

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * radius ** 2

if __name__ == "__main__":
    choice = input("Оберіть фігуру (1-прямокутник, 2-трикутник, 3-коло):")
    if choice == '1':
        print(rectangle_area(4, 5))
    elif choice == '2':
        print(triangle_area(3, 6))
    elif choice == '3':
        print(circle_area(7))
