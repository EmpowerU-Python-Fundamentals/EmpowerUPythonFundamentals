import unittest
from linguist_app import (
    init_db,
    user_create,
    user_get_by_id,
    user_update_name,
    user_change_password,
    user_delete_by_id,
    deck_create,
    deck_get_by_id,
    deck_update,
    deck_delete_by_id,
    card_create,
    card_get_by_id,
    card_filter,
    card_update,
    card_delete_by_id,
    session,
)

class TestLinguistApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init_db("sqlite:///:memory:")

    def test_user_crud_and_password(self):
        u = user_create("Alice", "alice@example.com", "pw1")
        self.assertIsNotNone(u.id)
        fetched = user_get_by_id(u.id)
        self.assertEqual(fetched.email, "alice@example.com")
        updated = user_update_name(u.id, "Alicia")
        self.assertEqual(updated.name, "Alicia")
        self.assertTrue(user_change_password(u.id, "pw1", "pw2"))
        self.assertFalse(user_change_password(u.id, "wrong", "x"))
        self.assertTrue(user_delete_by_id(u.id))
        self.assertFalse(user_delete_by_id(u.id))

    def test_deck_crud(self):
        u = user_create("Bob", "bob@example.com", "bpass")
        d = deck_create("Basics", u.id)
        self.assertIsNotNone(d.id)
        fetched = deck_get_by_id(d.id)
        self.assertEqual(fetched.name, "Basics")
        updated = deck_update(d.id, "Everyday")
        self.assertEqual(updated.name, "Everyday")
        self.assertTrue(deck_delete_by_id(d.id))
        self.assertFalse(deck_delete_by_id(d.id))

    def test_card_crud_and_filter(self):
        u = user_create("Carol", "carol@example.com", "cpass")
        c1 = card_create(u.id, "apple", "яблуко", "fruit")
        c2 = card_create(u.id, "book", "книга", "read")
        c3 = card_create(u.id, "notebook", "зошит", "write")
        self.assertEqual(card_get_by_id(c1.id).word, "apple")
        matches = card_filter("ook")
        self.assertTrue(any(c.word == "book" for c in matches))
        self.assertTrue(any(c.word == "notebook" for c in matches))
        self.assertFalse(any(c.word == "apple" for c in matches))
        updated = card_update(c1.id, tip="red fruit")
        self.assertEqual(updated.tip, "red fruit")
        self.assertTrue(card_delete_by_id(c2.id))
        self.assertFalse(card_delete_by_id(c2.id))

    @classmethod
    def tearDownClass(cls):
        try:
            session.close()
        except Exception:
            pass

if __name__ == "__main__":
    unittest.main()

