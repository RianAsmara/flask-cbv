# -*- coding: utf-8 -*-
""" This module is used to handle api request"""

from flask import request
from flask_restplus import Resource, Namespace, fields

from app.helpers import create_response
from .models import Todo, TodoSchema

# API Namespace is namespace instance for api
TODO_API_NAMESPACE = Namespace("", "Todo Namespaces")

# Fields is object just for swagger documentation only
TODO_FIELDS = TODO_API_NAMESPACE.model("TodoModel", {
    "name": fields.String(description="Name of todo", required=True),
    "description": fields.String(description="Todo description")
})


class TodoAPI(Resource):
    """ Todo API is Class Inheritance of Resource """
    todos_schema = TodoSchema(many=True)
    todo_schema = TodoSchema()

    @staticmethod
    def get_all_todo(search, page, trash):
        """ Get All Todo data
        :param search: keyword to search todo
        :param page: number of page will show
        :param trash: status deleted
        :returns todos
        """
        return Todo.get_all_todo(search, page, trash)

    @staticmethod
    def get_by_id(todo_id):
        """ Get Todo by id
            :param todo_id: Id of todo
            :return todo data
        """
        return Todo.get_by_id(todo_id)

    @staticmethod
    def new_todo(data):
        """ Create new todo from request json
            :param data: data from request or dict
            return new todo
        """
        todo = Todo()
        todo.from_request(data)
        return todo


@TODO_API_NAMESPACE.route("/list")
class TodoListAPI(TodoAPI):
    """ TodoListAPI is class inheritance of TodoAPI
    This class will handle request all todo data
    """
    def __init__(self, *args, **kwargs):
        super(TodoListAPI, self).__init__(*args, **kwargs)
        self.page = request.args.get('page', default=1, type=int)
        self.search = request.args.get('search', default="", type=str)
        self.trash = request.args.get('trash', default=False, type=bool)

    @TODO_API_NAMESPACE.doc(params={
        "page": "page number",
        "search": "Keyword for searching todo",
        "trash": "Get data in trash room"})
    def get(self):
        """ This method will handle all get data of list todo"""

        return create_response(
            200,
            self.todos_schema.dump(
                self.get_all_todo(self.search, self.page, self.trash).items
            ).data,
            "Success retrieved data todo")

    @TODO_API_NAMESPACE.expect(TODO_FIELDS)
    def post(self):
        """ This method will handle post data to create new todo data"""

        todo = self.new_todo(request.get_json(force=True))
        todo.save()
        return create_response(
            201,
            self.todo_schema.dump(todo).data,
            "Success create todo data")


@TODO_API_NAMESPACE.route("/<int:todo_id>/detail")
class TodoDetailAPI(TodoAPI):
    """ TodoDetailAPI is class to handle request data detail of todo"""

    def get(self, todo_id):
        """ This method is implement GET request to get detail data todo"""
        return create_response(
            200,
            self.todo_schema.dump(self.get_by_id(todo_id)).data,
            "Success get detail todo")


@TODO_API_NAMESPACE.route("/<int:todo_id>/action")
class TodoActionAPI(TodoAPI):
    """ TodoACtionAPI is class inheritance of TodoAPI
    This class wil have any method to handle change action of todo
    """

    def get(self, todo_id):
        """ This method will handle to restore todo from trash room"""

        todo = self.get_by_id(todo_id)
        todo.restore()
        data = self.todo_schema.dump(todo).data
        return create_response(200, data, "Success restore data todo")

    @TODO_API_NAMESPACE.expect(TODO_FIELDS)
    def put(self, todo_id):
        """ This method will use to handle update data todo"""

        todo = self.get_by_id(todo_id)
        todo.from_request(request.get_json(force=True))
        todo.save()
        return create_response(
            200,
            self.todo_schema.dump(todo).data,
            msg="Success update data todo"
        )

    def patch(self, todo_id):
        """ This method will handle to add todo to trash room"""

        todo = self.get_by_id(todo_id)
        todo.delete()
        return create_response(
            200,
            self.todo_schema.dump(todo).data,
            "Success add todo to trash room"
        )

    def delete(self, todo_id):
        """ This method will delete todo from database"""
        todo = self.get_by_id(todo_id)
        todo.remove()
        return create_response(
            200,
            todo_id,
            msg="Data todo has removed permanently"
        )
