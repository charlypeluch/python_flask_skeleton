# -*- encoding: utf-8 -*-
from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def initialize_db(app):
    db.init_app(app)
    migrate.init_app(app, db)


class BaseModel(db.Model):
    """
    This class includes all the common fields in the rest of the database tables.
    """
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(), default=lambda: datetime.utcnow())
    updated_at = db.Column(db.DateTime(), default=lambda: datetime.utcnow(), nullable=True)

    def as_dict(self):
        _dict = {}

        for field in self.__table__.c:
            value = None

            if isinstance(getattr(self, field.name), (datetime, date)):
                value = getattr(self, field.name).isoformat()
            else:
                value = getattr(self, field.name)

            _dict.update({field.name: value})

        return _dict