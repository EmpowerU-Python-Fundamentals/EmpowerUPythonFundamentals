import linguist
from linguist import User, Deck, Card

def run_tests():
    """
    Runs a series of tests to verify the functionality of the linguist application.
    """
    print("Running tests for linguist.py...")

    # --- Test 1: User CRUD Operations ---
    print("Testing User CRUD...")
    linguist.reset_db()
    # Create
    user1 = linguist.user_create("John Doe", "john@example.com", "pass123")
    assert user1 is not None and user1.id == 1, "Test 1.1: Failed to create user."
    
    # Read
    retrieved_user = linguist.user_get_by_id(1)
    assert retrieved_user == user1, "Test 1.2: Failed to retrieve user by ID."
    
    # Update Name
    updated_user = linguist.user_update_name(1, "Jane Doe")
    assert updated_user.name == "Jane Doe", "Test 1.3: Failed to update user name."
    
    # Change Password (success)
    password_changed_success = linguist.user_change_password(1, "pass123", "new_pass")
    assert password_changed_success is True, "Test 1.4: Failed to change password."
    retrieved_user = linguist.user_get_by_id(1)
    assert retrieved_user.password == "new_pass", "Test 1.5: Password not correctly updated."
    
    # Change Password (failure)
    password_changed_failure = linguist.user_change_password(1, "wrong_pass", "new_pass2")
    assert password_changed_failure is False, "Test 1.6: Password changed with incorrect old password."
    
    # Delete
    deleted_success = linguist.user_delete_by_id(1)
    assert deleted_success is True, "Test 1.7: Failed to delete user."
    deleted_user = linguist.user_get_by_id(1)
    assert deleted_user is None, "Test 1.8: User was not deleted from database."
    print("User CRUD tests passed.")

    # --- Test 2: Deck CRUD Operations ---
    print("Testing Deck CRUD...")
    linguist.reset_db()
    user1 = linguist.user_create("Deck Owner", "deckowner@test.com", "password")
    
    # Create
    deck1 = linguist.deck_create("English Vocabulary", user1.id)
    assert deck1 is not None and deck1.id == 1 and deck1.user_id == user1.id, "Test 2.1: Failed to create deck."
    
    # Read
    retrieved_deck = linguist.deck_get_by_id(1)
    assert retrieved_deck == deck1, "Test 2.2: Failed to retrieve deck by ID."
    
    # Update
    updated_deck = linguist.deck_update(1, "Advanced English")
    assert updated_deck.name == "Advanced English", "Test 2.3: Failed to update deck name."
    
    # Delete
    deleted_success = linguist.deck_delete_by_id(1)
    assert deleted_success is True, "Test 2.4: Failed to delete deck."
    deleted_deck = linguist.deck_get_by_id(1)
    assert deleted_deck is None, "Test 2.5: Deck was not deleted from database."
    print("Deck CRUD tests passed.")

    # --- Test 3: Card CRUD Operations ---
    print("Testing Card CRUD...")
    linguist.reset_db()
    user1 = linguist.user_create("Card Owner", "cardowner@test.com", "password")
    
    # Create
    card1 = linguist.card_create(user1.id, "Hello", "Привіт", "Greetings are important.")
    card2 = linguist.card_create(user1.id, "World", "Світ", "Think of the world.")
    assert card1 is not None and card1.id == 1, "Test 3.1: Failed to create first card."
    assert card2 is not None and card2.id == 2, "Test 3.2: Failed to create second card."
    
    # Read
    retrieved_card = linguist.card_get_by_id(1)
    assert retrieved_card == card1, "Test 3.3: Failed to retrieve card by ID."
    
    # Update
    updated_card = linguist.card_update(1, word="Hi", translation="Привіт")
    assert updated_card.word == "Hi" and updated_card.translation == "Привіт", "Test 3.4: Failed to update card fields."
    
    # Filter
    filtered_cards = linguist.card_filter("Привіт")
    assert len(filtered_cards) == 1 and filtered_cards[0].word == "Hi", "Test 3.5: Failed to filter by translation."
    
    filtered_cards = linguist.card_filter("world")
    assert len(filtered_cards) == 1 and filtered_cards[0].word == "World", "Test 3.6: Failed to filter by word (case-insensitive)."

    filtered_cards = linguist.card_filter("greetings")
    assert len(filtered_cards) == 1 and filtered_cards[0].word == "Hi", "Test 3.7: Failed to filter by tip."
    
    # Delete
    deleted_success = linguist.card_delete_by_id(1)
    assert deleted_success is True, "Test 3.8: Failed to delete card."
    deleted_card = linguist.card_get_by_id(1)
    assert deleted_card is None, "Test 3.9: Card was not deleted from database."
    print("Card CRUD tests passed.")
    
    print("\nAll tests passed successfully!")

# To run the tests, execute this script directly
if __name__ == "__main__":
    run_tests()
