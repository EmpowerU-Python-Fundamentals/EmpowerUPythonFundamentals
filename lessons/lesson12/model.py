import uuid
import random
import re

class Contact:
    def __init__(self, name: str, phone_number: str):
        self.id = uuid.uuid4()
        self.name = name
        self.phone_number = phone_number

    def __repr__(self) -> str:

        return f"Contact(id='{self.id}', name='{self.name}', phone_number='{self.phone_number}')"

    def __str__(self) -> str:
        return f"Ім'я: {self.name}, Номер: {self.phone_number}, ID: {self.id}"



class TelephoneBook:

    def __init__(self):
        """Ініціалізує порожній список для зберігання об'єктів Contact."""
        self.contacts = []

    def add_contact(self, contact: Contact):
        """Додає об'єкт Contact до телефонної книги."""
        self.contacts.append(contact)
        print(f"Контакт '{contact.name}' успішно додано.")

    def remove_contact(self, contact_id: str):
        """Видаляє контакт за його унікальним ID."""
        original_count = len(self.contacts)
        self.contacts = [c for c in self.contacts if c.id != contact_id]
        if len(self.contacts) < original_count:
            print(f"Контакт з ID '{contact_id}' успішно видалено.")
        else:
            print(f"Контакт з ID '{contact_id}' не знайдено.")

    def find_contact_by_id(self, contact_id: str):
        """Знаходить контакт за його унікальним ID."""
        for contact in self.contacts:
            if contact.id == contact_id:
                return contact
        return None

    def list_all_contacts(self):
        return self.contacts


    def generate_random_contacts(self, num_contacts: int):
        """
        Генерує випадкові контакти та додає їх до книги.

        Args:
            num_contacts (int): Кількість контактів для генерації.
        """
        first_names = ["Іван", "Марія", "Петро", "Олена", "Андрій", "Наталія", "Олег"]
        last_names = ["Іванов", "Петров", "Сидорова", "Коваленко", "Григоренко", "Мельник"]

        for _ in range(num_contacts):
            first = random.choice(first_names)
            last = random.choice(last_names)
            name = f"{first} {last}"
            
            # Генеруємо випадковий номер телефону
            phone_number = f"0{random.randint(50, 99)}-{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(10, 99)}"
            
            new_contact = Contact(name, phone_number)
            self.add_contact(new_contact)


# Функція для валідації номера телефону
def validate_phone_number(phone_number: str) -> bool:
    """Перевіряє, чи є номер телефону валідним."""
    # Приклад простого регулярного виразу для українських номерів
    # (може бути розширений для інших форматів)
    # Наприклад, 098-123-45-67 або +380981234567
    pattern = re.compile(r"^(?:\+38)?0[0-9]{2}-?[0-9]{3}-?[0-9]{2}-?[0-9]{2}$")
    return bool(pattern.match(phone_number))