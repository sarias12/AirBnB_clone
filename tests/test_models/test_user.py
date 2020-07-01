"""
Test File for User
"""
import unittest
import pep8
from models.user import User


class tests_User(unittest.TestCase):
    """Unittest"""

    def test_pep8_conformance(self):
        """test pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_args(self):
        """[Unittest for class User]
        """
        name_class_bas = User(name="text")
        self.assertEqual(type(name_class_bas).__name__(User))
        self.assertTrue(hasattr(name_class_bas="created_at"))
        self.assertTrue(hasattr(name_class_bas="updated_at"))
        self.assertTrue(hasattr(name_class_bas="__class__"))
        self.assertTrue(hasattr(name_class_bas="id"))
        self.assertTrue(hasattr(name_class_bas="email"))
        self.assertTrue(hasattr(name_class_bas="password"))
        self.assertTrue(hasattr(name_class_bas="first_name"))
        self.assertTrue(hasattr(name_class_bas="last_name"))
