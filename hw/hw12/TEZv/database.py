from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Визначення базового класу для моделей SQLAlchemy
Base = declarative_base()

# Налаштування бази даних
engine = create_engine("sqlite:///linguist.db", echo=False)

# Створення фабрики сесій, яка буде створювати нові сесії для взаємодії з БД
SessionLocal = sessionmaker(bind=engine)

# ------------------------------------
#             Моделі (Models)
# ------------------------------------
class User(Base):
    """
    Модель користувача додатка.
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    decks = relationship("Deck", back_populates="user", cascade="all, delete-orphan")
    cards = relationship("Card", back_populates="user", cascade="all, delete-orphan")

class Deck(Base):
    """
    Модель колоди карток.
    """
    __tablename__ = "decks"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="decks")

class Card(Base):
    """
    Модель окремої флешкартки.
    """
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    word = Column(String, nullable=False)
    translation = Column(String, nullable=False)
    tip = Column(String)
    user = relationship("User", back_populates="cards")
    
# Створення таблиць у базі даних, якщо вони ще не існують
Base.metadata.create_all(engine)
