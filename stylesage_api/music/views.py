from .services import fetch_artists, fetch_albums
from django.http import JsonResponse
from .serializer import serialize_artists, serialize_albums
from .services import fetch_albums_by_artist


def get_artist(request):
    artists = fetch_artists()
    artists = serialize_artists(artists)
    return JsonResponse(artists, safe=False)


def get_albums_with_songs(request):
    if request.GET.get('artist_id'):
        artist_id = request.GET.get('artist_id')
        artist_album = fetch_albums_by_artist(artist_id)
        artist_album = serialize_albums(artist_album)
        return JsonResponse(artist_album, safe=False)
    else:
        albums = fetch_albums()
        albums = serialize_albums(albums)
        return JsonResponse(albums, safe=False)
