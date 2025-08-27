# linguist.py

from typing import Optional, Tuple


# ------------------- Models -------------------

class User:
    def __init__(self, id: int, name: str, email: str, password: str):
        self.id = id
        self.name = name
        self.email = email
        self.password = password


class Deck:
    def __init__(self, id: int, name: str, user_id: int):
        self.id = id
        self.name = name
        self.user_id = user_id


class Card:
    def __init__(self, id: int, user_id: int, word: str, translation: str, tip: str):
        self.id = id
        self.user_id = user_id
        self.word = word
        self.translation = translation
        self.tip = tip


# ------------------- In-memory storage -------------------

_users: dict[int, User] = {}
_decks: dict[int, Deck] = {}
_cards: dict[int, Card] = {}

_user_id_counter = 1
_deck_id_counter = 1
_card_id_counter = 1


# ------------------- User functions -------------------

def user_create(name: str, email: str, password: str) -> User:
    """Creates a new user and returns the User object."""
    global _user_id_counter
    user = User(_user_id_counter, name, email, password)
    _users[_user_id_counter] = user
    _user_id_counter += 1
    return user


def user_get_by_id(user_id: int) -> Optional[User]:
    """Retrieves a user by their ID."""
    return _users.get(user_id)


def user_update_name(user_id: int, name: str) -> Optional[User]:
    """Updates the name of a user and returns the User object."""
    user = _users.get(user_id)
    if user:
        user.name = name
    return user


def user_change_password(user_id: int, old_password: str, new_password: str) -> bool:
    """Changes the password of a user and returns True if successful."""
    user = _users.get(user_id)
    if user and user.password == old_password:
        user.password = new_password
        return True
    return False


def user_delete_by_id(user_id: int) -> bool:
    """Deletes a user by ID."""
    return _users.pop(user_id, None) is not None


# ------------------- Deck functions -------------------

def deck_create(name: str, user_id: int) -> Deck:
    """Creates a new deck for a user."""
    global _deck_id_counter
    deck = Deck(_deck_id_counter, name, user_id)
    _decks[_deck_id_counter] = deck
    _deck_id_counter += 1
    return deck


def deck_get_by_id(deck_id: int) -> Optional[Deck]:
    """Retrieves a deck by ID."""
    return _decks.get(deck_id)


def deck_update(deck_id: int, name: str) -> Optional[Deck]:
    """Updates the name of a deck."""
    deck = _decks.get(deck_id)
    if deck:
        deck.name = name
    return deck


def deck_delete_by_id(deck_id: int) -> bool:
    """Deletes a deck by ID."""
    return _decks.pop(deck_id, None) is not None


# ------------------- Card functions -------------------

def card_create(user_id: int, word: str, translation: str, tip: str) -> Card:
    """Creates a new flashcard."""
    global _card_id_counter
    card = Card(_card_id_counter, user_id, word, translation, tip)
    _cards[_card_id_counter] = card
    _card_id_counter += 1
    return card


def card_get_by_id(card_id: int) -> Optional[Card]:
    """Retrieves a flashcard by ID."""
    return _cards.get(card_id)


def card_filter(sub_word: str) -> Tuple[Card, ...]:
    """Finds all flashcards containing sub_word in word, translation, or tip."""
    result = [
        card for card in _cards.values()
        if sub_word.lower() in card.word.lower()
        or sub_word.lower() in card.translation.lower()
        or sub_word.lower() in card.tip.lower()
    ]
    return tuple(result)


def card_update(card_id: int, word: Optional[str] = None,
                translation: Optional[str] = None,
                tip: Optional[str] = None) -> Optional[Card]:
    """Updates a flashcard's fields."""
    card = _cards.get(card_id)
    if card:
        if word is not None:
            card.word = word
        if translation is not None:
            card.translation = translation
        if tip is not None:
            card.tip = tip
    return card


def card_delete_by_id(card_id: int) -> bool:
    """Deletes a flashcard by ID."""
    return _cards.pop(card_id, None) is not None
