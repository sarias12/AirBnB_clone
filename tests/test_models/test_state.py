"""
Test File for State
"""
import unittest
import pep8
from models.state import State


class tests_State(unittest.TestCase):
    """Unittest"""

    def test_pep8_conformance(self):
        """test pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_args(self):
        """[Unittest for class State]
        """
        name_class_bas = State(name="text")
        self.assertEqual(type(name_class_bas).__name__(State))
        self.assertTrue(hasattr(name_class_bas="created_at"))
        self.assertTrue(hasattr(name_class_bas="updated_at"))
        self.assertTrue(hasattr(name_class_bas="__class__"))
        self.assertTrue(hasattr(name_class_bas="id"))
        self.assertTrue(hasattr(name_class_bas="name"))
