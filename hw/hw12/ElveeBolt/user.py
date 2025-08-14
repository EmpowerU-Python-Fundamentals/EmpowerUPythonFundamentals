from database import User, SessionLocal


def user_create(name: str, email: str, password: str) -> User:
    with SessionLocal() as session:
        user = User(name=name, email=email, password=password)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user


def user_get_by_id(user_id: int) -> User | None:
    with SessionLocal() as session:
        return session.get(User, user_id)


def user_update_name(user_id: int, name: str) -> User | None:
    with SessionLocal() as session:
        user = session.get(User, user_id)
        if not user:
            return None
        user.name = name
        session.commit()
        session.refresh(user)
        return user


def user_change_password(user_id: int, old_password: str, new_password: str) -> bool:
    with SessionLocal() as session:
        user = session.get(User, user_id)
        if not user or user.password != old_password:
            return False
        user.password = new_password
        session.commit()
        return True


def user_delete_by_id(user_id: int) -> bool:
    with SessionLocal() as session:
        user = session.get(User, user_id)
        if not user:
            return False
        session.delete(user)
        session.commit()
        return True