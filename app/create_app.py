# -*- coding: utf-8 -*-
""" This module will create app and register all needed extensions"""
from flask import Flask
from .settings import APP_CONFIG as app_config
from .extensions import DB, MIGRATE, MA


def create_app(config_name):
    """Create App From config name"""
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    DB.init_app(app)
    MIGRATE.init_app(app, DB)
    MA.init_app(app)
    return app
