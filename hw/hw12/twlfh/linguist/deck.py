class Deck:
    """
    Represents a deck of flashcards.
    """
    def __init__(self, deck_id: int, name: str, user_id: int):
        self.deck_id = deck_id
        self.name = name
        self.user_id = user_id
    """
    Initialize a new Deck object.
    Args:
        deck_id (int): Unique deck ID.
        name (str): Name of the deck.
        user_id (int): ID of the user who owns the deck.
    """


deck_db = {}
def deck_create(name, user_id):
    """Created a new deck"""
    new_deck_id = max(deck_db.keys(), default=0) + 1
    deck = Deck(new_deck_id, name, user_id)
    deck_db[new_deck_id] = deck
    return deck

def deck_get_by_id(deck_id):
    """Retrieve a deck by ID."""
    return deck_db.get(deck_id)

def deck_update(deck_id, name):
    """Update the name of a deck."""
    deck = deck_db.get(deck_id)
    if deck:
        deck.name = name
        return deck
    else:
        return False

def deck_delete_by_id(deck_id):
    """Delete a deck by ID"""
    if deck_id in deck_db:
        del deck_db[deck_id]
        return True
    else:
        return False