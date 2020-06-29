#!/usr/bin/python3
'''[FileStorage Module]
'''
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    '''[Function serializes instances to a JSON file and deserializes]
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """[Function all]

        Returns:
            [dict]: [dictionary __object]
        """
        return type(self).__objects

    def new(self, obj):
        '''[Function new]

        Args:
            [obj]: [sets in __object (attribute class)
            with key <obj class name>.id ]
        '''
        if obj:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            type(self).__objects[key] = obj

    def save(self):
        '''[Function save serializes __objects
        to the JSON file (path: __file_path)]
        '''
        obj = {}
        for key, i in type(self).__objects.items():
            obj[key] = i.to_dict()

        json_str = json.dumps(obj)

        with open(type(self).__file_path, 'w', encoding='utf-8') as f:
            f.write(json_str)

    def reload(self):
        '''[Function reload deserializes the JSON file
        to __objects (only if the JSON file (__file_path) exists]
        '''
        try:
            with open(type(self).__file_path, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    name_class = eval(value['__class__'])(**value)
                    type(self).__objects[key] = name_class
        except:
            pass
