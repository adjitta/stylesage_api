from .models import Artist, Album
from django.db.models import Count, Sum, Max, Min


def fetch_artists():
    return Artist.objects.all().order_by('artist_name')


def fetch_albums(fields):
    query_set = Album.objects.all().order_by('album_name')
    query_set = add_annotations(query_set, fields)
    return query_set


def fetch_albums_by_artist(artist_id, fields):
    query_set = Album.objects.filter(artist_id=artist_id).order_by('album_name')
    query_set = add_annotations(query_set, fields)
    return query_set


def add_annotations(query_set, fields):
    if 'track_count' in fields:
        query_set = query_set.annotate(track_count=Count('track'))
    if 'album_duration' in fields:
        query_set = query_set.annotate(album_duration=Sum('track__milliseconds'))
    if 'longest_track_duration' in fields:
        query_set = query_set.annotate(longest_track_duration=Max('track__milliseconds'))
    if 'shortest_track_duration' in fields:
        query_set = query_set.annotate(shortest_track_duration=Min('track__milliseconds'))
    return query_set

