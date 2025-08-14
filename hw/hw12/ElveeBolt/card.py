from typing import Tuple

from database import SessionLocal, Card, User


def card_create(user_id: int, word: str, translation: str, tip: str) -> Card | None:
    with SessionLocal() as session:
        if not session.get(User, user_id):
            return None
        card = Card(user_id=user_id, word=word, translation=translation, tip=tip)
        session.add(card)
        session.commit()
        session.refresh(card)
        return card


def card_get_by_id(card_id: int) -> Card | None:
    with SessionLocal() as session:
        return session.get(Card, card_id)


def card_filter(sub_word: str) -> Tuple[Card, ...]:
    with SessionLocal() as session:
        like_pattern = f"%{sub_word}%"
        results = session.query(Card).filter(
            (Card.word.ilike(like_pattern)) |
            (Card.translation.ilike(like_pattern)) |
            (Card.tip.ilike(like_pattern))
        ).all()
        return tuple(results)


def card_update(card_id: int, word: str | None = None, translation: str | None = None, tip: str | None = None) -> Card | None:
    with SessionLocal() as session:
        card = session.get(Card, card_id)
        if not card:
            return None
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
    with SessionLocal() as session:
        card = session.get(Card, card_id)
        if not card:
            return False
        session.delete(card)
        session.commit()
        return True