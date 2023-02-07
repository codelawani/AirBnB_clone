import uuid
import datetime


class BaseModel:
    """defines all common attributes/methods for other classes"""

    id = str(uuid.uuid4())
    created_at = datetime.datetime.today()
    updated_at = datetime.datetime.today()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        #        return {'my_number': self.my_number, 'name': self.__class__.__name__, id: self.id}
        trial = dict(self.__dict__)
        trial['id'] = self.id
        trial['created_at'] = self.created_at.isoformat()
        trial['updated_at'] = self.updated_at.isoformat()
        trial['__class__'] = self.__class__.__name__
        return trial
