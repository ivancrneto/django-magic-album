django-magic-album
==================

About
-----
A simple django app that picks pictures from Twitter and posts on Facebook

Instalation
----------

- Download from https://github.com/ivancrneto/django-magic-album/archive/master.zip
- Run the following command to install the app in your virtualenv

    $ python setup.py install

- In your Django `settings` module add the following to `INSTALLED_APPS`

    'magicalbum'

- And the `MAGICALBUM_TASKS_BROKER` environment variable for sending/receiving
    messages broker (Redis, RabbitMQ, etc). Make sure to install the properly
    broker packages. For example, for RabbitMQ:

    os.environ.setdefault('MAGICALBUM_TASKS_BROKER',
    'amqp://guest:**@localhost:5672/')

    or:

    $ export MAGICALBUM_TASKS_BROKER='amqp://guest:**@localhost:5672/'
