# -*- encoding: utf-8 -*-
from flask import Blueprint
api = Blueprint('api', __name__)

from . import auth_controller
from . import users_controller
