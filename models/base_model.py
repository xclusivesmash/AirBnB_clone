#!/usr/bin/env python3
"""
Module: base_model
Description: Blueprint base class for all subsequent classes.
"""
import uuid
from datetime import datetime
import models

_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Blueprint class for all subclasses related to the
       airbnb clone website. The subclasses include, but not
       limited to, city, user, amnity, etc.
       Note: rep. -> represantation.

       Attributes:
            id (str): unique id for each instance created.
            created_at (datetime): time when the object is created.
            updated_at (datetime): time when the object is updated.
       Methods:
            __init__(self, *args, **kwargs) -> initialization.
            __str__(self) -> string rep. of an object.
            save(self) -> updated the class instance after each modification.
            to_dict(self) -> gives a dict. rep. of an object.
       """

    def __init__(self, *args: list, **kwargs: dict) -> None:
        """Initialization method.
        Args:
            args (list): list of extra args passed to class
                         during initialization.
            kwargs (dict): dictionary with attributes as keys and
                           their associated values.
        Returns:
            Nothing.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    # do nothing, just pass to next item.
                    continue
                setattr(self, key, value)
                if type(self.updated_at) is str:
                    self.updated_at = datetime. \
                        strptime(self.updated_at, _format)
                if type(self.created_at) is str:
                    self.created_at = datetime. \
                        strptime(self.created_at, _format)
        else:
            models.storage.new(self)
        return None

    def __str__(self) -> str:
        """Returns str rep. of an object.
        Args:
            None
        Returns:
            (str): string rep. of an object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """Updates object when modification happens.
        Args:
            None
        Returns:
            Nothing.
        """
        self.updated_at = datetime.now()
        # models.storage.new(self)
        models.storage.save()
        return None

    def to_dict(self) -> dict:
        """Converts an instance of class to dict rep.
        Args:
            None
        Returns:
            dict_one (dict): dictionary rep. of object with
                             values of self.__dict__ and more added ones.
        """
        dict_one = self.__dict__.copy()
        dict_one["__class__"] = self.__class__.__name__
        if "updated_at" in dict_one:
            dict_one["updated_at"] = dict_one["updated_at"].isoformat()
        if "created_at" in dict_one:
            dict_one["created_at"] = dict_one["created_at"].isoformat()
        return dict_one
