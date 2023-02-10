#!/usr/bin/python3
import uuid
import datetime
import models


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__ (self, *args, **kwargs):
        """initializes the class atrributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                    value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.today()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.today()
            self.updated_at = datetime.datetime.today()
            models.storage.new(self)
    
    def __str__(self):
        """returns the class name"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute"""
        self.updated_at = datetime.datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary"""
        trial = dict(self.__dict__)
        trial['id'] = self.id
        trial['created_at'] = self.created_at.isoformat()
        trial['updated_at'] = self.updated_at.isoformat()
        trial['__class__'] = self.__class__.__name__
        return trial
