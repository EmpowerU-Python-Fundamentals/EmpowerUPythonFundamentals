import math
import functions

func=["Площа круга","Площа трикутника","Площа прямокутника"]
num=1

print("Виберіть одну з формул:")
for function in func:
    print(f"Натисніть {num} для {function}")
    num+=1
formula = ""

while formula not in ("1","2","3"):
    print("Введіть 1 або 2 або 3")
    formula=input()

if formula == '1':
    print("Введіть довжини двох сторін через ентер")
    a = int(input())
    b = int(input())
    print(f"Площа прямокутника {a}*{b}:", functions.rectangle_area(a,b))
    
elif formula == '2':
    print("Введіть довджину сторони та висоту через ентер")
    a = int(input())
    h = int(input())
    print(f"Площа трикутника  {a}*{h}*0.5:", functions.triangle_area(a,h))
    
elif formula == '3':
    print("Введіть радіус кола")
    r = int(input())
    print(f"Площа круга  {functions.math.pi}*{functions.math.pow(r,2)}:", functions.circle_area(r))
    

    


