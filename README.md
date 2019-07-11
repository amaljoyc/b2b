

# b2b

b2b is built with Python using the Django Web Framework.

## Demo

You can find a video walk-through of the project under the directory - [demo](demo) 

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv chafferr`
    2. `$ . b2b/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

To run the project, go to src,

    python3 manage.py runserver

To go to db, go under src and issue,

    python manage.py dbshell
