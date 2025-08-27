from extensions import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    email = db.Column(db.Text, unique = True, index = True)
    password = db.Column(db.Text)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f'User {self.name=} {self.email=} {self.id=}'
    
    @classmethod
    def user_create(cls, name: str, email: str, password: str) -> "User": 
        """Create a User, save it to the DB and return the instance. Email should be unique."""
        user = cls(name, email, password)
        db.session.add(user)
        db.session.commit()

        return user
    
    @classmethod
    def user_get_by_id(cls, user_id: int) -> "User":
        """Return the User instance with the given ID, or None if not found."""
        return cls.query.get(user_id)
    
    @classmethod
    def user_update_name(cls, user_id: int, name: str) -> "User": 
        """Updates user's name in the DB. Returns None if there's no user with this ID."""
        user = cls.query.get(user_id)
        if not user:
            return None
        user.name = name

        db.session.commit()
        return user
    
    @classmethod
    def user_change_password(cls, user_id: int, old_password: str, new_password: str) -> bool:
        """Updates the password of the user. Returns False if there's no such User in the DB, 
        or if the old_password param isn't equal to user's current password"""

        user = cls.query.get(user_id)
        if not user or user.password != old_password:
            return False
        user.password = new_password

        db.session.commit()
        return True
    

    @classmethod
    def user_delete_by_id(cls, user_id: int) -> bool:
        """Delete a user by ID. Return True if deleted, False if not found."""
        user = cls.query.get(user_id)
        if not user:
            return False

        db.session.delete(user)
        db.session.commit()
        return True
