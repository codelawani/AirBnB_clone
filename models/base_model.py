#!/usr/bin/python3
"""BaseModel module"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """defines all common attributes/methods for other classes"""

    id = str(uuid.uuid4())
    created_at = datetime.today()
    updated_at = datetime.today()

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at':
                        value = datetime.fromisoformat(value)
                        setattr(self, key, value)
                        continue
                    if key == 'updated_at':
                        value = datetime.fromisoformat(value)
                        setattr(self, key, value)
                        continue
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        #        return {'my_number': self.my_number, 'name': self.__class__.__name__, id: self.id}
        trial = dict(self.__dict__)
        trial['id'] = self.id
        trial['created_at'] = self.created_at.isoformat()
        trial['updated_at'] = self.updated_at.isoformat()
        trial['__class__'] = self.__class__.__name__
        return trial
