from django.conf.urls import patterns, url
from magicalbum.views import AlbumAPI

urlpatterns = patterns(
    'magicalbum.views',

    url(r'^$', 'album', name='album'),
    url(r'^api/$', AlbumAPI.as_view(), name='api'),
)
