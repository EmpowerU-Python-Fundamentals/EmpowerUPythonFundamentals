from linguist import (
    user_create, user_get_by_id, user_update_name, user_change_password, user_delete_by_id,
    deck_create, deck_get_by_id, deck_update, deck_delete_by_id,
    card_create, card_get_by_id, card_filter, card_update, card_delete_by_id
)

# User test
user = user_create("Alice", "alice@example.com", "1234")
assert user.id is not None
print("✅ user_create passed")

fetched_user = user_get_by_id(user.id)
assert fetched_user.name == "Alice"
print("✅ user_get_by_id passed")

updated_user = user_update_name(user.id, "Alice Updated")
assert updated_user.name == "Alice Updated"
print("✅ user_update_name passed")

assert user_change_password(user.id, "1234", "abcd") is True
assert user_change_password(user.id, "wrong", "newpass") is False
print("✅ user_change_password passed")

# Deck test
deck = deck_create("English Basics", user.id)
assert deck.id is not None
print("✅ deck_create passed")

fetched_deck = deck_get_by_id(deck.id)
assert fetched_deck.name == "English Basics"
print("✅ deck_get_by_id passed")

updated_deck = deck_update(deck.id, "English Advanced")
assert updated_deck.name == "English Advanced"
print("✅ deck_update passed")

# Card test
card = card_create(user.id, "apple", "яблуко", "Think of Apple Inc.")
assert card.id is not None
print("✅ card_create passed")

fetched_card = card_get_by_id(card.id)
assert fetched_card.word == "apple"
print("✅ card_get_by_id passed")

cards_found = card_filter("apple")
assert len(cards_found) > 0
print("✅ card_filter passed")

updated_card = card_update(card.id, word="pear", translation="груша", tip="Similar to 'pair'")
assert updated_card.word == "pear"
print("✅ card_update passed")

# Delete
assert card_delete_by_id(card.id) is True
assert card_get_by_id(card.id) is None
print("✅ card_delete_by_id passed")

assert deck_delete_by_id(deck.id) is True
assert deck_get_by_id(deck.id) is None
print("✅ deck_delete_by_id passed")

assert user_delete_by_id(user.id) is True
assert user_get_by_id(user.id) is None
print("✅ user_delete_by_id passed")

print("\n All tests passed successfully!")