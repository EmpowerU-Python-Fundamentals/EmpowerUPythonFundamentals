# Використання константи для зберігання днів тижня
DAYS = {
    1: "Monday", 
    2: "Tuesday", 
    3: "Wednesday", 
    4: "Thursday", 
    5: "Friday", 
    6: "Saturday", 
    7: "Sunday"
}

def get_day_of_week(number: int) -> str:
    """
    Повертає день тижня за його номером.

    Args:
        number (int): Номер дня тижня (1-7).

    Returns:
        str: Назва дня тижня.
    
    Raises:
        ValueError: Якщо номер поза діапазоном 1-7.
    """
    if number not in DAYS:
        raise ValueError("Invalid number! Please enter a number from 1 to 7.")
    return DAYS[number]

def main():
    """
    Основна функція для взаємодії з користувачем.
    """
    user_input = input("Enter a number (1-7) for the day of the week: ")
    
    try:
        # Перевіряємо, чи можна перетворити вхідні дані на float
        num_float = float(user_input)
        
        # Перевіряємо, чи є число цілим
        if not num_float.is_integer():
            print("Error: Please enter an integer number.")
            return
            
        num = int(num_float)
        day = get_day_of_week(num)
        print(f"The day of the week for number {num} is {day}.")

    except ValueError as e:
        # Обробка винятків для нечислових даних та чисел поза діапазоном
        print(f"Error: {e}")
    except KeyError:
        # Додаткова перевірка на випадок, якщо функція get_day_of_week не підняла ValueError
        print("Error: Invalid number! Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
