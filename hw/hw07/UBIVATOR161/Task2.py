
import math
def rectangle(w,l):
    s = w*l
    return s
def triangle(a,b):
    s = 1/2 * a * b
    return s
def circle(r):
    s = math.pi * (r**2)
    return s
print('Choose a shape:')
print('1. Rectangle')
print('2. Triangle')
print('3. Circle')

c = input('Enter: 1/2/3 ')
if c =='1':
    w = float(input('Enter width: '))
    l = float(input('Enter lenght: '))
    s = rectangle(w,l)
    print(f'Regtangle area = {s}')
elif c == "2":
    a = float(input("Enter base: "))
    b = float(input('Enter height: '))
    s = triangle(a,b)
    print(f'Triangle area = {s}')
elif c == '3':
    r = float(input('Enter radius: '))
    s = circle(r)
    print(f'Circle radius = {s}')