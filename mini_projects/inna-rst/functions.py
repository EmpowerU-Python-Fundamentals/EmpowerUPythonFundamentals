from sqlalchemy import func
from models import Note, Category
from database import db

def get_categories_with_notes_count(user_id):
    categories = db.session.query(
        Category,
        func.count(Note.id).label('notes_count')
    ).outerjoin(Note, Category.id == Note.category_id) \
        .filter(Category.user_id == user_id) \
        .group_by(Category.id) \
        .order_by(Category.name.asc()) \
        .all()

    return categories