from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from database import db
from models import User
from forms import LoginForm, RegisterForm


auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            flash("Вхід успішний!", "success")
            next_page = request.args.get("next")
            return redirect(next_page or url_for("main.index"))
        else:
            flash("Недійсне ім'я користувача або пароль.", "danger")
    return render_template("user/login.html", form=form)

@auth.route("/registration", methods=["GET", "POST"])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = RegisterForm()

    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash("Обліковий запис успішно створено! Тепер ви можете увійти.", "success")
            return redirect(url_for("auth.login"))
        except Exception as e:
            db.session.rollback()
            flash("При реєстрації виникла помилка", "danger")
            print(e)


    return render_template("user/registration.html", form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Ви вийшли з системи.", "info")
    return redirect(url_for("auth.login"))