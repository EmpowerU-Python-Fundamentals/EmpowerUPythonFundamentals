from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Database setup
engine = create_engine("sqlite:///linguist.db", echo=True)  # SQLite для простоти
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    decks = relationship("Deck", back_populates="user", cascade="all, delete")
    cards = relationship("Card", back_populates="user", cascade="all, delete")

class Deck(Base):
    __tablename__ = "decks"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="decks")

class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    word = Column(String, nullable=False)
    translation = Column(String, nullable=False)
    tip = Column(String)
    user = relationship("User", back_populates="cards")

# Create tables
Base.metadata.create_all(engine)

# CRUD functions
# User
def user_create(name, email, password):
    user = User(name=name, email=email, password=password)
    session.add(user)
    session.commit()
    return user

def user_get_by_id(user_id):
    return session.query(User).get(user_id)

def user_update_name(user_id, name):
    user = user_get_by_id(user_id)
    if user:
        user.name = name
        session.commit()
    return user

def user_change_password(user_id, old_password, new_password):
    user = user_get_by_id(user_id)
    if user and user.password == old_password:
        user.password = new_password
        session.commit()
        return True
    return False

def user_delete_by_id(user_id):
    user = user_get_by_id(user_id)
    if user:
        session.delete(user)
        session.commit()
        return True
    return False

# Deck
def deck_create(name, user_id):
    deck = Deck(name=name, user_id=user_id)
    session.add(deck)
    session.commit()
    return deck

def deck_get_by_id(deck_id):
    return session.query(Deck).get(deck_id)

def deck_update(deck_id, name):
    deck = deck_get_by_id(deck_id)
    if deck:
        deck.name = name
        session.commit()
    return deck

def deck_delete_by_id(deck_id):
    deck = deck_get_by_id(deck_id)
    if deck:
        session.delete(deck)
        session.commit()
        return True
    return False

# Card
def card_create(user_id, word, translation, tip):
    card = Card(user_id=user_id, word=word, translation=translation, tip=tip)
    session.add(card)
    session.commit()
    return card

def card_get_by_id(card_id):
    return session.query(Card).get(card_id)

def card_filter(sub_word):
    return tuple(session.query(Card).filter(
        (Card.word.ilike(f"%{sub_word}%")) |
        (Card.translation.ilike(f"%{sub_word}%")) |
        (Card.tip.ilike(f"%{sub_word}%"))
    ).all())

def card_update(card_id, word=None, translation=None, tip=None):
    card = card_get_by_id(card_id)
    if card:
        if word: card.word = word
        if translation: card.translation = translation
        if tip: card.tip = tip
        session.commit()
    return card

def card_delete_by_id(card_id):
    card = card_get_by_id(card_id)
    if card:
        session.delete(card)
        session.commit()
        return True
    return False