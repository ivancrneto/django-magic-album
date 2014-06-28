from django.shortcuts import render

def album(request):
    return render(request, 'album.html', {})
