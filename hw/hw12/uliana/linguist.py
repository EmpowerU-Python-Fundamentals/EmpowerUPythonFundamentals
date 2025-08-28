from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Optional, List, Tuple


engine = create_engine("sqlite:///./linguist.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)


class Deck(Base):
    __tablename__ = "decks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    user_id = Column(Integer)


class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    word = Column(String)
    translation = Column(String)
    tip = Column(String)


Base.metadata.create_all(bind=engine)

def user_create(name: str, email: str, password: str) -> User:
    """
    Creates a new user and returns the User object.
    """
    db = SessionLocal()
    try:
        user = User(name=name, email=email, password=password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    finally:
        db.close()


def user_get_by_id(user_id: int) -> Optional[User]:
    """
    Retrieves a user by their ID and returns the User object.
    """
    db = SessionLocal()
    try:
        return db.query(User).filter(User.id == user_id).first()
    finally:
        db.close()


def user_update_name(user_id: int, name: str) -> Optional[User]:
    """
    Updates the name of a user and returns the User object.
    """
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            user.name = name
            db.commit()
            db.refresh(user)
        return user
    finally:
        db.close()


def user_change_password(user_id: int, old_password: str, new_password: str) -> bool:
    """
    Changes the password of a user and returns a Boolean value indicating success or failure.
    """
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user and user.password == old_password:
            user.password = new_password
            db.commit()
            return True
        return False
    finally:
        db.close()


def user_delete_by_id(user_id: int) -> bool:
    """
    Deletes a user by their ID and returns a Boolean value indicating success or failure.
    """
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
            return True
        return False
    finally:
        db.close()


def deck_create(name: str, user_id: int) -> Optional[Deck]:
    """
    Creates a new deck belonging to a user and returns the Deck object.
    """
    db = SessionLocal()
    try:
        if db.query(User).filter(User.id == user_id).first():
            deck = Deck(name=name, user_id=user_id)
            db.add(deck)
            db.commit()
            db.refresh(deck)
            return deck
        return None
    finally:
        db.close()


def deck_get_by_id(deck_id: int) -> Optional[Deck]:
    """
    Retrieves a deck by its ID and returns the Deck object.
    """
    db = SessionLocal()
    try:
        return db.query(Deck).filter(Deck.id == deck_id).first()
    finally:
        db.close()


def deck_update(deck_id: int, name: str) -> Optional[Deck]:
    """
    Updates the name of a deck and returns the Deck object.
    """
    db = SessionLocal()
    try:
        deck = db.query(Deck).filter(Deck.id == deck_id).first()
        if deck:
            deck.name = name
            db.commit()
            db.refresh(deck)
        return deck
    finally:
        db.close()


def deck_delete_by_id(deck_id: int) -> bool:
    """
    Deletes a deck by its ID and returns a Boolean value indicating success or failure.
    """
    db = SessionLocal()
    try:
        deck = db.query(Deck).filter(Deck.id == deck_id).first()
        if deck:
            db.delete(deck)
            db.commit()
            return True
        return False
    finally:
        db.close()



def card_create(user_id: int, word: str, translation: str, tip: str) -> Optional[Card]:
    """
    Creates a new flashcard and returns the Card object.
    """
    db = SessionLocal()
    try:
        if db.query(User).filter(User.id == user_id).first():
            card = Card(user_id=user_id, word=word, translation=translation, tip=tip)
            db.add(card)
            db.commit()
            db.refresh(card)
            return card
        return None
    finally:
        db.close()


def card_get_by_id(card_id: int) -> Optional[Card]:
    """
    Retrieves a flashcard by its ID and returns the Card object.
    """
    db = SessionLocal()
    try:
        return db.query(Card).filter(Card.id == card_id).first()
    finally:
        db.close()


def card_filter(sub_word: str) -> Tuple[Card, ...]:
    """
    Retrieves all flashcards containing a substring in either the word, translation, or tip fields and returns a tuple of Card objects.
    """
    db = SessionLocal()
    try:
        matches = db.query(Card).filter(
            (Card.word.contains(sub_word)) |
            (Card.translation.contains(sub_word)) |
            (Card.tip.contains(sub_word))
        ).all()
        return tuple(matches)
    finally:
        db.close()


def card_update(card_id: int, word: Optional[str] = None, translation: Optional[str] = None,
                tip: Optional[str] = None) -> Optional[Card]:
    """
    Updates the fields of a flashcard and returns the Card object.
    """
    db = SessionLocal()
    try:
        card = db.query(Card).filter(Card.id == card_id).first()
        if card:
            if word is not None:
                card.word = word
            if translation is not None:
                card.translation = translation
            if tip is not None:
                card.tip = tip
            db.commit()
            db.refresh(card)
        return card
    finally:
        db.close()


def card_delete_by_id(card_id: int) -> bool:
    """
    Deletes a flashcard by its ID and returns a Boolean value indicating success or failure.
    """
    db = SessionLocal()
    try:
        card = db.query(Card).filter(Card.id == card_id).first()
        if card:
            db.delete(card)
            db.commit()
            return True
        return False
    finally:
        db.close()