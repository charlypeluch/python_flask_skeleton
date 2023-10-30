# -*- coding: utf-8 -*-
from dataclasses import dataclass
from app.database import BaseModel, db

@dataclass
class Users(BaseModel):
    __tablename__ = 'users'

    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255))
    name = db.Column(db.String(50), unique=False, nullable=False)
    lastname = db.Column(db.String(50), unique=False, nullable=False)