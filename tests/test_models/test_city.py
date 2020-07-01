"""
Test File for City
"""
import unittest
import pep8
from models.city import City


class tests_City(unittest.TestCase):
    """Unittest"""

    def test_pep8_conformance(self):
        """test pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_args(self):
        """[Unittest for class City]
        """
        name_class_bas = City(name="text")
        self.assertEqual(type(name_class_bas).__name__(City))
        self.assertTrue(hasattr(name_class_bas="created_at"))
        self.assertTrue(hasattr(name_class_bas="updated_at"))
        self.assertTrue(hasattr(name_class_bas="__class__"))
        self.assertTrue(hasattr(name_class_bas="id"))
        self.assertTrue(hasattr(name_class_bas="state_id"))
        self.assertTrue(hasattr(name_class_bas="name"))
