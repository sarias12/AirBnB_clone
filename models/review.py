#!/usr/bin/python3
'''[Class review]
'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''[Create new that inherits from BaseModel]
    '''
    place_id = ""
    user_id = ""
    text = ""
