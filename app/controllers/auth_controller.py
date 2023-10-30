# -*- encoding: utf-8 -*-
from flask import request, jsonify
from . import api
from ..database import db
from ..models.user_model import Users
from ..security import auth_user, validate_user, encrypt_password


@api.route("/auth/login", methods=["POST"])
def login():
    data = request.json

    if data.get('username') and data.get('password'):
        token = auth_user(data.get('username'), data.get('password'))

        if token:
            return jsonify({"token": token})

    return jsonify({"message": "Invalid username or password"}), 401


@api.route("/auth/register", methods=["POST"])
def register():
    data = request.json

    if validate_user(data.get('username')):
        password = encrypt_password(data.get('password'))

        user = Users(**data)
        user.password = password

        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"})

    return jsonify({"message": "Error in auth register"}), 500
