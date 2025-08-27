import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from extensions import db
from model.user import User
from model.card import Card
from model.deck import Deck


def init_app():
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'data.sqlite')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route("/")
    def index():
        test_deck_app()
        return "The test succeeded!"

    return app

def test_deck_app():
    db.session.query(User).delete()
    db.session.query(Deck).delete()
    db.session.query(Card).delete()
    db.session.commit()

    user = User.user_create("Ivan", "my.email@gmail.com", "1223")
    print(user)
    assert user.id > 0

    user = User.user_update_name(user.id, "NotIvan")
    print(user)

    changingPasswordSuccess = User.user_change_password(user.id, "1223", "NewPassword")
    print(f'{changingPasswordSuccess=}')

    userFromDb = User.user_get_by_id(user.id)
    print(f'user from db: {userFromDb}')

    card = Card.card_create(user.id, "Flashy", "Сяючий", "Very bright")
    print(f'First card {card}')
    assert card.id > 0

    card2 = Card.card_create(user.id, "Nonsense", "Нісенітниця", "Something that doesn't make any sense")
    print(f'Second card {card2}')

    cardFromDb = Card.card_get_by_id(card.id)
    assert card == cardFromDb
    print(f'Card that returned from DB is the same card? {card == cardFromDb}')

    cardFromFilter = Card.card_filter("Ніс")[0]
    assert cardFromFilter == card2
    print(f'Card from filter is the second card? {cardFromFilter == card2}')

    deck = Deck.deck_create("Important Deck", user.id)
    print(deck)
    assert deck.id > 0

    deckFromDb = Deck.deck_get_by_id(deck.id)
    assert deck == deckFromDb

    deleted = Deck.deck_delete_by_id(deck.id)
    assert deleted





if __name__ == "__main__":
    app = init_app()
    app.run(debug=True)