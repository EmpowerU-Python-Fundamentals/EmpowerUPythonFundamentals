def day_of_week(number):
    days_of_week = {
        1: "Понеділок",
        2: "Вівторок",
        3: "Середа",
        4: "Четвер",
        5: "П'ятниця",
        6: "Субота",
        7: "Неділя"
    }
    
    return days_of_week[number]

def main():
    while True:
        try:
            user_input = int(input("Введіть число (1-7), щоб дізнатися день тижня: "))
            day = day_of_week(user_input) if 1 <= user_input <= 7 else None

            if day:  
                print(f"День тижня: {day}")
                break  
            else:
                print("Число повинно бути в межах від 1 до 7.")
        
        except ValueError:
           print("Помилка: введено некоректне значення. Будь ласка, введіть число.")

if __name__ == "__main__":
    main()
