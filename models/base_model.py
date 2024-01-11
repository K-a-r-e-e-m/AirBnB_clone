#!/usr/bin/python3
from datetime import datetime
import uuid
import models


class BaseModel:
    """
    base class for airbnb tasks
    """
    def __init__(self, *args, **kwargs):
        """
        initialization method
        """
        DATA_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
        if not kwargs:
            self.id = str(uuid.uuid4(id))
            self.created_at = datetime.utcnow
            self.updated_at = datetime.utcnow
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                            value, DATA_TIME_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
        return the represntation of the class for the user
        """
        return "[{} ({}) {}]".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        udate the public attribute updated_at
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        return dict that has all __dict__ instacne
        """
        myDict = {}
        for key, value in self.__dict__.items:
            if key == "created_at" or key == "updated_at":
                myDict[key] = value.isoformat()
            else:
                myDict[key] = value
        myDict["__class__"] = self.__class__.__name__
        return myDict
