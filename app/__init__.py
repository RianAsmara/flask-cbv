# -*- coding: utf-8 -*-
""" This is just example app to learn how to write best practice
    code in Python Flask Framework
"""
import os
from app.create_app import create_app
from app.blueprint import register_blueprint

APP = create_app(os.getenv("APP_MODE"))

# Register All Function to app
register_blueprint(APP)
