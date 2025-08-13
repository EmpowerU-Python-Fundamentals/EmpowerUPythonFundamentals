import linguist as l

print("=== Creating a new user ===")
u1 = l.user_create("Alice", "alice@example.com", "pass123")
print(f"User created: {u1.id} | {u1.name} | {u1.email}")

print("\n=== Retrieving user by ID ===")
user = l.user_get_by_id(u1.id)
print(f"Retrieved: {user.id} | {user.name}")

print("\n=== Updating user name ===")
l.user_update_name(u1.id, "Alicia")
print(f"Updated name: {u1.name}")

print("\n=== Changing password ===")
success = l.user_change_password(u1.id, "pass123", "newpass")
print(f"Password change success: {success}")
fail = l.user_change_password(u1.id, "wrong", "pass")
print(f"Password change (wrong old password) success: {fail}")

print("\n=== Creating a new deck ===")
d1 = l.deck_create("Animals", u1.id)
print(f"Deck created: {d1.id} | {d1.name}")

print("\n=== Updating deck name ===")
l.deck_update(d1.id, "Wild Animals")
print(f"Deck updated: {d1.name}")

print("\n=== Creating cards ===")
c1 = l.card_create(u1.id, "cat", "кіт", "Think of 'kitten'")
c2 = l.card_create(u1.id, "dog", "собака", "Like 'sobaka' in Ukrainian")
print(f"Card 1: {c1.id} | {c1.word} - {c1.translation} | {c1.tip}")
print(f"Card 2: {c2.id} | {c2.word} - {c2.translation} | {c2.tip}")

print("\n=== Filtering cards containing 'sobaka' ===")
filtered = l.card_filter("sobaka")
for card in filtered:
    print(f"Found: {card.id} | {card.word} - {card.translation} | {card.tip}")

print("\n=== Updating card tip ===")
l.card_update(c1.id, tip="Small furry animal")
print(f"Updated card 1: {c1.word} - {c1.translation} | {c1.tip}")

print("\n=== Deleting card 2 ===")
deleted_card = l.card_delete_by_id(c2.id)
print(f"Card 2 deleted: {deleted_card}")

print("\n=== Deleting deck ===")
deleted_deck = l.deck_delete_by_id(d1.id)
print(f"Deck deleted: {deleted_deck}")

print("\n=== Deleting user ===")
deleted_user = l.user_delete_by_id(u1.id)
print(f"User deleted: {deleted_user}")

print("\n=== All tests completed successfully ===")
