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

    # Количество заметок без категории
    uncategorized_notes_count = Note.query.filter_by(
        user_id=current_user.id,
        category_id=None
    ).count()


    # query-parametr (?category=ID)
    category_id = request.args.get("category", type=int)

    if category_id:
        notes = Note.query.options(joinedload(Note.category)) \
            .filter_by(user_id=user_id, category_id=category_id) \
            .all()
    else:
        notes = Note.query.options(joinedload(Note.category)) \
            .filter_by(user_id=user_id) \
            .all()

    if not notes and not categories:
        return render_template("dashboard/empty_dashboard.html")


    return render_template("dashboard/dashboard.html",
                           categories=categories,
                           uncategorized_notes_count=uncategorized_notes_count,
                           notes=notes,
                           active_category=category_id)