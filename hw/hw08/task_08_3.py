import module08_3

print ("1.Прямокутник\n2.Трикутник\n3.Коло")
s=input("Обери номер: ")

if s=="1":
    a=float(input("Ширина: "))
    b=float(input("Висота: "))
    print(f"S = {module08_3.rec(a,b)}")
elif s=="2":
    a=float(input("Основа: "))
    h=float(input("Висота: "))
    print(f"S = {module08_3.tri(a,h)}")
elif s=="3":
    r=float(input("Радіус: "))
    print(f"S = {round(module08_3.cir(r), 2)}")

else:
    print("Не вірний номер")


