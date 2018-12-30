# -*- coding: utf-8 -*-
""" This module is used to Declare some object called BaseModel
    BaseModel will used in all object model that use to save data to database
"""
from datetime import datetime
from sqlalchemy import sql
from app.extensions import DB as sa


class BaseModel:
    """ This class is BaseModel and used by all model object in our app"""
    id = sa.Column(sa.Integer, primary_key=True)
    create_at = sa.Column(sa.DateTime, server_default=sql.func.now())
    update_at = sa.Column(sa.DateTime, onupdate=sql.func.now())
    deleted = sa.Column(sa.Boolean, default=False)
    delete_at = sa.Column(sa.DateTime)

    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__(*args, **kwargs)
        for data in args:
            for key in data:
                if isinstance(data[key], dict):
                    setattr(self, key, data[key])

    def from_request(self, *args):
        """Parsing data from request json
            """
        for data in args:
            for key in data:
                if isinstance(data[key], dict):
                    setattr(self, key, data[key])

    def save(self):
        """Method to save object to database"""
        sa.session.add(self)
        sa.session.commit()

    def delete(self):
        """Method to delete object
        In this method just add flag deleted to data.
        Not remove data from database
        """
        self.deleted = True
        self.delete_at = datetime.now()
        self.save()

    def restore(self):
        """Method to restore object
        In this method just set flag deleted to false to restore object.
        """
        self.deleted = False
        self.delete_at = None
        self.save()

    def remove(self):
        """Method to remove object permanently from database"""
        sa.session.delete(self)
        sa.session.commit()
