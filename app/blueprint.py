# -*- coding: utf-8 -*-
""" This module is used to register all blueprint in our application"""
from app.todo_app.urls import todo_blueprint


def register_blueprint(app):
    """Register all Blueprint to app"""
    app.register_blueprint(todo_blueprint)
