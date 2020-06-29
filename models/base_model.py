#!/usr/bin/python3
'''[Function base model]
'''
import uuid
from datetime import datetime
import models


class BaseModel:
    '''[Defines all common attributes/methods for other classes]
    '''
    def __init__(self, *args, **kwargs):
        '''[Constructor]
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key in ['updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key not in ['__class__']:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

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
        self.updated_at = datetime.now()
        models.storage.save()

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
