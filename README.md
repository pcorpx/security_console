# Security console website

This website based on Django and serves as a learning project. It presents information about visitors and their visits in repository from database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development.

### Prerequisites

Clone project to your local machine:

`git clone ...`

It's necessary to have right environment:

* pytz == 2017.2
* django==1.11.*
* psycopg2-binary==2.8.*

You may use requirements file to prepare your environment:

`pip install -r requirements.txt`

Also you should provide your environment with the right sef of variables and their values:

* __SECRET_KEY__
  *The value is used for generating cryptographic signature. It is critical data and mustn't be in public*
* __DB_ENGINE__ 
  *The value defines database backend for the project*

* __DB_HOST__
  *The value contains address of a host used for connecting to the database*

* __DB_PORT__
  *The value contains number of a port used for connecting to the database*

* __DB_NAME__
  *The value contains database name*

* __DB_USER__
  *The value contains name of a user for connecting to the database*

* __DB_PASSWORD__
  *The value contains password of a user for connecting to the database.  It is critical data and mustn't be in public*

You may put those variables with values in ~/.bash_profile script if your operation system is Linux as follows: `export DB_ENGINE=django.db.backends.postgresql_psycopg2` or keep it in .env file in the working directory of the project.

### Installation

To start project running enter following command being in project directory:

`python manage.py runserver 0.0.0.0:8000`

## Tests

Use your browser to follow this address: <127.0.0.1:8000>