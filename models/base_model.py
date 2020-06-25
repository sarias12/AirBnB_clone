#!/usr/bin/python3
'''[summary]
'''
import uuid
import datetime


class BaseModel:
    '''[Defines all common attributes/methods for other classes]
    '''
    def __init__(self):
        '''[Constructor]
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        '''[Function str]

        Returns:
            [str]: [Return string]
        '''
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        '''[Function save that update the public instance attribute]
        '''
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        '''[Function that return a dictinary containing all key/values]

        Returns:
            [dict]: [Return a dictionary]
        '''
        dicty = dict(self.__dict__)
        dicty['__class__'] = type(self).__name__
        dicty['created_at'] = self.created_at.isoformat()
        dicty['updated_at'] = self.updated_at.isoformat()
        return dicty
