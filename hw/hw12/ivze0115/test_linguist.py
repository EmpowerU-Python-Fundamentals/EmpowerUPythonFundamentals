import os
import datetime
import linguist


def generate_user_name():
    now = datetime.datetime.now()
    return 'ivan_' + now.strftime("%Y%m%d_%H%M%S")


if __name__ == '__main__':
    db_file = "linguist.db"

    # check if file exists in current directory
    if os.path.isfile(db_file):
        print(f"Database file '{db_file}' already exists.")
    else:
        print(f"Database file '{db_file}' not found. It will be created.")
        engine = linguist.create_engine("sqlite:///linguist.db", echo=False)
        linguist.Base.metadata.create_all(engine)
        print("Database & tables created!")

    new_user = generate_user_name()
    new_email = new_user + '@example.com'
    new_password = new_user + '~pAs$123'

    # Create user
    u = linguist.user_create(new_user, new_email, new_password)
    print(f"User created: u.id: {u.id}, u.name: {u.name}")

    # Create deck
    d = linguist.deck_create("My words", u.id)
    print(f"Deck created: d.id: {d.id}, d.name: {d.name}")

    # Create card
    c = linguist.card_create(u.id, "forgiveness", "прощення", "the act of excusing a mistake or offense")
    print(f"Card created: c.id: {c.id}, c.word: {c.word}")

    # Filter
    print("Filter results:", [card.word for card in linguist.card_filter("for")])

    # Update
    linguist.card_update(c.id, tip="Compassionate feelings for someone that make it easier to forgive that person for some offense can be called ...")
    print("Updated card:", linguist.card_get_by_id(c.id).tip)
