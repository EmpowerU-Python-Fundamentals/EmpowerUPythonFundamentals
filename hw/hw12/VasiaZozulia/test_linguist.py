import linguist as lg

user1 = lg.user_create("Vasyl", "vasyl@example.com", "1234")
assert user1.name == "Vasyl"
assert lg.user_get_by_id(user1.id) == user1

lg.user_update_name(user1.id, "Ivan")
assert user1.name == "Ivan"

assert lg.user_change_password(user1.id, "1234", "abcd") is True
assert lg.user_change_password(user1.id, "wrong", "new") is False

assert lg.user_delete_by_id(user1.id) is True

user2 = lg.user_create("Olga", "olga@example.com", "pass")
deck1 = lg.deck_create("Animals", user2.id)
assert deck1.name == "Animals"

lg.deck_update(deck1.id, "Wild Animals")
assert deck1.name == "Wild Animals"

assert lg.deck_get_by_id(deck1.id) == deck1
assert lg.deck_delete_by_id(deck1.id) is True

card1 = lg.card_create(user2.id, "dog", "собака", "Think of 'doge'")
assert card1.translation == "собака"

card2 = lg.card_create(user2.id, "cat", "кіт", "Similar to 'kitten'")
assert lg.card_get_by_id(card2.id) == card2

results = lg.card_filter("kit")
assert card2 in results

lg.card_update(card1.id, translation="пес")
assert card1.translation == "пес"

assert lg.card_delete_by_id(card1.id) is True

print("All tests passed successfully!")
