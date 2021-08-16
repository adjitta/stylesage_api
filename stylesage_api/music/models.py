from django.db import models


class Artist(models.Model):
    artist_id = models.IntegerField(primary_key=True)
    artist_name = models.CharField(max_length=150)
    media_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.artist_id}: {self.artist_name}'


class Album(models.Model):
    album_id = models.IntegerField(primary_key=True)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=200)


class Track(models.Model):
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    track_id = models.IntegerField(primary_key=True)
    name_track = models.CharField(max_length=200)
    milliseconds = models.IntegerField()
