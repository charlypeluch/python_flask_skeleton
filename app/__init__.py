# -*- encoding: utf-8 -*-
import os
from flask import Flask, jsonify
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

from .database import initialize_db
from app.security import initialize_security

from .controllers import api
from .configuration import config_environment


# class JSONEncoder(json.JSONEncoder):
#     ''' extend json-encoder class'''
#
#     def default(self, o):
#         if isinstance(o, ObjectId):
#             return str(o)
#         if isinstance(o, set):
#             return list(o)
#         if isinstance(o, datetime.datetime):
#             return str(o)
#         return json.JSONEncoder.default(self, o)


# ATTENTION: Because of the way Flask is designed, it normally requires that the configuration be available when
# the application fixes it. The ENV and DEBUG parameters have been previously changed are somewhat special, since
# if they are modified after the application starts, it can behave inconsistently. Furthermore, to ensure that its
# value is read as soon as possible, the recommendation by Frasco is to set its values through the environment
# variables FLASK_ENV and FLASK_DEBUG, respectively. Therefore, whenever possible, we will create these environment
# variables instead of using the previously defined configuration parameters.
environment = os.getenv('APP_ENV', 'development')

def create_app():
    app = Flask('Skeleton Project', instance_relative_config=True)
    configuration = config_environment[environment]
    app.config.from_object(configuration)

    initialize_db(app)
    initialize_security(app)

    # Register Blueprints
    app.register_blueprint(api, url_prefix='/api')

    # Error Handlers
    @app.errorhandler(Exception)
    def handle_error(e):
        response = {"description": str(e), "error": 'InternalError', "status_code": 500}

        if isinstance(e, HTTPException):
            response['status_code'] = e.code
            response['error'] = e.name

        if environment == 'development':
            import traceback
            print(traceback.format_exc())

        return jsonify(response), response['status_code']

    CORS(app)
    return app