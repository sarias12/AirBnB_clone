#!/usr/bin/python3
'''[summary]
'''
import uuid
import datetime

class BaseModel:
    '''[summary]
    '''
    def __init__(self): 
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        return dict(self.__dict__)