# -*- coding: utf-8 -*-
"""This module will declare function to help us in app"""
from flask import jsonify, make_response


def create_response(status=200, data=None, msg=""):
    """ create_response is function to create response
        :param status: int is status response default=200
        :param data: object is data to send data default=None
        :param msg: str is massage to tell user about message default=""
        :return response """

    res = jsonify({
        "data": data,
        "msg": msg
    })
    return make_response(res, status)
