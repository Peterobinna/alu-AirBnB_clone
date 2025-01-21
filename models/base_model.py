# Create base model class with the following attributes
# 1. id
# 2. created_at
# 3. updated_at
from models import storage
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)


    def __str__(self):
        return f'[{self.__class__}] ({self.id}) {self.__dict__}'
    
    def save(self, *args):
        self.updated_at = datetime.now()
        storage.save(self, *args)
        
    def to_dict(self):
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()

        return result
    

    
