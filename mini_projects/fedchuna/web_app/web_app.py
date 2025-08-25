import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from markupsafe import escape
from sqlalchemy import create_engine, text
from werkzeug.security import generate_password_hash, check_password_hash 


DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


def sql_connection(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME):
    DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    try:
        engine = create_engine(DATABASE_URL, echo=True, connect_args={'options': '-c client_encoding=utf8'})
        return engine
    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None

@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route('/index', methods=['GET', 'POST'])
def index():

    if session.get('logged_in'):

        return redirect(url_for('user_page', email=escape(session['email'])))

    if request.method == 'POST':
        button_name = request.form.get('button')
        if button_name == 'login':
            return redirect(url_for('login'))
        elif button_name == 'register':
            return redirect(url_for('register'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if session.get('logged_in'):
        return redirect(url_for('user_page', email=escape(session['email'])))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(f"Попытка входа: email={email}, password={'*' * len(password)}") 
        
        if not email or not password:
            flash("Пожалуйста, введите Email и Пароль.", "error")
            return redirect(url_for('login'))

        connect_sql = sql_connection(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
        if not connect_sql:
            flash("Ошибка подключения к базе данных! Пожалуйста, повторите попытку позже.", "error")
            return redirect(url_for('login'))

        with connect_sql.connect() as connection:
            query = text("SELECT password, username FROM users WHERE email = :email")
            result = connection.execute(query, {"email": email}).fetchone()

            if result:
                stored_hashed_password = result[0] 
                username = result[1]
                

                if check_password_hash(stored_hashed_password, password):
                    session['logged_in'] = True
                    session['email'] = email
                    session['username'] = username

                    flash(f"Вход для пользователя: {escape(email)} выполнен успешно!", "success")
                    print(f"Вход для пользователя: {escape(email)} выполнен успешно!")
                    return redirect(url_for('user_page', email=escape(email)))
                else:
                    flash("Неверный email или пароль.", "error")
                    print("Неверный пароль.")
            else:
                flash("Неверный email или пароль.", "error")
                print(f"Пользователь с email {email} не найден.")
        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():

    if session.get('logged_in'):
        return redirect(url_for('user_page', email=escape(session['email'])))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        username = request.form.get('username')
        confirm_password = request.form.get('confirm_password')
        number = request.form.get('number')
        city = request.form.get('city')
        address = request.form.get('address')


        if not all([email, password, username, confirm_password, number, city, address]):
            flash("Все поля обязательны для заполнения!", "error")
            return redirect(url_for('register'))

        if password != confirm_password:
            flash("Пароли не совпадают!", "error")
            return redirect(url_for('register'))
        elif len(password) < 6:
            flash("Пароль должен быть не менее 6 символов!", "error")
            return redirect(url_for('register'))
        elif '@' not in email or '.' not in email.split('@')[-1]:
            flash("Пожалуйста, введите корректный адрес электронной почты!", "error")
            return redirect(url_for('register'))
        elif len(username) < 3:
            flash("Имя пользователя должно быть не менее 3 символов!", "error")
            return redirect(url_for('register'))
        elif len(username) > 20:
            flash("Имя пользователя должно быть не более 20 символов!", "error")
            return redirect(url_for('register'))

        elif password.isalpha() or password.isdigit():
            flash("Пароль должен содержать как буквы, так и цифры/спецсимволы!", "warning")
            return redirect(url_for('register'))

        try:
            connect_sql = sql_connection(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
            if not connect_sql:
                flash("Ошибка подключения к базе данных! Пожалуйста, повторите попытку позже.", "error")
                return redirect(url_for('register'))

            with connect_sql.connect() as connection:
                query = text("SELECT email FROM users WHERE email = :email")
                result = connection.execute(query, {"email": email}).fetchone()
                if result:
                    flash(f"Пользователь с email {escape(email)} уже существует!", "warning")
                    return redirect(url_for('register'))

                hashed_password = generate_password_hash(password)

                query = text("INSERT INTO users (email, password, username, number, city, address) VALUES (:email, :password, :username, :number, :city, :address)")
                connection.execute(query,
                                   {"email": email, "password": hashed_password, "username": username,
                                    "number": number, "city": city, "address": address})
                connection.commit()

            session['logged_in'] = True
            session['email'] = email
            session['username'] = username
            flash(f"Регистрация для пользователя: {escape(email)} выполнена успешно!", "success")
            print(f"Регистрация для пользователя: {escape(email)} выполнена успешно!")
            return redirect(url_for('user_page', email=escape(email)))
        except Exception as e:
            flash(f"Ошибка регистрации: {e}", "error")
            print(f"Ошибка регистрации: {e}")
            return redirect(url_for('register'))

    return render_template('register.html')

@app.route('/user_page/<email>')
def user_page(email):
    if not session.get('logged_in') or session.get('email') != email:
        flash("Вы не авторизованы или пытаетесь получить доступ к чужой странице!", "error")
        return redirect(url_for('index'))
    try:
        connect_sql = sql_connection(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
        if not connect_sql:
            flash("Ошибка подключения к базе данных! Пожалуйста, повторите попытку позже.", "error")
            return redirect(url_for('index'))

        with connect_sql.connect() as connection:
            query = text("SELECT email, username, number, city, address FROM users WHERE email = :email")
            result = connection.execute(query, {"email": email}).fetchone()
            if result:
                user_data = {
                    'email': result.email,
                    'username': result.username,
                    'number': result.number,
                    'city': result.city,
                    'address': result.address
                }
                return render_template('user_page.html', user_data=user_data)
            else:

                flash("Не вдалося знайти дані користувача. Будь ласка, увійдіть знову.", "error")
                session.clear()
                return redirect(url_for('index'))

    except Exception as e:
        flash(f"Ошибка получения данных пользователя: {e}", "error")
        print(f"Ошибка получения данных пользователя: {e}")
        return redirect(url_for('index'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    if not session.get('logged_in'):
        flash("Ви не авторизовані для доступу до цієї сторінки.", "error")
        return redirect(url_for('index'))

    if request.method == 'GET':
        return render_template('search.html', users_data=[], search_query="")
    elif request.method == 'POST':
        button_name = request.form.get('button')
        if button_name == 'user_page':
            return redirect(url_for('user_page', email=escape(session['email'])))

    try:
        search_query = request.form.get('search_query', '').strip()
        if not search_query:
            flash("Будь ласка, введіть запит для пошуку.", "warning")
            return render_template('search.html', users_data=[], search_query="")

        users_data = []
        connect_sql = sql_connection(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
        if not connect_sql:
            flash("Помилка підключення до бази даних! Будь ласка, спробуйте пізніше.", "error")
            return redirect(url_for('search'))

        with connect_sql.connect() as connection:
            like_query = f"%{search_query}%"
            query = text("SELECT username, email, number, city, address FROM users WHERE email LIKE :like_query OR username LIKE :like_query")
            results = connection.execute(query, {"like_query": like_query}).fetchall()

            if results:
                users_data = [dict(row._mapping) for row in results]
            else:
                flash(f"Користувачів за запитом '{escape(search_query)}' не знайдено.", "info")
    
        return render_template('search.html', users_data=users_data, search_query=search_query)

    except Exception as e:
        flash(f"Під час пошуку сталася несподівана помилка: {e}", "error")
        print(f"Search Error: {e}")
        return render_template('search.html', users_data=[], search_query=request.form.get('search_query', ''))




@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    flash("Ви успішно вийшли з системи.", "success")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
