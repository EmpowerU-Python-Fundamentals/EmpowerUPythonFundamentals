from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello')
def hello():
    return 'Hello, all World'

@app.route('/hello/<name_user>')
def hello_name(name_user):
    print(type(name_user), name_user)
    return f'Hello, {name_user}'

@app.route('/hello/<int:user_id>')
def hello_id(user_id):
    print(type(user_id), user_id)
    return f'user id: {user_id}'



@app.route('/hello/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {subpath}'



@app.route('/user/<int:user_id>')
def user_id(user_id):
    print(type(user_id), user_id)
    return f'user id: {user_id}' 


if __name__ == '__main__':
    with app.test_request_context():
        print( url_for('hello_world'))
        print( url_for('hello'))
        print( url_for('hello_name', name_user="Liubomyr"))

        print (url_for('hello_id', user_id=15))


    app.run(host="0.0.0.0", port=5000, debug=True)



