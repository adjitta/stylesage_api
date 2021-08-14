from .models import Artist, Album


def fetch_artists():
    return Artist.objects.all().order_by('artist_name')


def fetch_albums():
    return Album.objects.all().order_by('album_name')


def fetch_albums_by_artist(artist_id):
    return Album.objects.filter(artist_id=artist_id).order_by('album_name')