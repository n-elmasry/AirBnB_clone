#!/usr/bin/python3
'''User class defenition'''
from models.base_model import BaseModel


class User(BaseModel):
    '''User representation'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        '''User instance Initialization'''
        super().__init__(*args, **kwargs)
