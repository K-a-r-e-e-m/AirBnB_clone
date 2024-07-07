#!/usr/bin/python3
"""
BaseModel class.
"""
from datetime import datetime
from uuid import uuid4
import models
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column
# from sqlalchemy import DateTime
# from sqlalchemy import String

# Base = declarative_base()


class BaseModel:
    """Base class that defines all common
    attributes/methods for other classes"""

    # id = Column(String(60), primary_key=True, nullable=False)
    # created_at = Column(DateTime, nullable=False, default=datetime.now())
    # updated_at = Column(DateTime, nullable=False, default=datetime.now())

    def __init__(self, *args, **kwargs):
        """Initialize a new class BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    # strptime returns a datetime object from str object
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key == '__class__':
                    continue
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())  # Unique ID for each base model
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """save method that update the time"""
        self.updated_at = datetime.now()
        models.storage.save()
        # models.storage.new(self)
        # models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        # get a copy from __dict__ to update it
        myDict = self.__dict__.copy()
        # Add the class name
        myDict['__class__'] = self.__class__.__name__
        # Convert the datetime objects to ISO strings
        myDict['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        # strftime is equal to isoformat when strftime take ISO format code
        myDict['updated_at'] = self.updated_at.isoformat()
        return myDict

    # def delete(self):
    #     """
    #     Delete method
    #     """
    #     models.storage.delete(self)

    def __str__(self):
        """Return string representation of the class"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
