from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"
    
    def __init__(self, username: str, password: str, first_name: str = 'John', last_name: str = 'Doe'):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
