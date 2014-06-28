from django.shortcuts import render
from magicalbum.models import Album
from rest_framework.views import APIView
from rest_framework.response import Response

def album(request):

    context = {}

    try:
        album = Album.objects.get()
    except Album.DoesNotExist:
        pass
    else:
        context.update(album=album)

    return render(request, 'album.html', context)


class AlbumAPI(APIView):
    """ Class with views for Album API """

    def get(self, request, format=None):
        """ Method for retrieving expenses """
        resp = []
        return Response(resp)
