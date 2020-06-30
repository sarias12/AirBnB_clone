#!/usr/bin/python3
'''[Class City]
'''

from models.base_model import BaseModel


class City(BaseModel):
    '''[Create new that inherits from BaseModel ]

    Attributes:
        state_id ([str]): [state id]
        name ([str]): [amenity name]
    '''
    state_id = ""
    name = ""
