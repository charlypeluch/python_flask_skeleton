# -*- encoding: utf-8 -*-
import json
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from . import api
from ..database import db
from ..models.user_model import Users


@api.route('/users', methods=['GET'])
@jwt_required()
def get_users():
	response = []
	users = Users.query.all()

	for user in users:
		response.append(user.as_dict())

	return jsonify(response)

# @api.route('/users', methods=['POST'])
# @jwt_required()
# def post_users():
# 	response = []
# 	data = request.json
#
# 	user = Users(**data)
# 	user.save()
#
# 	return json.dumps(response)


@api.route('/users', methods=['PUT'])
@jwt_required()
def put_users():
	response = {}
	data = request.json

	user = Users.query.filter_by(id=data.get('id')).first()

	if user:
		for key, value in data.items():
			setattr(user, key, value)

		db.session.commit()
		response = user.as_dict()

	return json.dumps(response)


@api.route('/users', methods=['DELETE'])
@jwt_required()
def delete_users():
	response = {}
	user_id = request.args.get('id', None)

	Users.query.filter_by(id=user_id).delete()
	db.session.commit()

	return json.dumps(response)