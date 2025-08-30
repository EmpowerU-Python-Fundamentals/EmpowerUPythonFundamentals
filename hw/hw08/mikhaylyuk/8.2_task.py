password = input("Введіть пароль ")

lower = any(ch.islower() for ch in password)
upper = any(ch.isupper() for ch in password)
digits = any(ch.isdigit() for ch in password)
symbol = any(ch in "@#$" for ch in password)
length = 6 <= len(password) <= 16

if lower and upper and digits and symbol and length:
    print("Valid Password")
else:
    print("Invalid Password")

    