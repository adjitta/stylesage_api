import base64
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate
from .services import fetch_artists, fetch_albums
from .serializer import serialize_artists, serialize_albums
from .services import fetch_albums_by_artist


def get_artist(request):
    artists = fetch_artists()
    artists = serialize_artists(artists)
    return JsonResponse(artists, safe=False)


def get_albums(request):
    if not is_valid_user(request):
        return HttpResponse('Unauthorized', status=401)
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


def is_valid_user(request):
    if 'Authorization' not in request.headers:
        return False
    authorization = request.headers.get('Authorization').split('Basic ')
    if len(authorization) != 2:
        return False
    username, password = base64.b64decode(authorization[1]).decode('utf-8').split(':')
    user = authenticate(username=username, password=password)
    return user is not None
