from django.shortcuts import render

from .models import Artist
from rest_framework import viewsets
from .serializers import ArtistSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('artist_name')
    serializer_class = ArtistSerializer
