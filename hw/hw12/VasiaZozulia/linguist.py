class User:
    def __init__(self, user_id, name, email, password):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password


class Deck:
    def __init__(self, deck_id, name, user_id):
        self.id = deck_id
        self.name = name
        self.user_id = user_id


class Card:
    def __init__(self, card_id, user_id, word, translation, tip):
        self.id = card_id
        self.user_id = user_id
        self.word = word
        self.translation = translation
        self.tip = tip


_users = {}
_decks = {}
_cards = {}
_next_ids = {"user": 1, "deck": 1, "card": 1}

def user_create(name, email, password):
    """Creates a new user and returns the User object."""
    user_id = _next_ids["user"]
    _next_ids["user"] += 1
    user = User(user_id, name, email, password)
    _users[user_id] = user
    return user


def user_get_by_id(user_id):
    """Retrieves a user by ID."""
    return _users.get(user_id)


def user_update_name(user_id, name):
    """Updates user name."""
    user = _users.get(user_id)
    if user:
        user.name = name
    return user


def user_change_password(user_id, old_password, new_password):
    """Changes user password if old matches."""
    user = _users.get(user_id)
    if user and user.password == old_password:
        user.password = new_password
        return True
    return False


def user_delete_by_id(user_id):
    """Deletes user by ID."""
    return _users.pop(user_id, None) is not None


def deck_create(name, user_id):
    """Creates a deck for a user."""
    deck_id = _next_ids["deck"]
    _next_ids["deck"] += 1
    deck = Deck(deck_id, name, user_id)
    _decks[deck_id] = deck
    return deck


def deck_get_by_id(deck_id):
    """Retrieves a deck by ID."""
    return _decks.get(deck_id)


def deck_update(deck_id, name):
    """Updates deck name."""
    deck = _decks.get(deck_id)
    if deck:
        deck.name = name
    return deck


def deck_delete_by_id(deck_id):
    """Deletes a deck by ID."""
    return _decks.pop(deck_id, None) is not None


def card_create(user_id, word, translation, tip):
    """Creates a new card."""
    card_id = _next_ids["card"]
    _next_ids["card"] += 1
    card = Card(card_id, user_id, word, translation, tip)
    _cards[card_id] = card
    return card


def card_get_by_id(card_id):
    """Gets a card by ID."""
    return _cards.get(card_id)


def card_filter(sub_word):
    """Finds cards containing sub_word in word, translation, or tip."""
    results = [
        c for c in _cards.values()
        if sub_word.lower() in c.word.lower()
        or sub_word.lower() in c.translation.lower()
        or sub_word.lower() in c.tip.lower()
    ]
    return tuple(results)


def card_update(card_id, word=None, translation=None, tip=None):
    """Updates fields of a card."""
    card = _cards.get(card_id)
    if card:
        if word: card.word = word
        if translation: card.translation = translation
        if tip: card.tip = tip
    return card


def card_delete_by_id(card_id):
    """Deletes a card by ID."""
    return _cards.pop(card_id, None) is not None
