from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ColorField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo

class RegisterForm(FlaskForm):
    username = StringField("Им'я користувача", validators=[DataRequired(message="Будь ласка, введіть ім'я"), Length(min=3, max=50)])
    password = PasswordField('Пароль', validators=[DataRequired(message="Введіть пароль"), Length(min=6)])
    confirm_password = PasswordField('Підтвердьте пароль', validators=[DataRequired(message="Підтвердіть пароль"), EqualTo("password", message="Паролі не співпадають")])
    submit = SubmitField('Реєстрація')

class LoginForm(FlaskForm):
    username = StringField("Им'я користувача", validators=[DataRequired(message="Будь ласка, введіть ім'я"), Length(min=3, max=50)])
    password = PasswordField('Пароль', validators=[DataRequired(message="Введіть пароль")])
    remember = BooleanField("Запам'ятати мене")
    submit = SubmitField('Увійти')

class CategoryForm(FlaskForm):
    name = StringField("Назва", validators=[DataRequired(), Length(min=2, max=100)])
    # Чекбокс для увімкнення/вимкнення кольору
    enable_color = BooleanField("Використати колір для категорії", default=False)
    color = ColorField("Колір", default="#6c757d")

    icon = SelectField("Іконка", choices=[
        ("bi-folder", "Папка"),
        ("bi-journal", "Журнал"),
        ("bi-star", "Зірка"),
        ("bi-bookmark", "Закладка"),
        ("bi-list-task", "Список задач"),
        ("bi-briefcase", "Робота"),
        ("bi-house", "Дім"),
        ("bi-heart", "Серце"),
        ("bi-book", "Книга"),
        ("bi-camera", "Камера"),
        ("bi-music-note", "Музика"),
        ("bi-airplane", "Подорожі"),
        ("bi-cart", "Покупки"),
        ("bi-currency-dollar", "Фінанси"),
        ("bi-person-arms-up", "Спорт"),
        ("bi-cup-hot", "Кафе"),
        ("bi-palette", "Творчість"),
        ("bi-gear", "Налаштування")
    ])
    submit = SubmitField("Зберегти")


class NoteForm(FlaskForm):
    title = StringField(
        "Назва нотатки",
        validators=[DataRequired(message="Введіть назву"), Length(min=3, max=200)],
        render_kw={"placeholder": "Наприклад: Ідеї для проекту"}
    )
    content = TextAreaField(
        "Текст нотатки",
        render_kw={"rows": 6, "placeholder": "Введіть ваш текст сюди..."}
    )
    category = SelectField("Категорія", coerce=int)
    submit = SubmitField("Зберегти")