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

    def get(self, request):
        """ Method for retrieving expenses """
        resp = []
        if Album.objects.count():
            alb = Album.objects.get()
            if len(alb.pictures):
                resp = alb.pictures
        return Response(resp)
