# -*- coding: utf-8 -*-
""" This module will declare object of config will used by app mode"""
import os


class BasicConfig:
    """ BasicConfig """
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevConfig(BasicConfig):
    """DevConfig for development mode"""
    DEBUG = True
    ENV = "development"


class ProdConfig(BasicConfig):
    """ProdConfig for production mode"""
    DEBUG = False
    ENV = "production"


class TestingConfig(BasicConfig):
    """TestingConfig for testing mode"""
    DEBUG = True
    ENV = "test"


APP_CONFIG = {
    "testing": TestingConfig,
    "production": ProdConfig,
    "development": DevConfig
}
