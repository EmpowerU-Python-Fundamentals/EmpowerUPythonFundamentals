from database import Deck, User, SessionLocal


def deck_create(name: str, user_id: int) -> Deck | None:
    with SessionLocal() as session:
        if not session.get(User, user_id):
            return None
        deck = Deck(name=name, user_id=user_id)
        session.add(deck)
        session.commit()
        session.refresh(deck)
        return deck


def deck_get_by_id(deck_id: int) -> Deck | None:
    with SessionLocal() as session:
        return session.get(Deck, deck_id)


def deck_update(deck_id: int, name: str) -> Deck | None:
    with SessionLocal() as session:
        deck = session.get(Deck, deck_id)
        if not deck:
            return None
        deck.name = name
        session.commit()
        session.refresh(deck)
        return deck


def deck_delete_by_id(deck_id: int) -> bool:
    with SessionLocal() as session:
        deck = session.get(Deck, deck_id)
        if not deck:
            return False
        session.delete(deck)
        session.commit()
        return True