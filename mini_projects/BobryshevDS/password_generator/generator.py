import random
import string

def generate_password(length: int, use_letters: bool, use_numbers: bool, use_symbols: bool, use_uppercase: bool, exclude_ambiguous: bool, is_accountant_mode: bool) -> str:
    """
    Генерує пароль на основі заданих критеріїв.
    """
    if is_accountant_mode:
        # Режим бухгалтера: дуже простий пароль з літер і цифр
        simple_chars = string.ascii_lowercase + string.digits
        return "".join(random.choices(simple_chars, k=length))

    # 1. Визначаємо набір символів для генерації
    characters = ""
    if use_letters:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # 2. Якщо обрано виключення неоднозначних символів
    if exclude_ambiguous:
        ambiguous_chars = "O0Il|"
        for char in ambiguous_chars:
            characters = characters.replace(char, "")

    # 3. Гарантуємо наявність хоча б одного символу з кожного обраного типу
    password = []
    if use_letters:
        password.append(random.choice(string.ascii_lowercase))
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    # 4. Доповнюємо пароль до потрібної довжини
    remaining_length = length - len(password)
    if remaining_length > 0:
        if not characters:
            return "Помилка: Не обрано жодного типу символів."
        
        password.extend(random.choices(characters, k=remaining_length))
    
    # Обрізаємо пароль, якщо початкова довжина була занадто малою
    password = password[:length]

    # 5. Перемішуємо символи, щоб вони не йшли послідовно
    random.shuffle(password)

    # 6. Об'єднуємо список символів у рядок та повертаємо результат
    return "".join(password)