import os
import linguist
import database

# Перевіряємо, чи існує файл бази даних, і видаляємо його для чистого тестування
# Це місце, де виникала помилка. Виправити її можна, закривши всі програми,
# які можуть використовувати файл.
if os.path.exists("linguist.db"):
    os.remove("linguist.db")
    print("Old 'linguist.db' removed for a clean test run.")

# Створюємо таблиці в новій базі даних через database.py
database.Base.metadata.create_all(database.engine)
print("New database and tables created.")

# ---------------------------------
#            Тестування
# ---------------------------------
print("\n--- Starting tests ---")

# 1. Створення користувача
user = linguist.user_create("John Doe", "john.doe@example.com", "secure-pass")
assert user is not None and user.name == "John Doe"
print("User created successfully. ✅")

# 2. Отримання користувача за ID
fetched_user = linguist.user_get_by_id(user.id)
assert fetched_user is not None and fetched_user.email == "john.doe@example.com"
print("User retrieved successfully. ✅")

# 3. Оновлення імені користувача
updated_user = linguist.user_update_name(user.id, "Jane Doe")
assert updated_user is not None and updated_user.name == "Jane Doe"
print("User name updated successfully. ✅")

# 4. Зміна пароля користувача
assert linguist.user_change_password(user.id, "secure-pass", "new-secure-pass") is True
assert linguist.user_change_password(user.id, "wrong-pass", "new-pass") is False
print("User password changed successfully. ✅")

# 5. Створення колоди
deck = linguist.deck_create("My First Deck", user.id)
assert deck is not None and deck.name == "My First Deck"
print("Deck created successfully. ✅")

# 6. Оновлення колоди
updated_deck = linguist.deck_update(deck.id, "My Updated Deck")
assert updated_deck is not None and updated_deck.name == "My Updated Deck"
print("Deck updated successfully. ✅")

# 7. Створення карток
card1 = linguist.card_create(user.id, "Hello", "Привіт", "Common greeting")
card2 = linguist.card_create(user.id, "World", "Світ", "Everything")
assert card1 is not None and card1.word == "Hello"
assert card2 is not None and card2.word == "World"
print("Cards created successfully. ✅")

# 8. Фільтрування карток
found_cards = linguist.card_filter("віт")
assert len(found_cards) == 1 and found_cards[0].word == "Hello"
print("Card filter working correctly. ✅")

# 9. Оновлення картки
updated_card = linguist.card_update(card1.id, word="Hi", tip="Less formal greeting")
assert updated_card is not None and updated_card.word == "Hi" and updated_card.tip == "Less formal greeting"
print("Card updated successfully. ✅")

# 10. Видалення картки
assert linguist.card_delete_by_id(card2.id) is True
assert linguist.card_get_by_id(card2.id) is None
print("Card deleted successfully. ✅")

# 11. Видалення колоди
assert linguist.deck_delete_by_id(deck.id) is True
assert linguist.deck_get_by_id(deck.id) is None
print("Deck deleted successfully. ✅")

# 12. Видалення користувача
assert linguist.user_delete_by_id(user.id) is True
assert linguist.user_get_by_id(user.id) is None
print("User deleted successfully. ✅")

print("\n--- All tests passed! ✨ ---")

# Важливий крок: примусове закриття всіх з'єднань з базою даних.
database.engine.dispose()
print("Database engine disposed.")
