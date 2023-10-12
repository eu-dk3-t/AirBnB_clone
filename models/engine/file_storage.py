#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ Storage """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """ Adds a new k/v pair """
        k_obj = obj.__class__.__name__
        FileStorage.__objects[f'{k_obj}.{obj.id}'] = obj

    def save(self):
        """ Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        obj_d = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_d, f)

    def reload(self):
        """ Deserialize the JSON file __file_path to __objects."""
        try:
            FileStorage.__objects.clear()
            with open('file.json', 'r') as f:
                obj_d = json.load(f)
                for k, val in obj_d.items():
                    FileStorage.__objects[k] = eval(val["__class__"])(**val)
        except (FileNotFoundError, IOError, ValueError):
           pass
