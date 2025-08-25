from typing import Optional, Tuple
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.exc import NoResultFound

Base = declarative_base()

# -------------------
# Database setup
# -------------------
engine = create_engine("sqlite:///linguist.db", echo=False)
SessionLocal = sessionmaker(bind=engine)


# -------------------
# Models
# -------------------
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
    tip = Column(String)

    user = relationship("User", back_populates="cards")


# -------------------
# CRUD Functions
# -------------------
def user_create(name: str, email: str, password: str) -> User:
    """Creates a new user and returns the User object."""
    session = SessionLocal()
    user = User(name=name, email=email, password=password)
    session.add(user)
    session.commit()
    session.refresh(user)
    session.close()
    return user


def user_get_by_id(user_id: int) -> Optional[User]:
    """Retrieves a user by their ID."""
    session = SessionLocal()
    user = session.get(User, user_id)
    session.close()
    return user


def user_update_name(user_id: int, name: str) -> Optional[User]:
    """Updates the name of a user."""
    session = SessionLocal()
    user = session.get(User, user_id)
    if not user:
        session.close()
        return None
    user.name = name
    session.commit()
    session.refresh(user)
    session.close()
    return user


def user_change_password(user_id: int, old_password: str, new_password: str) -> bool:
    """Changes the password of a user."""
    session = SessionLocal()
    user = session.get(User, user_id)
    if not user or user.password != old_password:
        session.close()
        return False
    user.password = new_password
    session.commit()
    session.close()
    return True


def user_delete_by_id(user_id: int) -> bool:
    """Deletes a user by ID."""
    session = SessionLocal()
    user = session.get(User, user_id)
    if not user:
        session.close()
        return False
    session.delete(user)
    session.commit()
    session.close()
    return True


def deck_create(name: str, user_id: int) -> Deck:
    """Creates a new deck for a user."""
    session = SessionLocal()
    deck = Deck(name=name, user_id=user_id)
    session.add(deck)
    session.commit()
    session.refresh(deck)
    session.close()
    return deck


def deck_get_by_id(deck_id: int) -> Optional[Deck]:
    """Retrieves a deck by ID."""
    session = SessionLocal()
    deck = session.get(Deck, deck_id)
    session.close()
    return deck


def deck_update(deck_id: int, name: str) -> Optional[Deck]:
    """Updates a deck name."""
    session = SessionLocal()
    deck = session.get(Deck, deck_id)
    if not deck:
        session.close()
        return None
    deck.name = name
    session.commit()
    session.refresh(deck)
    session.close()
    return deck


def deck_delete_by_id(deck_id: int) -> bool:
    """Deletes a deck by ID."""
    session = SessionLocal()
    deck = session.get(Deck, deck_id)
    if not deck:
        session.close()
        return False
    session.delete(deck)
    session.commit()
    session.close()
    return True


def card_create(user_id: int, word: str, translation: str, tip: str) -> Card:
    """Creates a new flashcard."""
    session = SessionLocal()
    card = Card(user_id=user_id, word=word, translation=translation, tip=tip)
    session.add(card)
    session.commit()
    session.refresh(card)
    session.close()
    return card


def card_get_by_id(card_id: int) -> Optional[Card]:
    """Retrieves a flashcard by ID."""
    session = SessionLocal()
    card = session.get(Card, card_id)
    session.close()
    return card


def card_filter(sub_word: str) -> Tuple[Card]:
    """Finds cards containing a substring in word, translation, or tip."""
    session = SessionLocal()
    query = session.query(Card).filter(
        (Card.word.contains(sub_word)) |
        (Card.translation.contains(sub_word)) |
        (Card.tip.contains(sub_word))
    )
    results = tuple(query.all())
    session.close()
    return results


def card_update(card_id: int, word: str = None, translation: str = None, tip: str = None) -> Optional[Card]:
    """Updates fields of a flashcard."""
    session = SessionLocal()
    card = session.get(Card, card_id)
    if not card:
        session.close()
        return None
    if word is not None:
        card.word = word
    if translation is not None:
        card.translation = translation
    if tip is not None:
        card.tip = tip
    session.commit()
    session.refresh(card)
    session.close()
    return card


def card_delete_by_id(card_id: int) -> bool:
    """Deletes a flashcard by ID."""
    session = SessionLocal()
    card = session.get(Card, card_id)
    if not card:
        session.close()
        return False
    session.delete(card)
    session.commit()
    session.close()
    return True


# -------------------
# Create DB
# -------------------
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Database & tables created!")
