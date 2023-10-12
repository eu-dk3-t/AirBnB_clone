#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ BaseModel Class """

    def __init__(self, *args, **kwargs):
        """ Initialize a new BaseModel. """

        form = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    self.__dict__[k] = datetime.strptime(v, form)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """ Return the print/str representation of the BaseModel instance. """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """ Update updated_at with the current datetime. """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return the dictionary of the BaseModel instance. """
        inst_d = self.__dict__.copy()
        inst_d['created_at'] = self.created_at.isoformat()
        inst_d['updated_at'] = self.updated_at.isoformat()
        inst_d['__class__'] = self.__class__.__name__
        return inst_d
