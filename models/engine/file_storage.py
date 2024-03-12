#!/usr/bin/python3
"""Manages the file storage for hbnb clone"""
import json


class FileStorage:
    """serializes to a JSON file and deserializes to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Stores a new object"""
        self.all().update({obj.to_dict()['__class__'] + "." + obj.id: obj})

    def save(self):
        """serializes stored dictionary to a JSON file"""
        with open(FileStorage.__file_path, 'w') as s:
            tmp = {}
            tmp.update(FileStorage.__objects)
            for key, val in tmp.items():
                tmp[key] = val.to_dict()
            json.dump(tmp, s)

    def reload(self):
        """Deserializes JSON file into instances"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    "BaseModel": BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                    }
        try:
            tmp = {}
            with open(FileStorage.__file_path, 'r') as s:
                tmp = json.load(s)
                for key, val in tmp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
