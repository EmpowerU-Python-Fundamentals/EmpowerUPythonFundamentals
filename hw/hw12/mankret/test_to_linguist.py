import linguist as lg

# Create user
u = lg.user_create("Anton", "anton@example.com", "1234")
assert u.id == 1

# Read user
assert lg.user_get_by_id(u.id).email == "anton@example.com"

# Update name
lg.user_update_name(u.id, "Антон")
assert lg.user_get_by_id(u.id).name == "Антон"

# Change password
assert lg.user_change_password(u.id, "1234", "5678")
assert not lg.user_change_password(u.id, "wrong", "pass")

# Decks
d = lg.deck_create("Top verbs", u.id)
assert d.name == "Top verbs"
lg.deck_update(d.id, "Top verbs A1")
assert lg.deck_get_by_id(d.id).name == "Top verbs A1"

# Cards
c = lg.card_create(u.id, "go", "йти", "irregular")
assert lg.card_get_by_id(c.id).word == "go"

hits = lg.card_filter("йти")
assert hits and hits[0].word == "go"

lg.card_update(c.id, tip="went/gone")
assert lg.card_get_by_id(c.id).tip == "went/gone"

assert lg.card_delete_by_id(c.id)

# Delete user
t = lg.user_delete_by_id(u.id)
assert t

print("All tests passed")

