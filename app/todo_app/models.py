# -*- coding: utf-8 -*-
""" This is module to declare todo data"""
from sqlalchemy import and_
from app.models import BaseModel, sa
from app import extensions


class Todo(sa.Model, BaseModel):
    """TodoModel is object will be save in database"""
    __tablename__ = 'todo_tb'
    name = sa.Column(sa.String(20))
    description = sa.Column(sa.String(255))

    @staticmethod
    def get_all_todo(search, page, trash):
        """ Get All Todo data
        :param search: keyword to search todo
        :param page: number of page will show
        :param trash: deleted status
        :returns todos
        """
        return Todo.query.filter(
            and_(
                Todo.name.like("%{}%".format(search)),
                Todo.deleted == trash
            )
        ).paginate(page=page, per_page=10)

    @staticmethod
    def get_by_id(todo_id):
        """ Get Todo by id
            :param todo_id: Id of todo
            :return todo data
        """
        return Todo.query.get(todo_id)


class TodoSchema(extensions.MA.ModelSchema):
    """ TodoSchema is schema for object"""

    class Meta:
        """ Meta class for todo schema"""
        model = Todo
