from django.db import models


class Artist(models.Model):
    artist_id = models.IntegerField()
    artist_name = models.CharField(max_length=150)
