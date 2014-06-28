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

    'south',
    'rest_framework',
    'magicalbum',

We use Django Rest Framework for the album API.

Add the following to your project `__init__.py`:

    from __future__ import absolute_import
    from celery import Celery
    from celery.schedules import crontab
    from django.conf import settings
    import os

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '<yourproject>.settings')
    celery = Celery('magicalbum', broker=settings.MAGICALBUM_TASKS_BROKER)
    celery.config_from_object('django.conf:settings')
    celery.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

    celery.conf.CELERYBEAT_SCHEDULE = {
        'poll-twitter-photos-every-twenty-minutes': {
            'task': 'magicalbum.tasks.update_album',
            'schedule': crontab(minute='*/20'),
        },
    }

And the setting `MAGICALBUM_TASKS_BROKER` especifying the sending/receiving
    messages broker (Redis, RabbitMQ, etc). Make sure to install the properly
    broker packages. For example, for RabbitMQ:

    MAGICALBUM_TASKS_BROKER = 'amqp://guest@localhost:5672/'

Add your Twitter API key and secret to the project settings:

    TWITTER_KEY = '06CUabtdjfPHvZ8IfsQ7iw'
    TWITTER_SECRET = 'BJL7ujCUMmEIRF8wAI5tDjhZa6n2dV1FROjd4dZ1yc4'

Run `python manage.py syncdb`.

To see the album page, add the following to your urls setting:

    url(r'^magicalbum/', include('magicalbum.urls', namespace='magicalbum')),

In production, run the scheduler (beat) and the task workers:

    $ celery -A <yourproject> beat
    $ celery -A <yourproject> worker -l info

To run them as daemons, check Celery documentation in http://celery.readthedocs.org
