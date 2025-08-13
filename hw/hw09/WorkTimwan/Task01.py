import random

a = random.randint(0, 100)

for i in range (10) :
    b = int(input("Enter the number"))
    if b == a:
        print("right one")
        exit()
    elif b > a:
        print("smaller one")
    elif b < a:
        print("bigger one")


else :
    print("ha-ha number is", a )