from extensions import db
from sqlalchemy import or_

class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    word = db.Column(db.Text)
    translation = db.Column(db.Text)
    tip = db.Column(db.Text)

    def __init__(self, user_id: int, word: str, translation: str, tip: str):
        self.user_id = user_id
        self.word = word
        self.translation = translation
        self.tip = tip

    def __repr__(self):
        return f'Card {self.id=} {self.word=} {self.translation=}'
    
    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return (
            self.user_id == other.user_id and
            self.word == other.word and
            self.translation == other.translation and
            self.tip == other.tip
        )
    
    @classmethod
    def card_create(cls, user_id: int, word: str, translation: str, tip: str) -> "Card":
        """Creates a new Card objects and saves it to the DB. I don't check user_id for validity because it's already long task"""
        card =  cls(user_id, word, translation, tip)
        db.session.add(card)

        db.session.commit()
        return card
    
    @classmethod
    def card_get_by_id(cls, card_id: int) -> "Card":
        """Tries to fetch and return a card from DB by id. If there's no such card, returns None."""
        return cls.query.get(card_id)
    
    @classmethod
    def card_filter(cls, sub_word) -> list["Card"]: 
          """Returns all cards where the word, translation, or tip contain given sub_word"""
          pattern = f"%{sub_word}%"
          return (cls.query.filter(
                    or_(
                        cls.word.like(pattern),
                        cls.translation.like(pattern),
                        cls.tip.like(pattern)
                    )
                ).all()
            )
    
    @classmethod
    def card_update(cls, card_id, word: str = None, translation: str = None, tip:str = None) -> "Card": 
        """Looks for a card in the DB and updates its fields. Returns None if no card is found"""
        card = cls.query.get(card_id)
        if not card:
            return None
        
        card.word = word
        card.translation = translation
        card.tip = tip
        
        db.commit()
        return card
    
    @classmethod
    def card_delete_by_id(cls, card_id: int) -> bool:
        """Searches for a card in DB and removes it. Returns true if a card was found, false otherwise"""
        card = cls.query.get(card_id)
        if not card:
            return False
        
        db.session.delete(card_id)
        db.session.commit()
        return True

        
        