#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DATETIME
from datetime import datetime
import uuid

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column("id", String(60), nullable=False, primary_key=True)
    created_at = Column("created_at", DATETIME, nullable=False,
                        default=datetime.utcnow())
    updated_at = Column("updated_at", DATETIME, nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """ Instatntiates a new model """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
            for k, v in kwargs.items():
                if k != "__class__":
                    if k in ["created_at", "updated_at"]:
                        setattr(self, k, datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = dict(self.__dict__)
        dictionary['__class__'] = str(type(self).__name__)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        try:
            del dictionary['_sa_instance_state']
        except KeyError:
            pass

        return dictionary

    def delete(self):
        """ Deletes the current instance from the storage """
        from models import storage
        storage.delete(self)
