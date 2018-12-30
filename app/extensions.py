# -*- coding: utf-8 -*-
""" In this module will declare all extension we needed"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

# All extensions was placed here

DB = SQLAlchemy()
MIGRATE = Migrate()
MA = Marshmallow()
