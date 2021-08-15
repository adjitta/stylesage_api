from .services import fetch_artists, fetch_albums
from django.http import JsonResponse
from .serializer import serialize_artists, serialize_albums
from .services import fetch_albums_by_artist


def get_artist(request):
    artists = fetch_artists()
    artists = serialize_artists(artists)
    return JsonResponse(artists, safe=False)


def get_albums_with_songs(request):
    fields = get_fields(request)
    if request.GET.get('artist_id'):
        artist_id = request.GET.get('artist_id')
        albums = fetch_albums_by_artist(artist_id, fields)
    else:
        albums = fetch_albums(fields)

    albums = serialize_albums(albums, fields)
    return JsonResponse(albums, safe=False)


def get_fields(request):
    fields = request.GET.get('fields', '').split(',')
    fields = [field.strip() for field in fields]
    return fields
