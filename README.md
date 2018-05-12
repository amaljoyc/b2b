

# chafferr

chafferr is built with [Python][0] using the [Django Web Framework][1].

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

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

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
