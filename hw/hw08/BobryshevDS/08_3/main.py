import task2

def user_choice():
    while True:
        print("\nОберіть фігуру для обчислення площі:")
        print("1. Прямокутник")
        print("2. Трикутник")
        print("3. Коло")

        choice = input("Оберіть номер фігури (1/2/3): ")
        area = task2.calculate_area(choice)

        if area is not None:
            print(f"Площа: {area}")

        next = input("\nБажаєте обчислити ще одну площу? (так/ні): ").lower()
        if next != 'так':
            print("До побачення!")
            break

if __name__ == "__main__":
    user_choice()