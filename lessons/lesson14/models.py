import uuid
from typing import Dict, List, Optional

# --- User Model Class ---
# This class defines the structure of a user object.
# It's a simple data container.
class User:
    def __init__(self, name: str, email: str, user_id: Optional[str] = None):
        # Generate a unique ID if one is not provided.
        self.id = user_id if user_id else str(uuid.uuid4())
        self.name = name
        self.email = email

    def to_dict(self) -> Dict:
        """Converts the user object to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }

    def __repr__(self):
        """Provides a string representation for easy printing."""
        return f"User(id='{self.id}', name='{self.name}', email='{self.email}')"

# --- CRUD Operations Class ---
# This class handles the business logic for managing users.
# It simulates a data layer that interacts with a database (in this case, a list).
class UserCRUD:
    def __init__(self):
        # The "database" is just a list to hold User objects.
        self.users_db: List[User] = []

    def create(self, name: str, email: str, pk:str) -> User:
        """
        Creates a new user and adds it to the database.
        
        Args:
            name: The user's name.
            email: The user's email.
            
        Returns:
            The newly created User object.
        """
        new_user = User(name=name, email=email, user_id=str(pk))
        self.users_db.append(new_user)
        return new_user

    def read(self, user_id: str) -> Optional[User]:
        """
        Retrieves a single user by their ID.
        
        Args:
            user_id: The ID of the user to retrieve.
            
        Returns:
            The User object if found, otherwise None.
        """
        for user in self.users_db:
            if user.id == user_id:
                return user
        return None

    def read_all(self) -> List[User]:
        """
        Retrieves all users from the database.
        
        Returns:
            A list of all User objects.
        """
        return self.users_db

    def update(self, user_id: str, new_data: Dict) -> Optional[User]:
        """
        Updates an existing user's information.
        
        Args:
            user_id: The ID of the user to update.
            new_data: A dictionary containing the new data (e.g., {'name': 'New Name'}).
            
        Returns:
            The updated User object if successful, otherwise None.
        """
        user_to_update = self.read(user_id)
        if user_to_update:
            # Update attributes based on the provided dictionary.
            if 'name' in new_data:
                user_to_update.name = new_data['name']
            if 'email' in new_data:
                user_to_update.email = new_data['email']
            return user_to_update
        return None

    def delete(self, user_id: str) -> bool:
        """
        Deletes a user from the database by their ID.
        
        Args:
            user_id: The ID of the user to delete.
            
        Returns:
            True if the user was deleted, False otherwise.
        """
        user_to_delete = self.read(user_id)
        if user_to_delete:
            self.users_db.remove(user_to_delete)
            return True
        return False