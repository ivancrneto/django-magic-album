""" Module for executing magic album tasks """

from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings
from twython import Twython
from .models import Album, TweetsControl
from django.utils.timezone import now as datetime_now
import random

logger = get_task_logger(__name__)


@shared_task
def update_album():
    """ Fetches Twitter for pictures and adds to album """

    if not Album.objects.count():
        Album.objects.create()
        logger.info('Magic Album just created!')

    album = Album.objects.get()

    twitter = Twython(settings.TWITTER_KEY, settings.TWITTER_SECRET)

    since_id = TweetsControl.get_last_since_id()
    logger.info('Using {} value as since_id for twitter search...'.format(
        since_id))

    # we want tweets with hashtag carnival and with images
    picture_tweets = twitter.search(q='#carnival filter:images', count=100,
                                  since_id=since_id)

    count = 0
    for tweet in picture_tweets['statuses']:
        user = tweet['user']['name']
        # some tweets have more than one picture
        for media in tweet['entities'].get('media', []):
            picture = media['media_url']
            album.add_picture({
                'user': user,
                'picture': picture,
                'created_on': datetime_now().isoformat(),
                'likes': random.randint(0, 100)
            })
            count += 1

    logger.info('{} new pictures added to Magic Album!'.format(count))

    new_since_id = picture_tweets['search_metadata']['max_id_str']
    TweetsControl.objects.create(since_id=new_since_id)
    return True
