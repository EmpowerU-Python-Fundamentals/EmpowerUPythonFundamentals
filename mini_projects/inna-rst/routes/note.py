from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from database import db
from models import User, Category, Note
from forms import NoteForm
from markupsafe import Markup
from functions import get_categories_with_notes_count

note= Blueprint("note", __name__)

@note.route("/notes/new", methods=["GET", "POST"])
@login_required
def create_note():
    form = NoteForm()
    categories = Category.query.filter_by(user_id=current_user.id).all()

    form.category.choices = [(0, "Без категорії")] + [
        (c.id, Markup(f"<i class='{c.icon}' style='color:{c.color}'></i> {c.name}")) for c in categories
    ]


    if form.validate_on_submit():
        note = Note(
            title=form.title.data,
            content=form.content.data,
            user_id=current_user.id,
            category_id=form.category.data if form.category.data != 0 else None
        )
        db.session.add(note)
        db.session.commit()
        flash("Нотатку створено!", "success")
        return redirect(url_for("main.dashboard"))
    return render_template("note/create_note.html", form=form, categories=categories)


@note.route("/notes/<int:note_id>/edit", methods=["GET", "POST"])
@login_required
def edit_note(note_id):
    note = Note.query.filter_by(id=note_id, user_id=current_user.id).first_or_404()
    categories = Category.query.filter_by(user_id=current_user.id).all()
    choices = [(0, "Без категорії")] + [
        (c.id, c.name) for c in categories
    ]
    form = NoteForm(obj=note)
    form.category.choices = choices

    # Создаем форму с данными из запроса или объекта
    # form = NoteForm(request.form, obj=note) if request.method == 'POST' else NoteForm(obj=note)
    #
    # # Всегда устанавливаем choices
    # form.category.choices = choices
    # Заполняем форму данными из объекта
    # form.process(obj=note)

    # Дополнительная проверка на случай, если category все равно None
    if form.category.data is None:
        form.category.data = note.category_id or 0

    if form.validate_on_submit():
        note.title = form.title.data
        note.content = form.content.data
        note.category_id = form.category.data if form.category.data != 0 else None
        db.session.commit()
        flash("Нотатку оновлено!", "success")
        return redirect(url_for("main.dashboard"))
    return render_template("note/edit_note.html", form=form, note=note, categories=categories)

@note.route("/notes/<int:id>/delete", methods=["POST"])
@login_required
def delete_note(id):
    note = Note.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    db.session.delete(note)
    db.session.commit()
    flash("Нотатку видалено.", "warning")
    return redirect(url_for("main.dashboard"))


@note.route("/notes/<int:id>/details", methods=["GET"])
@login_required
def note_details(id):
    note = Note.query.filter_by(id=id, user_id=current_user.id).first_or_404()

    return jsonify({
        'id': note.id,
        'title': note.title,
        'content': note.content,
        'category_id': note.category_id,
    })

@note.route("/notes/<int:id>/view", methods=["GET"])
@login_required
def note_view(id):
    note = Note.query.filter_by(id=id, user_id=current_user.id).first_or_404()

    # All categories for the current user
    categories = get_categories_with_notes_count(current_user.id)

    # Количество заметок без категории
    uncategorized_notes_count = Note.query.filter_by(
        user_id=current_user.id,
        category_id=None
    ).count()

    return render_template("note/note_item.html",
                           categories=categories,
                           uncategorized_notes_count=uncategorized_notes_count,
                           note=note,
                           active_category=note.category_id)