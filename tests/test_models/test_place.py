"""
Test File for Place
"""
import unittest
import pep8
from models.place import Place


class tests_Place(unittest.TestCase):
    """Unittest"""

    def test_pep8_conformance(self):
        """test pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_args(self):
            """[Unittest for class Place]
            """
            name_class_bas = Place(name="text")
            self.assertEqual(type(name_class_bas).__name__(Place))
            self.assertTrue(hasattr(name_class_bas="created_at"))
            self.assertTrue(hasattr(name_class_bas="updated_at"))
            self.assertTrue(hasattr(name_class_bas="__class__"))
            self.assertTrue(hasattr(name_class_bas="id"))
            self.assertTrue(hasattr(name_class_bas="city_id"))
            self.assertTrue(hasattr(name_class_bas="user_id"))
            self.assertTrue(hasattr(name_class_bas="name"))
            self.assertTrue(hasattr(name_class_bas="description"))
            self.assertTrue(hasattr(name_class_bas="number_rooms"))
            self.assertTrue(hasattr(name_class_bas="number_bathrooms"))
            self.assertTrue(hasattr(name_class_bas="max_guest"))
            self.assertTrue(hasattr(name_class_bas="price_by_night"))
            self.assertTrue(hasattr(name_class_bas="latitude"))
            self.assertTrue(hasattr(name_class_bas="longitude"))
            self.assertTrue(hasattr(name_class_bas="amenity_ids"))
