def rec(a,b):
    return a*b

def tri(a,h):
    return (a*h)/2

def cir(r):
    pi=3.14
    return pi*r**2

print ("1.Прямокутник\n2.Трикутник\n3.Коло")
s=input("Обери номер: ")

if s=="1":
    a=float(input("Ширина: "))
    b=float(input("Висота: "))
    print(f"S = {rec(a,b)}")
elif s=="2":
    a=float(input("Основа: "))
    h=float(input("Висота: "))
    print(f"S = {tri(a,h)}")
elif s=="3":
    r=float(input("Радіус: "))
    print(f"S = {cir(r)}")
else:
    print("Не вірний номер")
