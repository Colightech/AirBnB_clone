#!/usr/bin/python3
"""A module that defines the class base model"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ this class is the base class and it
    defines all common attributes/methods for other classes"""

    def __init__(self, *args, kwargs):
        """the init method of the base class"""

        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """this method updates the public instance
        attribute updated_at with the current datetime"""
        self.updated_at = datetime.today
        models.storage.save()

    def to_dict(self):
        """this method returns a dictionary containing all 
        keys/values of __dict__ of the instance"""
        dict_copy = self.__dict__.copy
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["__class__"] = self.__class__.__name__
        return (dict_copy)

    def __str__(self):
        """this method print [<class name>] (<self.id>)
        <self.__dict__> Public instance methods"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
