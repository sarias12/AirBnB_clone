"""
Test File for Amenity
"""
import unittest
import pep8
from models.amenity import Amenity


class tests_Amenity(unittest.TestCase):
    """Unittest"""

    def test_pep8_conformance(self):
        """test pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_args(self):
        """[Unittest for class Amenity]
        """
        name_class_bas = Amenity(name="text")
        self.assertEqual(type(name_class_bas).__name__(Amenity))
        self.assertTrue(hasattr(name_class_bas="created_at"))
        self.assertTrue(hasattr(name_class_bas="updated_at"))
        self.assertTrue(hasattr(name_class_bas="__class__"))
        self.assertTrue(hasattr(name_class_bas="id"))
        self.assertTrue(hasattr(name_class_bas="name"))
