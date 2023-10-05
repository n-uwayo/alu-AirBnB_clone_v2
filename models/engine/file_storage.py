#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of objects of the specified class"""
        if cls:
            return {key: obj for key, obj in self.__objects.items() if isinstance(obj, cls)}
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage"""
        if obj:
            key = f"{type(obj).__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serializes the objects to a JSON file"""
        serialized_objects = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="UTF-8") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as file:
                serialized_objects = json.load(file)
                for key, value in serialized_objects.items():
                    obj = eval(value["__class__"])(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object if it exists in the storage"""
        if obj:
            key = f"{type(obj).__name__}.{obj.id}"
            self.__objects.pop(key, None)
            self.save()

    def close(self):
        """Deserializes the JSON file to objects"""
        self.reload()

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        return {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

    def attributes(self):
        """Returns the valid attributes and their types for each class."""
        return {
            "BaseModel": {"id": str, "created_at": datetime.datetime, "updated_at": datetime.datetime},
            "User": {"email": str, "password": str, "first_name": str, "last_name": str},
            "State": {"name": str},
            "City": {"state_id": str, "name": str},
            "Amenity": {"name": str},
            "Place": {"city_id": str, "user_id": str, "name": str, "description": str,
                      "number_rooms": int, "number_bathrooms": int, "max_guest": int,
                      "price_by_night": int, "latitude": float, "longitude": float, "amenity_ids": list},
            "Review": {"place_id": str, "user_id": str, "text": str}
        }  
