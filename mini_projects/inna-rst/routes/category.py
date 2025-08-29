from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from database import db
from models import User, Category, Note
from forms import CategoryForm


category = Blueprint("category", __name__)

@category.route("/categories/new", methods=["GET", "POST"])
@login_required
def create_category():
    form = CategoryForm()
    if form.validate_on_submit():
        color = form.color.data if form.enable_color.data else None

        category = Category(
            name=form.name.data,
            color=color,
            icon=form.icon.data,
            user_id=current_user.id
        )
        db.session.add(category)
        db.session.commit()

        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            # ответ для AJAX
            return jsonify({
                "id": category.id,
                "name": category.name,
                "color": category.color,
                "icon": category.icon
            })

        # обычная форма → редирект
        flash("Категорію створено!", "success")
        return redirect(url_for("main.dashboard"))

    return render_template("category/create_category.html", form=form)


@category.route("/categories/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_category(id):
    category = Category.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    form = CategoryForm(obj=category)

    if request.method == 'GET' and category:
        # Заповнюємо форму даними категорії
        form.name.data = category.name
        form.enable_color.data = bool(category.color)  # True если есть цвет
        form.color.data = category.color or '#6c757d'
        category.icon = category.icon

    if form.validate_on_submit():
        if not category:
            category = Category()

        category.name = form.name.data
        category.color = form.color.data if form.enable_color.data else None
        category.icon = form.icon.data

        db.session.commit()
        flash("Категорію оновлено!", "success")
        return redirect(url_for("main.index"))
    return render_template("category/edit_category.html", form=form, category=category)


@category.route("/categories/<int:id>/delete", methods=["POST"])
@login_required
def delete_category(id):
    category = Category.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    db.session.delete(category)
    db.session.commit()
    flash("Категорію видалено.", "warning")
    return redirect(url_for("main.dashboard"))


@category.route("/categories/<int:id>/details", methods=["GET"])
@login_required
def category_details(id):
    category = Category.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    notes_count = Note.query.filter_by(category_id=category.id).count()

    return jsonify({
        'id': category.id,
        'name': category.name,
        'color': category.color,
        'icon': category.icon,
        'notes_count': notes_count
    })