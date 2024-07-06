#!/usr/bin/python3
"""
BaseModel class.
"""
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String

Base = declarative_base()


class BaseModel:
    """Base class that defines all common attributes/methods for other classes"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize a new class BaseModel."""
        self.id = str(uuid4()) # Unique ID for each base model
        self.created_at = self.updated_at = datetime.now()
        # if kwargs:
        #     for key, value in kwargs.items():
        #         if key == "created_at" or key == "updated_at":
        #             value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
        #         if key != "__class__":
        #             setattr(self, key, value)

    def save(self):
        """save method that update the time"""
        self.updated_at = datetime.now()
        # models.storage.new(self)
        # models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        # get a copy from __dict__ to update it
        new_dict = self.__dict__.copy()
        # Add the class name
        new_dict['__class__'] = self.__class__.__name__
        # Convert the datetime objects to ISO strings
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

    # def delete(self):
    #     """
    #     Delete method
    #     """
    #     models.storage.delete(self)

    def __str__(self):
        """Return string representation of the class"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
