# -*- coding: utf-8 -*-
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
from app.models.user_model import Users

jwt = JWTManager()
flask_bcrypt = Bcrypt()


def initialize_security(app):
    jwt.init_app(app)
    flask_bcrypt.init_app(app)

def auth_user(username, password):
    user = Users.query.filter(username == username).first()

    if user and user.username == username and flask_bcrypt.check_password_hash(user.password, password):
        metadata = generate_meta(user)
        return create_access_token(identity=metadata)

    return None

def validate_user(username):
    user = Users.query.filter(username == username).first()
    return False if user else True

def generate_meta(user):
    meta = {
        "username": user.username,
        "name": user.name,
        "lastname": user.lastname
    }

    return meta

def encrypt_password(password):
    credential = flask_bcrypt.generate_password_hash(password)
    return credential.decode('utf-8')