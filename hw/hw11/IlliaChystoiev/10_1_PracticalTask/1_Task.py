def process_age(age):
    if age < 0:
        raise ValueError("Вік не може бути від'ємним.")
    
    if age % 2 == 0:
        print(f"Ваш вік {age} є парним.")
    else:
        print(f"Ваш вік {age} є непарним.")

def main():
    try:
        age = int(input("Введіть свій вік: "))
        process_age(age)
    except ValueError as e:
        print(f"Помилка: {e}")
    except Exception as e:
        print(f"Несподівана помилка: {e}")

if __name__ == "__main__":
    main()
