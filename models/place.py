#!/usr/bin/python3
'''[Class place]
'''

from models.base_model import BaseModel


class Place(BaseModel):
    '''[Create new that inherits from BaseModel]
    '''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guess = 0
    price_by_night = 0
    latitude = 0.0
    logitude = 0.0
    amenity_ids = [""]
