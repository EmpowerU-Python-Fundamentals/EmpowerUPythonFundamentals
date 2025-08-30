from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, or_
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from typing import Tuple, Optional

Base = declarative_base()
_engine = None
_Session = None
session = None

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    decks = relationship("Deck", back_populates="user", cascade="all, delete-orphan")
    cards = relationship("Card", back_populates="user", cascade="all, delete-orphan")

class Deck(Base):
    __tablename__ = "decks"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="decks")

class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    word = Column(String, nullable=False)
    translation = Column(String, nullable=False)
    tip = Column(String, nullable=True)
    user = relationship("User", back_populates="cards")

def init_db(engine_url: str = "sqlite:///linguist.db"):
    """
    Initialize database engine and session. Call before using CRUD functions.
    """
    global _engine, _Session, session
    _engine = create_engine(engine_url, echo=False, future=True)
    _Session = sessionmaker(bind=_engine, future=True)
    session = _Session()
    Base.metadata.create_all(_engine)

def user_create(name: str, email: str, password: str) -> User:
    """
    Creates a new user and returns the User object.
    """
    u = User(name=name, email=email, password=password)
    session.add(u)
    session.commit()
    session.refresh(u)
    return u

def user_get_by_id(user_id: int) -> Optional[User]:
    """
    Retrieves a user by their ID and returns the User object or None.
    """
    return session.get(User, user_id)

def user_update_name(user_id: int, name: str) -> Optional[User]:
    """
    Updates the name of a user and returns the User object or None if not found.
    """
    u = session.get(User, user_id)
    if not u:
        return None
    u.name = name
    session.commit()
    session.refresh(u)
    return u

def user_change_password(user_id: int, old_password: str, new_password: str) -> bool:
    """
    Changes the password of a user and returns True on success, False otherwise.
    """
    u = session.get(User, user_id)
    if not u:
        return False
    if u.password != old_password:
        return False
    u.password = new_password
    session.commit()
    return True

def user_delete_by_id(user_id: int) -> bool:
    """
    Deletes a user by their ID and returns True if deleted, False otherwise.
    """
    u = session.get(User, user_id)
    if not u:
        return False
    session.delete(u)
    session.commit()
    return True

def deck_create(name: str, user_id: int) -> Deck:
    """
    Creates a new deck belonging to a user and returns the Deck object.
    """
    # ensure user exists
    u = session.get(User, user_id)
    if not u:
        raise ValueError("User not found")
    d = Deck(name=name, user_id=user_id)
    session.add(d)
    session.commit()
    session.refresh(d)
    return d

def deck_get_by_id(deck_id: int) -> Optional[Deck]:
    """
    Retrieves a deck by its ID and returns the Deck object or None.
    """
    return session.get(Deck, deck_id)

def deck_update(deck_id: int, name: str) -> Optional[Deck]:
    """
    Updates the name of a deck and returns the Deck object or None if not found.
    """
    d = session.get(Deck, deck_id)
    if not d:
        return None
    d.name = name
    session.commit()
    session.refresh(d)
    return d

def deck_delete_by_id(deck_id: int) -> bool:
    """
    Deletes a deck by its ID and returns True if deleted, False otherwise.
    """
    d = session.get(Deck, deck_id)
    if not d:
        return False
    session.delete(d)
    session.commit()
    return True

def card_create(user_id: int, word: str, translation: str, tip: str) -> Card:
    """
    Creates a new flashcard and returns the Card object.
    """
    u = session.get(User, user_id)
    if not u:
        raise ValueError("User not found")
    c = Card(user_id=user_id, word=word, translation=translation, tip=tip)
    session.add(c)
    session.commit()
    session.refresh(c)
    return c

def card_get_by_id(card_id: int) -> Optional[Card]:
    """
    Retrieves a flashcard by its ID and returns the Card object or None.
    """
    return session.get(Card, card_id)

def card_filter(sub_word: str) -> Tuple[Card, ...]:
    """
    Retrieves all flashcards containing a substring in word, translation, or tip (case-insensitive).
    Returns a tuple of Card objects.
    """
    q = session.query(Card).filter(
        or_(
            Card.word.ilike(f"%{sub_word}%"),
            Card.translation.ilike(f"%{sub_word}%"),
            Card.tip.ilike(f"%{sub_word}%")
        )
    )
    return tuple(q.all())

def card_update(card_id: int, word: Optional[str] = None, translation: Optional[str] = None, tip: Optional[str] = None) -> Optional[Card]:
    """
    Updates the fields of a flashcard and returns the Card object or None if not found.
    """
    c = session.get(Card, card_id)
    if not c:
        return None
    if word is not None:
        c.word = word
    if translation is not None:
        c.translation = translation
    if tip is not None:
        c.tip = tip
    session.commit()
    session.refresh(c)
    return c

def card_delete_by_id(card_id: int) -> bool:
    """
    Deletes a flashcard by its ID and returns True if deleted, False otherwise.
    """
    c = session.get(Card, card_id)
    if not c:
        return False
    session.delete(c)
    session.commit()
    return True
