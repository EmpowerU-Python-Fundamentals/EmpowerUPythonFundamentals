from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///linguist.db", echo=False)
Session = sessionmaker(bind=engine, expire_on_commit=False)


class User(Base):
    """App user with their own decks and cards."""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    decks = relationship("Deck", back_populates="user", cascade="all, delete-orphan")
    cards = relationship("Card", back_populates="user", cascade="all, delete-orphan")


class Deck(Base):
    """A deck of cards owned by the user."""
    __tablename__ = "decks"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="decks")


class Card(Base):
    """A separate card with a word, translation and a hint."""
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    word = Column(String)
    translation = Column(String)
    tip = Column(String)

    user = relationship("User", back_populates="cards")


Base.metadata.create_all(engine)


# ------------------------- CRUD functions -------------------------
def user_create(name, email, password):
    """Create a new user."""
    s = Session()
    u = User(name=name, email=email, password=password)
    s.add(u)
    s.commit()
    return u


def user_get_by_id(user_id):
    """Returns the user by their ID."""
    s = Session()
    return s.get(User, user_id)


def user_update_name(user_id, name):
    """Updates the username."""
    s = Session()
    u = s.get(User, user_id)
    if u:
        u.name = name
        s.commit()
    return u


def user_change_password(user_id, old_password, new_password):
    """Changes the user's password if the old one matches."""
    s = Session()
    u = s.get(User, user_id)
    if u and u.password == old_password:
        u.password = new_password
        s.commit()
        return True
    return False


def user_delete_by_id(user_id):
    """Deletes a user by ID."""
    s = Session()
    u = s.get(User, user_id)
    if u:
        s.delete(u)
        s.commit()
        return True
    return False


def deck_create(name, user_id):
    """Creates a new deck for the user."""
    s = Session()
    d = Deck(name=name, user_id=user_id)
    s.add(d)
    s.commit()
    return d


def deck_get_by_id(deck_id):
    """Returns a deck by its ID."""
    s = Session()
    return s.get(Deck, deck_id)


def deck_update(deck_id, name):
    """Updates the deck name."""
    s = Session()
    d = s.get(Deck, deck_id)
    if d:
        d.name = name
        s.commit()
    return d


def deck_delete_by_id(deck_id):
    """Deletes a deck by its ID."""
    s = Session()
    d = s.get(Deck, deck_id)
    if d:
        s.delete(d)
        s.commit()
        return True
    return False


def card_create(user_id, word, translation, tip):
    """Creates a new card."""
    s = Session()
    c = Card(user_id=user_id, word=word, translation=translation, tip=tip)
    s.add(c)
    s.commit()
    return c


def card_get_by_id(card_id):
    """Returns the card by its ID."""
    s = Session()
    return s.get(Card, card_id)


def card_filter(sub_word):
    """Searches for cards by order in a word, translation, or clue."""
    s = Session()
    q = f"%{sub_word.lower()}%"
    return s.query(Card).filter(
        (Card.word.ilike(q)) |
        (Card.translation.ilike(q)) |
        (Card.tip.ilike(q))
    ).all()


def card_update(card_id, word=None, translation=None, tip=None):
    """Updates card data (word, translation, hint)."""
    s = Session()
    c = s.get(Card, card_id)
    if c:
        if word: c.word = word
        if translation: c.translation = translation
        if tip: c.tip = tip
        s.commit()
    return c


def card_delete_by_id(card_id):
    """Deletes a card by its ID."""
    s = Session()
    c = s.get(Card, card_id)
    if c:
        s.delete(c)
        s.commit()
        return True
    return False
