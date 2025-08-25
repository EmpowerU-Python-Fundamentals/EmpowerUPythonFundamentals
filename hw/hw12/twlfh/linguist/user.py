class User:
    """
    Represents a user of the system.
    """
    def __init__(self, id: int, name: str, email: str, password: str):
        """
        Initialize a new User object.

        Args:
            id (int): Unique user ID.
            name (str): User's name.
            email (str): User's email address.
            password (str): User's password.
        """
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def user_update_name(self, name: str):
        """Update the user's name."""
        self.name = name
        return self.name

    def user_change_password(self, old_password: str, new_password: str):
        """Change the user`s password"""
        if self.password == old_password:
            self.password = new_password
            return True
        else:
            return False

users_db = {}

def user_create(name, email, password):
    """Created a new user"""
    new_id = max(users_db.keys(), default=0) + 1
    user = User(new_id, name, email, password)
    users_db[new_id] = user
    return user

def user_get_by_id(user_id):
    """Retrieve a user by ID."""
    return users_db.get(user_id)

def user_update_name(user_id, name):
    """Update the name of a user"""
    user = users_db.get(user_id)
    if user:
        user.user_update_name(name)
        return user
    return False

def user_change_password(user_id, old_password, new_password):
    """Change the user's password"""
    user = users_db.get(user_id)
    if user:
        return user.user_change_password(old_password, new_password)
    else:
        return False

def user_delete_by_id(user_id):
    """Deleted a user by id"""
    if user_id in users_db:
        del users_db[user_id]
        return True
    return False


