from linguist import (
    user_create, user_get_by_id, user_update_name, user_change_password, user_delete_by_id,
    deck_create, deck_get_by_id, deck_update, deck_delete_by_id,
    card_create, card_get_by_id, card_filter, card_update, card_delete_by_id)

if __name__ == "__main__":

    kate = user_create("Kate", "kate@example.com", "pass123")
    assert user_get_by_id(kate.id).email == "kate@example.com"

    user_update_name(kate.id, "Kate Doe")
    assert user_get_by_id(kate.id).name == "Kate Doe"

    assert user_change_password(kate.id, "pass123", "newpass") is True
    assert user_change_password(kate.id, "wrongpass", "x") is False

    test_user = user_create("Max", "max@example.com", "maxpass")
    assert user_delete_by_id(test_user.id) is True
    assert user_get_by_id(test_user.id) is None

    basic_verbs_deck = deck_create("Basic verbs", kate.id)
    assert deck_get_by_id(basic_verbs_deck.id).name == "Basic verbs"

    deck_update(basic_verbs_deck.id, "Core verbs")
    assert deck_get_by_id(basic_verbs_deck.id).name == "Core verbs"

    test_deck = deck_create("Temp deck", kate.id)
    assert deck_delete_by_id(test_deck.id) is True
    assert deck_get_by_id(test_deck.id) is None

    card_run = card_create(kate.id, basic_verbs_deck.id, "run", "бігти", "think of running")
    card_read = card_create(kate.id, basic_verbs_deck.id, "read", "читати", "books -> read")

    found_cards = card_filter("read")
    assert len(found_cards) == 1 and found_cards[0].word == "read"

    card_update(card_run.id, tip="fast movement")
    assert card_get_by_id(card_run.id).tip == "fast movement"

    card_delete_by_id(card_read.id)
    assert card_get_by_id(card_read.id) is None

    print("All tests passed successfully.")
