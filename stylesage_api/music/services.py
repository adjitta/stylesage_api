from .models import Artist, Album
from django.db.models import Count


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
    return query_set
