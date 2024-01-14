#!/usr/bin/python3
"""This Module for User class that
 inherite from BaseModel class
 """
from models.base_model import BaseModel


class User(BaseModel):
    """This User class inherite from BaseModel
    and has a public class attributes"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
