"""
Test File for Amenity
"""
import unittest
import pep8
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.city import City
from datetime import datetime
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class tests_Amenity(unittest.TestCase):
    """Unittest"""

    def test_pep8_conformance(self):
        """test pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_all(self):
        """[test inst all]"""

    def test_new(self):
        """[test inst new]"""

    def test_save(self):
        """[test inst save]"""

    def test_reload(self):
        """[test inst all]"""
