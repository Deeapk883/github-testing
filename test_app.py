import unittest
from app import greet, login

class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Deepak"), "Hello Deepak")
        self.assertEqual(greet("Alice"), "Hello Alice")
        self.assertEqual(greet(""), "Hello ")

    def test_login(self):
        self.assertEqual(login("Deepak"), "Deepak logged in")
        self.assertEqual(login("Alice"), "Alice logged in")

if __name__ == "__main__":
    unittest.main()
