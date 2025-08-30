class Card:
    """
     Represents a flashcard with a word, translation, and tip.
    """
    def __init__(self, card_id: int, user_id: int, word: str, translation: str, tip: str):
        """
        Initialize a new Card object.

        Args:
            card_id (int): Unique card ID.
            user_id (int): ID of the user who owns the card.
            word (str): Word in English.
            translation (str): Translation in Ukrainian.
            tip (str): Additional hint or description.
        """
        self.card_id = card_id
        self.user_id = user_id
        self.word = word
        self.translation = translation
        self.tip = tip


    def card_update(self, word = None, translation = None, tip = None):
        """Update card fields if provided."""
        if word is not None:
            self.word = word
        if translation is not None:
            self.translation = translation
        if tip is not None:
            self.tip = tip
        return self


cards_db = {}

def card_create(user_id, word, translation, tip):
    """Create a new card."""
    card_id = max(cards_db.keys(), default=0) + 1
    card = Card(card_id, user_id, word, translation, tip)
    cards_db[card_id] = card
    return card

def card_get_by_id(card_id):
    """Retrieve a card by id"""
    return cards_db.get(card_id)

def card_filter(sub_word):
    """Find cards that contain the substring in word, translation, or tip."""
    res = []
    for card in cards_db.values():
        if sub_word.lower() in card.word.lower() or sub_word.lower() in card.translation.lower() or \
                sub_word.lower() in card.tip.lower():
            res.append(card)
    return tuple(res)


def card_delete_by_id(card_id):
    """Deleted a card by ID"""
    if card_id in cards_db:
        del cards_db[card_id]
        return True
    else:
        return False

def card_update(card_id, word=None, translation=None, tip=None):
    """Update fields of a card"""
    card = cards_db.get(card_id)
    if card:
        card.card_update(word, translation, tip)
        return card
    else:
        return False




