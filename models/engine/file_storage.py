#!/usr/bin/env python3
"""
Module: file_storage
Description: File storage model for all users.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


CLASSES = {"BaseModel": BaseModel, "User": User, "State": State,
           "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}


class FileStorage:
    """Storage models for serializationa and deserializatio
       workflow. Used continuously with the other subclasses created.
       The format goes as follows:
       class -> to_dict -> json dumps -> store in file -> json loads ->
       dictionary rep. -> class.
       Note: fmt >--< format

       Attributes:
            __file_path (str): path to file for storing objects.
            __objects (dict): contains python objects stored after each
                              creation and later serialized to json fmt.
       Methods:
            __all(self) -> returns the __objects for printing purposes.
            new(self, obj) -> used when a new instance of class is created.
            save(self) -> writes the json format of objects created to file.
            reload(self) -> reloads the objects from stored file to Python
                            objects.
      """
    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """Returns the dict. rep. of objects created.
        Args:
            None.
        Returns:
            __objects (dict): dictionary with Python objects.
        """
        return self.__objects

    def new(self, obj) -> None:
        """Updated class instance as new one is created.
        Args:
            obj (cls object): object to be updated in __objects.
        Returns:
            Nothing.
        """
        if obj is not None:
            self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
        return None

    def save(self) -> None:
        """Saves the created instance of class to file for later use.
        Args:
            None.
        Returns:
            Nothing.
        """
        store = {}
        for key in self.__objects.keys():
            store[key] = self.__objects[key].to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as fh:
            data = json.dumps(store)
            fh.write(data)
        return None

    def reload(self) -> None:
        """Reloads the saved objects on disk if __file_path exists.
           Otherwise, nothing happens on any captured exception.
        Args:
            None.
        Returns:
            Nothing.
        """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as fh:
                data = fh.read()
                objs = json.loads(data)
                for key in objs.keys():
                    self.__objects[key] = \
                        CLASSES[objs[key]["__class__"]](**objs[key])
        except FileNotFoundError:
            pass
        return None

    def delete(self, obj=None) -> None:
        """Deletes an instance from __objects.
        Args:
            obj (object): instance to delete from storage.
        Returns:
            Nothing.
        """
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            del self.__objects[key]
            self.save()
        return None
