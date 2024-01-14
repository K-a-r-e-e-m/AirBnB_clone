#!/usr/bin/python3
"""This Module for Review class that
 inherite from BaseModel class
 """
from models.base_model import BaseModel


class Review(BaseModel):
    """This Review class inherite from BaseModel
    and has a public class attributes"""

    place_id = ''
    user_id = ''
    text = ''
