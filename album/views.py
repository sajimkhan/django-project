from django.shortcuts import render

# Create your views here.
from .models import Album

def album(request):

    albums = Album.objects.all()

    context = {
        'albums': albums
    }

    return render(request, 'album/index.html', context)