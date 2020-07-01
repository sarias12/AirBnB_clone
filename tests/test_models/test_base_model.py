#!/usr/bin/python3
"""
Test File for BaseModel
"""
import unittest
import pep8


class tests_BaseModel(unittest.TestCase):
    """Unittest"""

    def test_pep8_conformance(self):
        """test pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")


    def test_args(self):
        name_class_bas = BaseModel(name="Holis")
        self.assertEqual(type(name_class_bas).__name__(BaseModel))
        self.assertFalse(hasattr(name_class_bas="created_at"))
        self.assertFalse(hasattr(name_class_bas="updated_at"))
        self.assertFalse(hasattr(name_class_bas="__class__"))
        self.assertFalse(hasattr(name_class_bas="id"))