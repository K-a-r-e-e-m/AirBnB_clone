#!/usr/bin/python3
"""
base module
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    base class
    """
    def __init__(self, *args, **kwargs):
        """
            Initialize attributes.
        """
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """
        return the represntation of the class for the user
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        """
        return the represntation of the class for the developer
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
        udate the public attribute updated_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        return dict that has all __dict__ instacne
        """
        myDict = dict(self.__dict__)
        myDict['__class__'] = self.__class__.__name__
        myDict['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        myDict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return (myDict)
