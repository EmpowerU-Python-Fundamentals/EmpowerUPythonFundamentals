from datetime import datetime, UTC
from typing import Annotated
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Text, DateTime, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

from database import db

intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
created_at = Annotated[datetime, mapped_column(DateTime, default=lambda: datetime.now(UTC))]
updated_at = Annotated[datetime, mapped_column(DateTime,
                                               default=lambda: datetime.now(UTC),
                                               onupdate=lambda: datetime.now(UTC))]



class User(db.Model, UserMixin):
    __tablename__ = "users"

    id: Mapped[intpk]
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(256), nullable=False)

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    notes: Mapped[list["Note"]] = relationship("Note", back_populates="user", cascade="all, delete-orphan")
    categories: Mapped[list["Category"]] = relationship("Category", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<User {self.username}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Category(db.Model):
    __tablename__ = "categories"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    color: Mapped[str] = mapped_column(String(10), nullable=True)
    icon : Mapped[str] = mapped_column(String(10), default="bi-folder")

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    # Прив'язка до користувача
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="categories")

    # Зв'язок із замітками
    notes: Mapped[list["Note"]] = relationship("Note", back_populates="category", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Category {self.name}>"


class Note(db.Model):
    __tablename__ = "notes"

    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(String(200), nullable=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    # Прив'язка до категорії (може бути NULL)
    category_id: Mapped[int | None] = mapped_column(ForeignKey("categories.id"), nullable=True)
    category: Mapped["Category"] = relationship("Category", back_populates="notes")

    # Прив'язка до користувача
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="notes")

    def __repr__(self) -> str:
        return f"<Note {self.title}>"
