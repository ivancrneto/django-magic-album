from django.shortcuts import render
from magicalbum.models import Album

def album(request):

    context = {}

    try:
        album = Album.objects.get()
    except Album.DoesNotExist:
        pass
    else:
        context.update(album=album)

    return render(request, 'album.html', context)
