from dataclasses import dataclass, field
from typing import Optional, List, Tuple

# --- In-memory "Database" ---
# Using dictionaries for O(1) lookup by ID.
_users_db = {}
_decks_db = {}
_cards_db = {}

# Counters for creating unique IDs
_next_user_id = 1
_next_deck_id = 1
_next_card_id = 1


# --- Models ---
@dataclass
class User:
    """Represents a user in the language learning application."""
    id: int
    name: str
    email: str
    password: str

@dataclass
class Deck:
    """Represents a deck of flashcards belonging to a user."""
    id: int
    name: str
    user_id: int

@dataclass
class Card:
    """Represents a single flashcard with a word, translation, and tip."""
    id: int
    user_id: int
    word: str
    translation: str
    tip: str

# --- User Functions ---

def user_create(name: str, email: str, password: str) -> Optional[User]:
    """
    Creates a new user and returns the User object.

    Args:
        name (str): The name of the user.
        email (str): The user's email address.
        password (str): The user's password.

    Returns:
        User: The created User object.
    """
    global _next_user_id
    new_user = User(id=_next_user_id, name=name, email=email, password=password)
    _users_db[new_user.id] = new_user
    _next_user_id += 1
    return new_user

def user_get_by_id(user_id: int) -> Optional[User]:
    """
    Retrieves a user by their ID and returns the User object.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        Optional[User]: The User object if found, otherwise None.
    """
    return _users_db.get(user_id)

def user_update_name(user_id: int, new_name: str) -> Optional[User]:
    """
    Updates the name of a user and returns the updated User object.

    Args:
        user_id (int): The ID of the user to update.
        new_name (str): The new name for the user.

    Returns:
        Optional[User]: The updated User object if found, otherwise None.
    """
    user = user_get_by_id(user_id)
    if user:
        user.name = new_name
    return user

def user_change_password(user_id: int, old_password: str, new_password: str) -> bool:
    """
    Changes the password of a user and returns a Boolean value indicating success or failure.

    Args:
        user_id (int): The ID of the user.
        old_password (str): The current password.
        new_password (str): The new password to set.

    Returns:
        bool: True if the password was successfully changed, False otherwise.
    """
    user = user_get_by_id(user_id)
    if user and user.password == old_password:
        user.password = new_password
        return True
    return False

def user_delete_by_id(user_id: int) -> bool:
    """
    Deletes a user by their ID and returns a Boolean value indicating success or failure.
    Also deletes all associated decks and cards.

    Args:
        user_id (int): The ID of the user to delete.

    Returns:
        bool: True if the user was successfully deleted, False otherwise.
    """
    if user_id in _users_db:
        # Delete user's decks and cards first
        decks_to_delete = [deck.id for deck in _decks_db.values() if deck.user_id == user_id]
        for deck_id in decks_to_delete:
            deck_delete_by_id(deck_id)

        cards_to_delete = [card.id for card in _cards_db.values() if card.user_id == user_id]
        for card_id in cards_to_delete:
            card_delete_by_id(card_id)

        del _users_db[user_id]
        return True
    return False

# --- Deck Functions ---

def deck_create(name: str, user_id: int) -> Optional[Deck]:
    """
    Creates a new deck belonging to a user and returns the Deck object.

    Args:
        name (str): The name of the deck.
        user_id (int): The ID of the user who owns the deck.

    Returns:
        Optional[Deck]: The created Deck object if the user exists, otherwise None.
    """
    global _next_deck_id
    if user_get_by_id(user_id):
        new_deck = Deck(id=_next_deck_id, name=name, user_id=user_id)
        _decks_db[new_deck.id] = new_deck
        _next_deck_id += 1
        return new_deck
    return None

def deck_get_by_id(deck_id: int) -> Optional[Deck]:
    """
    Retrieves a deck by its ID and returns the Deck object.

    Args:
        deck_id (int): The ID of the deck to retrieve.

    Returns:
        Optional[Deck]: The Deck object if found, otherwise None.
    """
    return _decks_db.get(deck_id)

def deck_update(deck_id: int, new_name: str) -> Optional[Deck]:
    """
    Updates the name of a deck and returns the updated Deck object.

    Args:
        deck_id (int): The ID of the deck to update.
        new_name (str): The new name for the deck.

    Returns:
        Optional[Deck]: The updated Deck object if found, otherwise None.
    """
    deck = deck_get_by_id(deck_id)
    if deck:
        deck.name = new_name
    return deck

def deck_delete_by_id(deck_id: int) -> bool:
    """
    Deletes a deck by its ID and returns a Boolean value indicating success or failure.

    Args:
        deck_id (int): The ID of the deck to delete.

    Returns:
        bool: True if the deck was successfully deleted, False otherwise.
    """
    if deck_id in _decks_db:
        del _decks_db[deck_id]
        return True
    return False

# --- Card Functions ---

def card_create(user_id: int, word: str, translation: str, tip: str) -> Optional[Card]:
    """
    Creates a new flashcard and returns the Card object.

    Args:
        user_id (int): The ID of the user who owns the card.
        word (str): The English word.
        translation (str): The Ukrainian translation.
        tip (str): A tip for remembering the word.

    Returns:
        Optional[Card]: The created Card object if the user exists, otherwise None.
    """
    global _next_card_id
    if user_get_by_id(user_id):
        new_card = Card(id=_next_card_id, user_id=user_id, word=word, translation=translation, tip=tip)
        _cards_db[new_card.id] = new_card
        _next_card_id += 1
        return new_card
    return None

def card_get_by_id(card_id: int) -> Optional[Card]:
    """
    Retrieves a flashcard by its ID and returns the Card object.

    Args:
        card_id (int): The ID of the card to retrieve.

    Returns:
        Optional[Card]: The Card object if found, otherwise None.
    """
    return _cards_db.get(card_id)

def card_filter(sub_word: str) -> Tuple[Card, ...]:
    """
    Retrieves all flashcards containing a substring in either the word,
    translation, or tip fields and returns a tuple of Card objects.

    Args:
        sub_word (str): The substring to search for.

    Returns:
        Tuple[Card, ...]: A tuple of matching Card objects.
    """
    sub_word_lower = sub_word.lower()
    matching_cards = []
    for card in _cards_db.values():
        if (sub_word_lower in card.word.lower() or
            sub_word_lower in card.translation.lower() or
            sub_word_lower in card.tip.lower()):
            matching_cards.append(card)
    return tuple(matching_cards)

def card_update(card_id: int, word: Optional[str] = None, translation: Optional[str] = None, tip: Optional[str] = None) -> Optional[Card]:
    """
    Updates the fields of a flashcard and returns the updated Card object.

    Args:
        card_id (int): The ID of the card to update.
        word (Optional[str]): The new English word.
        translation (Optional[str]): The new Ukrainian translation.
        tip (Optional[str]): The new tip.

    Returns:
        Optional[Card]: The updated Card object if found, otherwise None.
    """
    card = card_get_by_id(card_id)
    if card:
        if word is not None:
            card.word = word
        if translation is not None:
            card.translation = translation
        if tip is not None:
            card.tip = tip
    return card

def card_delete_by_id(card_id: int) -> bool:
    """
    Deletes a flashcard by its ID and returns a Boolean value indicating success or failure.

    Args:
        card_id (int): The ID of the flashcard to delete.

    Returns:
        bool: True if the card was successfully deleted, False otherwise.
    """
    if card_id in _cards_db:
        del _cards_db[card_id]
        return True
    return False

# --- Helper for Testing ---
def reset_db():
    """Resets the in-memory database for clean testing."""
    global _users_db, _decks_db, _cards_db, _next_user_id, _next_deck_id, _next_card_id
    _users_db.clear()
    _decks_db.clear()
    _cards_db.clear()
    _next_user_id = 1
    _next_deck_id = 1
    _next_card_id = 1

