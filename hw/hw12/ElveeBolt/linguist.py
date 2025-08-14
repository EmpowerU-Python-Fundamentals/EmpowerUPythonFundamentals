from card import card_create, card_filter, card_update, card_delete_by_id, card_get_by_id
from deck import deck_get_by_id, deck_create, deck_update
from user import user_create, user_get_by_id, user_update_name, user_change_password

if __name__ == "__main__":
    u1 = user_create("Alice", "alice@example.com", "pass")
    assert user_get_by_id(u1.id).email == "alice@example.com"

    user_update_name(u1.id, "Alice Cooper")
    assert user_get_by_id(u1.id).name == "Alice Cooper"

    assert user_change_password(u1.id, "pass", "newpass") is True
    assert user_change_password(u1.id, "wrong", "x") is False

    d1 = deck_create("Basic verbs", u1.id)
    assert deck_get_by_id(d1.id).name == "Basic verbs"

    deck_update(d1.id, "Core verbs")
    assert deck_get_by_id(d1.id).name == "Core verbs"

    c1 = card_create(u1.id, "run", "бігти", "think of running")
    c2 = card_create(u1.id, "read", "читати", "books -> read")

    found = card_filter("read")
    assert len(found) == 1 and found[0].word == "read"

    card_update(c1.id, tip="fast movement")
    assert card_get_by_id(c1.id).tip == "fast movement"

    card_delete_by_id(c2.id)
    assert card_get_by_id(c2.id) is None

    print("All tests passed ✅")