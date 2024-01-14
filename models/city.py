#!/usr/bin/python3
"""This Module for City class that
 inherite from BaseModel class
 """
from models.base_model import BaseModel


class City(BaseModel):
    """This City class inherite from BaseModel
    and has a public class attributes"""

    state_id = ''
    name = ''
