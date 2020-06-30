#!/usr/bin/python3
'''[Class User]
'''

from models.base_model import BaseModel


class User(BaseModel):
    '''[Create new that inherits from BaseModel]
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
