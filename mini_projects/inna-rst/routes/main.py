from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_required

from sqlalchemy.orm import joinedload
from models import Note
from functions import get_categories_with_notes_count

main = Blueprint("main", __name__)


@main.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    return render_template("main/info.html")


@main.route("/dashboard")
@login_required
def dashboard():
    user_id = current_user.id

    # All categories for the current user
    categories = get_categories_with_notes_count(current_user.id)

    uncategorized_notes_count = Note.query.filter_by(
        user_id=current_user.id,
        category_id=None
    ).count()

    # Параметри пагінації
    page = request.args.get('page', 1, type=int)
    per_page = 6  # кількість записів на сторінку

    # query-parametr (?category=ID)
    category_id = request.args.get("category", type=int)
    query = Note.query.options(joinedload(Note.category)).filter_by(user_id=user_id).order_by(Note.updated_at.desc())

    if category_id is not None:  # означає параметр є в URL
        if category_id == 0:
            # Усі нотатки без категорії
            query = query.filter(Note.category_id.is_(None))
        else:
            # Нотатки конкретної категорії
            query = query.filter_by(category_id=category_id)

    notes_pagination = query.paginate(
        page=page,
        per_page=per_page,
        error_out=False  # не выдавать ошибку 404 при неверной странице
    )

    notes = notes_pagination.items

    # notes = query.all()

    if not notes and not categories and uncategorized_notes_count == 0:
        return render_template("dashboard/empty_dashboard.html")

    return render_template("dashboard/dashboard.html",
                           categories=categories,
                           uncategorized_notes_count=uncategorized_notes_count,
                           notes=notes,
                           pagination=notes_pagination,
                           active_category=category_id)
