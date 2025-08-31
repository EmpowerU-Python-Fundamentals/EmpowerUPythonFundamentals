from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from extensions import db
from models.user import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "supersecretkey123" 
db.init_app(app)


@app.route('/')
def index():
    user = session.get('user')
    return render_template('index.html', user=user)

@app.route('/signup_form')
def signup_form():
    return render_template('sign_up.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # check credentials in DB
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            print('User found in the DB!')
            # save login info in session
            session['user'] = {'id': user.id, 'username': user.username, 
                               'first_name': user.first_name, 'last_name': user.last_name}
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Invalid username or password")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)  
    return redirect(url_for('index'))


@app.route('/thankyou', methods=['POST'])
def thank_you():
    username = request.form.get('username')
    first = request.form.get('first')
    last = request.form.get('last')
    user_pass = request.form.get('password')

    new_user = User(username = username, password = user_pass, first_name = first, last_name = last)
    db.session.add(new_user)
    db.session.commit()

    return render_template('thank_you.html', first=first, last=last)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()   
    app.run(debug=True)