#!/usr/bin/python3
'''[summary]
'''
import json
from models.base_model import BaseModel


class FileStorage:
    '''[Function serializes instances to a JSON file and deserializes]
    '''
    __file_path = 'file.json'
    __object = {}

    def all(self):
        '''[all]
        '''
        return self.__object

    def new(self, obj):
        '''[summary]

        Args:
            obj ([type]): [description]
        '''
        if obj:
            key = '{} {}'.format(type(obj).__name__, obj.id)
            self.__object[key] = obj

    def save(self):
        '''[summary]
        '''
        obj = {}
        for key, i in type(self).__object.items():
            obj[key] = i.to_dict()

        json_str = json.dumps(obj)

        with open(type(self).__file_path, 'w', encoding='utf-8') as f:
            f.write(json_str)

    def reload(self):
        '''[summary]
        '''
        try:
            with open(type(self).__file_path, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)
        except:
            pass
