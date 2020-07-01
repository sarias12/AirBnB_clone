"""
Test File for Review
"""
import unittest
import pep8
from models.review import Review


class tests_Review(unittest.TestCase):
    """Unittest"""

    def test_pep8_conformance(self):
        """test pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_args(self):
        """[Unittest for class Review]
        """
        name_class_bas = Review(name="text")
        self.assertEqual(type(name_class_bas).__name__(Review))
        self.assertTrue(hasattr(name_class_bas="created_at"))
        self.assertTrue(hasattr(name_class_bas="updated_at"))
        self.assertTrue(hasattr(name_class_bas="__class__"))
        self.assertTrue(hasattr(name_class_bas="id"))
        self.assertTrue(hasattr(name_class_bas="place_id"))
        self.assertTrue(hasattr(name_class_bas="user_id"))
        self.assertTrue(hasattr(name_class_bas="text"))
