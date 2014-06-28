django-magic-album
==================

About
-----
A simple django app that picks pictures from Twitter and posts on Facebook

Instalation
----------

Download from https://github.com/ivancrneto/django-magic-album/archive/master.zip
Run the following command to install the app in your virtualenv

    $ python setup.py install

In your Django `settings` module add the following to `INSTALLED_APPS`

    'magicalbum'

And the setting `MAGICALBUM_TASKS_BROKER` especifying the sending/receiving
    messages broker (Redis, RabbitMQ, etc). Make sure to install the properly
    broker packages. For example, for RabbitMQ:

    MAGICALBUM_TASKS_BROKER = 'amqp://guest:**@localhost:5672/'

Add your Twitter API key and secret to the project settings:

    TWITTER_KEY = '06CUabtdjfPHvZ8IfsQ7iw'
    TWITTER_SECRET = 'BJL7ujCUMmEIRF8wAI5tDjhZa6n2dV1FROjd4dZ1yc4'

Run `python manage.py migrate magicalbum`.

To see the album page, add the following to your urls setting:

    url(r'^magicalbum/', include('magicalbum.urls', namespace='magicalbum')),
