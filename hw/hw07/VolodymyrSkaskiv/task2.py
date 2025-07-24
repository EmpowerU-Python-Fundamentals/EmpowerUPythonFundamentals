def s_rect(a, b):
    '''return area rectangle'''
    if a <= 0 or b<=0:
        print("Некоректні дані сторона a < = 0 або b < = 0")
    else:
        return a * b


def s1_triangle(a, b, c):
    ''''return area triangle'''
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        print("Некоректні дані/Трикутника з такими сторонами не існує")
    else:
        p = (a + b + c)/2
        res = (p * (p - a) * (p - b) * (p - c))**0.5
        return res


def s2_triangle(a, h):
    ''''return area triangle'''
    return a*h/2


def s_circle(r):
    pi = 3.14
    '''return area circle'''
    if r < 0:
        print("Incorect data r < 0")
    else:
        return pi * r**2

s = "Y"
while s!="n":
    print ("1.Прямокутник\n2.Трикутник\n3.Коло")
    s=input("Обери номер: ")

    if s=="1":
        a=float(input("Ширина: "))
        b=float(input("Висота: "))
        print(f"S =", s_rect(a,b))
    elif s=="2":
        print("1.Три сторони\n2.Основа і висота")
        s1 = input("Обери номер: ")
        if s1 == "1":
            a = float(input("Сторона а: "))
            b = float(input("Сторона b: "))
            c = float(input("Сторона c: "))
            print(f"S_triangle = ",s1_triangle(a, b, c))
        elif s1 == "2":
            a=float(input("Основа: "))
            h=float(input("Висота: "))
            print(f"S =", s2_triangle(a, h))
        else:
            print("Не вірний номер")
    elif s=="3":
        r=float(input("Радіус: "))
        print(f"S =", s_circle(r))
    else:
        print("Не вірний номер")

    print("Потрібно ще обчислювати Yes/No введіть y/n")
    s = input().lower()