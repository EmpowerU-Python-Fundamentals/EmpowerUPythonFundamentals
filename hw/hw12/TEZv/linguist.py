from typing import Optional, Tuple
# Правильний рядок імпорту
from database import SessionLocal, User, Deck, Card
from sqlalchemy import func

# ------------------------------------
#             Функції (CRUD)
# ------------------------------------
def user_create(name: str, email: str, password: str) -> User:
    """Створює нового користувача та повертає його об'єкт."""
    with SessionLocal() as session:
        new_user = User(name=name, email=email, password=password)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user

def user_get_by_id(user_id: int) -> Optional[User]:
    """Отримує користувача за його ID."""
    with SessionLocal() as session:
        return session.get(User, user_id)

def user_update_name(user_id: int, name: str) -> Optional[User]:
    """Оновлює ім'я користувача."""
    with SessionLocal() as session:
        user = session.get(User, user_id)
        if user:
            user.name = name
            session.commit()
            session.refresh(user)
        return user

def user_change_password(user_id: int, old_password: str, new_password: str) -> bool:
    """Змінює пароль користувача, якщо старий пароль вірний."""
    with SessionLocal() as session:
        user = session.get(User, user_id)
        if user and user.password == old_password:
            user.password = new_password
            session.commit()
            return True
        return False

def user_delete_by_id(user_id: int) -> bool:
    """Видаляє користувача за його ID."""
    with SessionLocal() as session:
        user = session.get(User, user_id)
        if user:
            session.delete(user)
            session.commit()
            return True
        return False

def deck_create(name: str, user_id: int) -> Deck:
    """Створює нову колоду, що належить користувачеві."""
    with SessionLocal() as session:
        new_deck = Deck(name=name, user_id=user_id)
        session.add(new_deck)
        session.commit()
        session.refresh(new_deck)
        return new_deck

def deck_get_by_id(deck_id: int) -> Optional[Deck]:
    """Отримує колоду за її ID."""
    with SessionLocal() as session:
        return session.get(Deck, deck_id)

def deck_update(deck_id: int, name: str) -> Optional[Deck]:
    """Оновлює ім'я колоди."""
    with SessionLocal() as session:
        deck = session.get(Deck, deck_id)
        if deck:
            deck.name = name
            session.commit()
            session.refresh(deck)
        return deck

def deck_delete_by_id(deck_id: int) -> bool:
    """Видаляє колоду за її ID."""
    with SessionLocal() as session:
        deck = session.get(Deck, deck_id)
        if deck:
            session.delete(deck)
            session.commit()
            return True
        return False

def card_create(user_id: int, word: str, translation: str, tip: str) -> Card:
    """Створює нову картку."""
    with SessionLocal() as session:
        new_card = Card(user_id=user_id, word=word, translation=translation, tip=tip)
        session.add(new_card)
        session.commit()
        session.refresh(new_card)
        return new_card

def card_get_by_id(card_id: int) -> Optional[Card]:
    """Отримує картку за її ID."""
    with SessionLocal() as session:
        return session.get(Card, card_id)

def card_filter(sub_word: str) -> Tuple[Card, ...]:
    """
    Фільтрує картки за наявністю підрядка в слові, перекладі або підказці.
    Повертає кортеж знайдених об'єктів Card.
    """
    with SessionLocal() as session:
        like_pattern = f"%{sub_word}%"
        # Використовуємо func.lower для коректного порівняння без урахування регістру
        query = session.query(Card).filter(
            (func.lower(Card.word).like(func.lower(like_pattern))) |
            (func.lower(Card.translation).like(func.lower(like_pattern))) |
            (func.lower(Card.tip).like(func.lower(like_pattern)))
        )
        return tuple(query.all())

def card_update(card_id: int, word: Optional[str] = None, translation: Optional[str] = None, tip: Optional[str] = None) -> Optional[Card]:
    """Оновлює поля картки."""
    with SessionLocal() as session:
        card = session.get(Card, card_id)
        if card:
            if word is not None:
                card.word = word
            if translation is not None:
                card.translation = translation
            if tip is not None:
                card.tip = tip
            session.commit()
            session.refresh(card)
        return card

def card_delete_by_id(card_id: int) -> bool:
    """Видаляє картку за її ID."""
    with SessionLocal() as session:
        card = session.get(Card, card_id)
        if card:
            session.delete(card)
            session.commit()
            return True
        return False
