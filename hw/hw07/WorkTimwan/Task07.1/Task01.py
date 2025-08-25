def large_number (a, b):
    if a > b :
        print(f"The bigger number is first", a)
    elif a < b :
        print(f"The bigger number is second", b)
    else:
        print("Its simple")

a = float(input("Enter the first number "))
b = float(input("Enter the second number "))

number = large_number(a, b)