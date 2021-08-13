from .services import fetch_artists, fetch_albums
from django.http import JsonResponse
from .serializer import serialize_artists, serialize_albums


def get_artist(request):
    artists = fetch_artists()
    artists = serialize_artists(artists)
    return JsonResponse(artists, safe=False)


def get_albums_with_songs(request):
    albums = fetch_albums()
    albums = serialize_albums(albums)
    return JsonResponse(albums, safe=False)
