# -*- coding: utf-8 -*-
""" This module will use to add and url role if needed"""
import os
from flask_restplus import Api

from .blueprint import TODO_BLUEPRINT as todo_blueprint
from .apis import TODO_API_NAMESPACE as todo_api_namespace


TODO_API = Api(todo_blueprint, version=os.getenv("API_VERSION"))
TODO_API.add_namespace(todo_api_namespace)
