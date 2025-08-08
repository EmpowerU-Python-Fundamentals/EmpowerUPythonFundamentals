import re

def validate_password(password):
    """
    Перевіряє, чи відповідає пароль усім вимогам.
    
    Вимоги:
    - Довжина від 6 до 16 символів.
    - Містить принаймні одну малу літеру [a-z].
    - Містить принаймні одну велику літеру [A-Z].
    - Містить принаймні один спеціальний символ з [$#@].
    
    Аргументи:
        password (str): Пароль для перевірки.
    
    Повертає:
        bool: True, якщо пароль валідний, інакше False.
    """
    
    # Визначення умов за допомогою булевих виразів.
    is_length_valid = 6 <= len(password) <= 16
    has_lowercase = re.search(r'[a-z]', password)
    has_uppercase = re.search(r'[A-Z]', password)
    has_special_char = re.search(r'[$#@]', password)
    
    # Перевірка всіх умов одночасно.
    return all([is_length_valid, has_lowercase, has_uppercase, has_special_char])


# --- Основна частина програми ---
# Цей код отримує пароль від користувача та перевіряє його.

if __name__ == "__main__":
    while True:
        print("This program checks the validity of a password. Be careful to not to use a real password!")
        password = input("Please, enter your fake password: ")
        
        if validate_password(password):
            print("Password is right.")
            break
        else:
            print("Password doesn't meet the requirements. Please, try again.")

