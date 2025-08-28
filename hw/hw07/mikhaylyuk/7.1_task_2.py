import math

def area_rectangle(a, b):
    """
    Площа прямокутника
    a - ширина прямокутника 
    b - висота прямокутника
    """
    return a * b

def area_triangle(basis, height):
    """
    Площа трикутника
    basis - основа трикутника 
    height - висота трткутника 
    """
    return 0.5 * basis * height

def area_circle(r):
    """
    Площа кола
    r - радіус
    """
    return math.pi * r**2


choice = input("Оберіть фігуру (rectangle, triangle, circle): ") 
if choice == "rectangle":
    print(area_rectangle(4, 5))
elif choice == "triangle":
    print(area_triangle(3, 6))
elif choice == "circle":
    print(area_circle(4))

# rectangle - вивід 20 
# triangle - вивід 9.0
# circle - вивід 50.26548245743669 