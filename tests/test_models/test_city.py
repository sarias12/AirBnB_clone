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

    def test_city(self):
        """Unittest city method"""
        Cities = City()
        self.assertEqual(type(Cities).__name__("City"))
