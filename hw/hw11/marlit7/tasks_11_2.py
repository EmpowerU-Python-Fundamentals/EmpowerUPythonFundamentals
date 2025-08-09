def age():
    try:
        num=int(input("Вік: "))
        if num<1:
            raise ValueError
        else:
            if num%2==0:
                print("Парне")
            else:
                print("Непарне")
    except ValueError:
        print("Не вірний вік")

while True:
    age()