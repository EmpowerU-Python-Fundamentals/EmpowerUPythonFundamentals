#Task1

# def lar_num(a, b):
#     """This function returns the largest number of two numbers"""
#     largest = 0
#     if a > b:
#         largest = a
#     elif b > a:
#         largest = b
#     return largest

#Task2

# def rectangle(a, b):
#     area = a*b
#     return area
#
#
# def triangle(a, b, c):
#     sp = (a+b+c)/2
#     area = (sp*(sp-a)*(sp-b)*(sp-c))**0.5
#     return area
#
#
# def circle(a):
#     area = a**2*3.14
#     return area
#
#
# figure = input("Area of which figure do you want to calculate? \nWrite rectangle, triangle or circle\n")
#
# if figure == "rectangle":
#     a = int(input("Lenght = "))
#     b = int(input("Width = "))
#     print(rectangle(a, b))
#
# elif figure == "triangle":
#     a = int(input("Sides:\na = "))
#     b = int(input("b = "))
#     c = int(input("c = "))
#     print(triangle(a, b, c))
#
# elif figure == "circle":
#     a = int(input("radius = "))
#     print(circle(a))
#
# else:
#     print("Invalid figure")


#Task3

# def num(string):
#     dict = {}
#     for letter in string:
#         dict[letter] = string.count(letter)
#     return dict
#
# word = input("Your string: ")
# print(num(word))