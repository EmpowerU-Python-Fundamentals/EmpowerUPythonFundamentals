def check_age(age: int) -> str:
    """
    Перевіряє, чи є вік парним або непарним.
    
    Args:
        age (int): Вік, який потрібно перевірити.
        
    Raises:
        ValueError: Якщо вік є від'ємним числом.
        
    Returns:
        str: Повідомлення про парність або непарність віку.
    """
    if age < 0:
        raise ValueError("Age cannot be negative!")
    
    if age % 2 == 0:
        return "Your age is even."
    else:
        return "Your age is odd."

def main():
    """
    Основна функція для взаємодії з користувачем.
    """
    try:
        age_input = input("Enter your age: ")
        
        # Перевіряємо, чи є вхідні дані цілим числом.
        if not age_input.strip().isdigit():
            print("Error: Please enter a valid integer number for age.")
            return

        age = int(age_input)
        message = check_age(age)
        print(message)
    except ValueError as e:
        # Обробляємо виняток, що виникає, якщо age < 0
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
