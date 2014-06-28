from celery import Celery
from celery.schedules import crontab
import os

app = Celery('magicalbum', broker=os.environ['MAGICALBUM_TASKS_BROKER'])
app.conf.CELERYBEAT_SCHEDULE = {
    'poll-twitter-photos-every-twenty-minutes': {
        'task': 'tasks.get_twitter_photos',
        'schedule': crontab(),
    },
}

@app.task
def get_twitter_photos():
    return True
