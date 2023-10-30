import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

class Configuration:

    # Application info
    APPLICATION_NAME = "proyect_python_skeleton"
    VERSION = "1.00"

    # JWT Configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'c5c99894c5d44c6b92ab2ce7e484db89')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=2)

    # SQLAlchemy configuration
    DATABASE_USER = os.getenv('DATABASE_USER', 'postgres')
    DATABASE_PASS = os.getenv('DATABASE_PASS', 'mysecretpassword')
    DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
    DATABASE_PORT = os.getenv('DATABASE_PORT', '5432')
    DATABASE_BBDD = os.getenv('DATABASE_BBDD', 'skeleton')
    DATABASE_DRIVER = 'postgresql'

    SQLALCHEMY_DATABASE_URI = f'{DATABASE_DRIVER}://{DATABASE_USER}:{DATABASE_PASS}@' \
                              f'{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_BBDD}'


class ProductionConfiguration(Configuration):
    ENV = 'production'
    DEBUG = False
    TESTING = False

class DevelopmentConfiguration(Configuration):
    ENV = 'development'
    DEBUG = True
    TESTING = False

    # Flask options configuration
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_environment = dict(
    production=ProductionConfiguration,
    development=DevelopmentConfiguration
)