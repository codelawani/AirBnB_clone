import uuid
import datetime

class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self):
        """initializes class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        trial = dict(self.__dict__)
        trial['created_at'] = self.created_at.isoformat()
        trial['updated_at'] = self.updated_at.isoformat()
        return trial
