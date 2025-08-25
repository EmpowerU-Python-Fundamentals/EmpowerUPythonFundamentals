import unittest
from .models import User, UserCRUD

class UserTests(unittest.TestCase):
    def test_create_user(self):
        user = User("Ihor", "rest@g,ail.com")
        self.assertEqual(type(user), User, "message")
        self.assertEqual(user.name, "Ihor")
        self.assertEqual(user.email, "rest@g,ail.com", "message")
    def test_create_user2(self):
        user = User("Ihor", "rest@g,ail.com", "152")
        self.assertEqual(type(user), User, "message")
        self.assertEqual(user.name, "Ihor")
        self.assertEqual(user.email, "rest@g,ail.com", "message")
        self.assertEqual(user.id, 15, "message")


class UserUserCRUD(unittest.TestCase):

    def test_create_user(self):
        manager = UserCRUD()
        for i in range(5):
            manager.create("Ihor", f"rest_{i}@g,ail.com", i)
        self.assertEqual(len(manager.users_db), 5)
    def test_create_user2(self):
        manager = UserCRUD()
        for i in range(5):
            manager.create("Ihor", f"rest_{i}@g,ail.com", i)
        actual = manager.read("4")
        self.assertEqual(actual.id, "4")
        self.assertEqual(actual.name, "Ihor")
        self.assertEqual(actual.email, "rest_4@g,ail.com")
    def test_create_user_readIsNone2(self):
        manager = UserCRUD()
        for i in range(5):
            manager.create("Ihor", f"rest_{i}@g,ail.com", i)
        actual = manager.read("44")
        self.assertIsNone(actual)
        
if __name__ == "__main__":
    unittest.main()

# coverage run -m unittest .\lessons\lesson14\tests.py
# coverage html