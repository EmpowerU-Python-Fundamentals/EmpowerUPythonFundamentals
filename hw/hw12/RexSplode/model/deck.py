from extensions import db

class Deck(db.Model):
    __tablename__ = 'decks'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, index = True)
    user_id = db.Column(db.Integer)

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f'Deck {self.id=} {self.name=} {self.user_id=}'
    
    def __eq__(self, other):
        if not isinstance(other, Deck):
            return False
        return self.name == other.name and self.user_id == other.user_id
    
    
    @classmethod
    def deck_create(cls, name: str, user_id: int) -> "Deck": 
        """Creates a new instance of Deck and saves it into the DB"""
        deck = cls(name, user_id)
        db.session.add(deck)
        db.session.commit()

        return deck
    
    @classmethod
    def deck_get_by_id(cls, deck_id: int) -> "Deck":
        """Looks for a Deck in the DB. If it's not there, it will return None"""
        return cls.query.get(deck_id)
    
    @classmethod
    def deck_update(cls, deck_id: int, name: str) -> "Deck":
        """Updates the name of the Deck. If the Deck is not found in the DB, it will return None"""
        deck = cls.query.get(deck_id)
        if not deck:
            return None
        
        deck.name = name
        db.commit()
        return deck
    
    @classmethod
    def deck_delete_by_id(cls, deck_id: int) -> bool:
        """Attempt to delete a Deck from the database. If it's already not there, the method returns False"""
        deck = cls.query.get(deck_id)
        if not deck:
            return False
        db.session.delete(deck)
        db.session.commit()
        return True

    

