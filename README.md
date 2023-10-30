# Python Project Skeleton

Simple project to integrate ORM and REST

# Features

* Rest Interfaces with Flask
* Database ORM with SQLAlchemy
* JSON Web Token Authentication with Flask-JWT-Extended
* Database Migrations using Alembic


# Pre-requisites

This boilerplate uses `PostgreSQL` as its database, make sure you have instance available. (TIP: Docker)

### DOCKER

If you don't have a posgres instance, dockerize it `postgres:alpine3.18`

```
docker run --name docker_postgresql -e POSTGRES_PASSWORD=mysecretpassword -d skeleton
```

### ENVIRONMENT
It is recommended to create a virtual environment to install dependencies
```
CREATE: python3 -m venv venv
ACTIVATE: source venv/bin/activat3
DEACTIVATE: deactivate
```

### DEPENDENCIES
Install python dependencies

```
pip install -r requirements.txt
```


### SETUP
Configure project environment variables in `configuration.py`

```
# JWT Configuration
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'mysecretjwt')
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=2)

# SQLAlchemy configuration
DATABASE_USER = os.getenv('DATABASE_USER', 'postgres')
DATABASE_PASS = os.getenv('DATABASE_PASS', 'mysecretpassword')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_PORT = os.getenv('DATABASE_PORT', '5432')
DATABASE_BBDD = os.getenv('DATABASE_BBDD', 'skeleton')
```

# Project Commands
```sh
Alembic:
  flask db init       # Initialize database
  flask db migrate    # Generate alembic versions
  flask db upgrade    # Upgrade alembic versions in database
  flask db downgrade  # Downgrade alembic versions in database
  flask db --help     # Show db options

Run:
  python3 manage.py   # Run application
```