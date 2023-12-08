#!/usr/bin/python3
"""This module defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        dict_obj = FileStorage.__objects
        objdict = {obj: dict_obj[obj].to_dict() for obj in dict_obj.keys()}
        with open(FileStorage.__file_path, "w") as wf:
            json.dump(objdict, wf)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as rf:
                objdict = json.load(rf)
                for ob in objdict.values():
                    class_name = ob["__class__"]
                    del ob["__class__"]
                    self.new(eval(class_name)(**ob))
        except FileNotFoundError:
            return
