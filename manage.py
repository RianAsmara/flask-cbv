# -*- coding: utf-8 -*-
""" This file will be used for run our apps with CLI mode"""
from flask_script import Manager
from app import APP as app


MANAGER = Manager(app)


@MANAGER.command
def runserver():
    """This arguments will run your server"""
    app.run(port=8009, debug=True)


if __name__ == '__main__':
    MANAGER.run()
