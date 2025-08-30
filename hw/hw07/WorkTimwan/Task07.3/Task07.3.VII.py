num = int(input("enter the number "))

sum = 0

if num <=0:
    print("0")
for i in range(num):



    if i %3 == 0:
        num2 = i
        sum = sum + num2 

    elif i %5 == 0:
        num2 = i
        sum = sum + num2 

print(f"sum =, {sum}")