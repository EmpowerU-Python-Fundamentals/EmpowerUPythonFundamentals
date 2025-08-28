import linguist
import os

def run_tests():
    """Runs a series of tests to verify the functionality of the SQLAlchemy-based linguist application."""

    if os.path.exists("./linguist.db"):
        os.remove("./linguist.db")

    linguist.Base.metadata.create_all(bind=linguist.engine)

    user1 = linguist.user_create("John Doe", "john@example.com", "password123")
    assert user1.name == "John Doe", "User creation failed."
    print("User created successfully.")

    retrieved_user = linguist.user_get_by_id(user1.id)
    assert retrieved_user.name == "John Doe", "User retrieval failed."
    print("User retrieved successfully.")

    updated_user = linguist.user_update_name(user1.id, "Jane Doe")
    assert updated_user.name == "Jane Doe", "User name update failed."
    print("User name updated successfully.")

    password_changed = linguist.user_change_password(user1.id, "password123", "new_password456")
    assert password_changed is True, "Password change with correct old password failed."
    print("Password changed successfully.")
    password_change_failed = linguist.user_change_password(user1.id, "incorrect_password", "another_new_password")
    assert password_change_failed is False, "Password should not have changed with incorrect old password."
    print("Password change failed as expected with incorrect old password.")

    deck1 = linguist.deck_create("Basic Greetings", user1.id)
    assert deck1.name == "Basic Greetings", "Deck creation failed."
    print("Deck created successfully.")

    retrieved_deck = linguist.deck_get_by_id(deck1.id)
    assert retrieved_deck.name == "Basic Greetings", "Deck retrieval failed."
    print("Deck retrieved successfully.")

    updated_deck = linguist.deck_update(deck1.id, "Common Phrases")
    assert updated_deck.name == "Common Phrases", "Deck name update failed."
    print("Deck name updated successfully.")

    card1 = linguist.card_create(user1.id, "Hello", "Привіт", "Sounds like 'Pree-veet'")
    card2 = linguist.card_create(user1.id, "Goodbye", "До побачення", "Doh po-ba-chen-nya")
    assert card1.word == "Hello", "Card creation failed."
    assert card2.word == "Goodbye", "Second card creation failed."
    print("Cards created successfully.")

    retrieved_card = linguist.card_get_by_id(card1.id)
    assert retrieved_card.word == "Hello", "Card retrieval failed."
    print("Card retrieved successfully.")

    filtered_cards = linguist.card_filter("Goodbye")
    assert len(filtered_cards) == 1, "Card filter by word failed."
    assert filtered_cards[0].translation == "До побачення", "Card filter by translation failed."

    filtered_cards_by_tip = linguist.card_filter("Pree-veet")
    assert len(filtered_cards_by_tip) == 1, "Card filter by tip failed."
    print("Cards filtered successfully.")

    updated_card = linguist.card_update(card1.id, translation="Вітаю")
    assert updated_card.translation == "Вітаю", "Card update failed."
    print("Card updated successfully.")

    card_deleted = linguist.card_delete_by_id(card2.id)
    assert card_deleted is True, "Card deletion failed."
    assert linguist.card_get_by_id(card2.id) is None, "Card still exists after deletion."
    print("Card deleted successfully.")

    deck_deleted = linguist.deck_delete_by_id(deck1.id)
    assert deck_deleted is True, "Deck deletion failed."
    assert linguist.deck_get_by_id(deck1.id) is None, "Deck still exists after deletion."
    print("Deck deleted successfully.")

    user_deleted = linguist.user_delete_by_id(user1.id)
    assert user_deleted is True, "User deletion failed."
    assert linguist.user_get_by_id(user1.id) is None, "User still exists after deletion."
    print("User deleted successfully.")

    if os.path.exists("./linguist.db"):
        os.remove("./linguist.db")

    print("\nAll tests passed!")


if __name__ == "__main__":
    run_tests()