from django.core.management.base import BaseCommand
from music.models import Artist
from music.scraping import get_media_url


class Command(BaseCommand):
    help = 'Add artist images'

    def add_artist_image_url(self):
        query_set = Artist.objects.filter(media_url__isnull=True)
        for artist in query_set:
            media_url = get_media_url(artist.artist_name)
            self.stdout.write(self.style.SUCCESS(f'Adding {media_url} to {artist.artist_name}'))
            artist.media_url = media_url
            artist.save()

    def handle(self, *args, **options):
        self.add_artist_image_url()
