from flask import Flask
from flask_login import LoginManager
from database import db
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    migrate = Migrate(app, db)

    app.config['SECRET_KEY'] = 'your secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes_db.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "echo": True,                # виводити SQL-запити
        "pool_recycle": 3600,        # перепідключення кожні N секунд
        "pool_timeout": 30,          # тайм очікування з'єднання
        "connect_args": {
            "timeout": 30,
            "check_same_thread": False  # потрібно для SQLite + Flask
        }
    }

    db.init_app(app)

    # Ініціалізація Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Будь ласка, увійдіть, щоб отримати доступ до цієї сторінки.'
    login_manager.login_message_category = 'info'

    # Функція завантаження користувача для Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        from models import User
        return User.query.get(int(user_id))


    # імпорт blueprint'ів усередині функції для уникнення циклічних імпортів
    from routes.main import main
    from routes.auth import auth
    from routes.category import category
    from routes.note import note


    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(category)
    app.register_blueprint(note)

    return app




if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        from models import User, Category, Note
        db.create_all()

    app.run(debug=True)