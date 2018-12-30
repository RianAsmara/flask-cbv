# -*- coding: utf-8 -*-
""" Create todo blueprint here"""
import os
from flask import Blueprint


TODO_BLUEPRINT = Blueprint(
    "todo_bp",
    __name__,
    url_prefix="/api/{}/todos".format(os.getenv("API_VERSION")))
