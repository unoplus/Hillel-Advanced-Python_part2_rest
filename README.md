# Hillel REST API application

# Setup

## Mandatory steps

1. Install Python3.9+
2. Install Pipenv

## Setup project

Setup environment

```bash
# Create virtual environment
pipenv sync
pipenv shell

# Setup frameworks and tools
djangorestframework==3.13.1
psycopg2-binary==2.9.3
django-environ==0.8.1
celery==5.2.3
django==3.2
django-celery-beat==2.2.1

# formatters to dev
pipenv install --dev black==22.1.0
pipenv install --dev flake8==4.0.1

# Sync virtual environment
pipenv sync
```

## Create django project

```bash
cd src
django-admin startproject config .
```

# Run server

```bash
# Run migrations only on a project setup
python src/manage.py migrate

# Run server
python src/manage.py runserver
```

# Create applications

```bash
# Create application named "posts"
python src/manage.py startapp posts
```

# Code formatters

```bash
# flake8
flake8 .

# isort
isort .

# black
python -m black .
```

# DB connection

```bash
# Create postgesql connection
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "db_name",
        "USER": "db_username",
        "PASSWORD": "password",
        "HOST": "your_hostname",
        "PORT": "your_port",
    }
}
```
