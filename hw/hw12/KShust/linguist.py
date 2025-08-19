from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///linguist.db", echo=False)
Session = sessionmaker(bind=engine, expire_on_commit=False)

# ------------------- Models -------------------

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    decks = relationship("Deck", back_populates="user", cascade="all, delete-orphan")
    cards = relationship("Card", back_populates="user", cascade="all, delete-orphan")

class Deck(Base):
    __tablename__ = "decks"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="decks")
    cards = relationship("Card", back_populates="deck", cascade="all, delete-orphan")

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    deck_id = Column(Integer, ForeignKey("decks.id"))
    word = Column(String)
    translation = Column(String)
    tip = Column(String)

    user = relationship("User", back_populates="cards")
    deck = relationship("Deck", back_populates="cards")

Base.metadata.create_all(engine)

# ------------------- CRUD User -------------------

def user_create(name, email, password):
    session = Session()
    new_user = User(name=name, email=email, password=password)
    session.add(new_user)
    session.commit()
    return new_user

def user_get_by_id(user_id):
    session = Session()
    return session.get(User, user_id)

def user_update_name(user_id, new_name):
    session = Session()
    user = session.get(User, user_id)
    if user:
        user.name = new_name
        session.commit()
    return user

def user_change_password(user_id, old_password, new_password):
    session = Session()
    user = session.get(User, user_id)
    if user and user.password == old_password:
        user.password = new_password
        session.commit()
        return True
    return False

def user_delete_by_id(user_id):
    session = Session()
    user = session.get(User, user_id)
    if user:
        session.delete(user)
        session.commit()
        return True
    return False

# ------------------- CRUD Deck -------------------

def deck_create(name, user_id):
    session = Session()
    new_deck = Deck(name=name, user_id=user_id)
    session.add(new_deck)
    session.commit()
    return new_deck

def deck_get_by_id(deck_id):
    session = Session()
    return session.get(Deck, deck_id)

def deck_update(deck_id, new_name):
    session = Session()
    deck = session.get(Deck, deck_id)
    if deck:
        deck.name = new_name
        session.commit()
    return deck

def deck_delete_by_id(deck_id):
    session = Session()
    deck = session.get(Deck, deck_id)
    if deck:
        session.delete(deck)
        session.commit()
        return True
    return False

# ------------------- CRUD Card -------------------

def card_create(user_id, deck_id, word, translation, tip):
    session = Session()
    new_card = Card(user_id=user_id, deck_id=deck_id, word=word, translation=translation, tip=tip)
    session.add(new_card)
    session.commit()
    return new_card

def card_get_by_id(card_id):
    session = Session()
    return session.get(Card, card_id)

def card_filter(sub_word):
    session = Session()
    search_pattern = f"%{sub_word.lower()}%"
    return session.query(Card).filter(
        (Card.word.ilike(search_pattern)) |
        (Card.translation.ilike(search_pattern)) |
        (Card.tip.ilike(search_pattern))
    ).all()

def card_update(card_id, word=None, translation=None, tip=None):
    session = Session()
    card = session.get(Card, card_id)
    if card:
        if word:
            card.word = word
        if translation:
            card.translation = translation
        if tip:
            card.tip = tip
        session.commit()
    return card

def card_delete_by_id(card_id):
    session = Session()
    card = session.get(Card, card_id)
    if card:
        session.delete(card)
        session.commit()
        return True
    return False