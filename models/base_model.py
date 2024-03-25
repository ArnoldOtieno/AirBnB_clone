#!/usr/bin/python3
"""Base model class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """initialization function for the class"""

        if kwargs:
            for key, value in kwargs.items():
                mformat = "%Y-%m-%dT%H:%M:%S.%f"
                if key == "created_at":
                    if type(kwargs["created_at"]) is str:
                        value = datetime.now().strptime(value, mformat)
                if key == "updated_at":
                    if type(kwargs["updated_at"]) is str:
                        value = datetime.now().strptime(value, mformat)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """prints the class, name and id of the class"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute"""

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns dictionary containing keys and values of dict"""

        dicCopy = self.__dict__.copy()
        dicCopy["__class__"] = self.__class__.__name__
        if "created_at" in dicCopy:
            dicCopy["created_at"] = datetime.now().isoformat()
        if "updated_at" in dicCopy:
            dicCopy["updated_at"] = datetime.now().isoformat()
        return dicCopy
