def get_day_of_week(day_number_str):
    """
    Аналізує введене число і повертає відповідний день тижня.
    Обробляє нечислові дані, від'ємні числа та числа поза діапазоном.
    """
    try:
        day_number = int(day_number_str)
        
        if day_number < 1:
            return "Помилка: будь ласка, введіть додатне число.", False
            
        days = {
            1: "Понеділок", 2: "Вівторок", 3: "Середа", 4: "Четвер", 5: "П'ятниця", 6: "Субота", 7: "Неділя"
        }
        
        # Обчислюємо відповідний день тижня за допомогою операції "modulo"
        effective_day = day_number % 7
        if effective_day == 0:
            effective_day = 7
        
        day_name = days[effective_day]

        if day_number > 7:
            # Створюємо дружнє повідомлення для чисел більше 7
            message = f"Число {day_number} відповідає дню: {day_name}. Напевно, ви мали на увазі {effective_day}."
            return message, True
        else:
            return f"Число {day_number} відповідає дню: {day_name}", True
            
    except (ValueError, KeyError):
        return "Неправильне введення. Будь ласка, введіть число.", False

# Основний код
while True:
    user_input = input("Введіть число, щоб дізнатися день тижня: ")
    result, is_valid = get_day_of_week(user_input)
    print(result)
    
    if is_valid:
        break