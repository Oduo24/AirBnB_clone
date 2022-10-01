#!/usr/bin/python3
"""
Contains my models
"""

import uuid
import datetime
from __init__ import storage


class BaseModel:
    """
    Describes all the common attributes/methods for other classes
    """


    def __init__(self, *args, **kwargs):
        """Initializes an instance of the class
        """
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == 'created_at':
                        v = datetime.datetime.fromisoformat(v)
                    if k == 'updated_at':
                        v = datetime.datetime.fromisoformat(v)
                    setattr(self, k, v)
                    storage.new(self)
                    storage.save()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
            storage.save()

    def __str__(self):
        """Defines a string representation of any object of this class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the 'updated_at attribute of the object'
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all key/value of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = str(datetime.datetime.isoformat(self.created_at))
        new_dict['updated_at'] = str(datetime.datetime.isoformat(self.updated_at))
        new_dict['__class__'] = self.__class__.__name__
        return new_dict



