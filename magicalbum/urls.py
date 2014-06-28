from django.conf.urls import patterns, url

urlpatterns = patterns(
    'magicalbum.views',

    url(r'', 'album', name='album'),
)
