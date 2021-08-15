from django.forms.models import model_to_dict


def serialize_artists(artist_model):
    return [model_to_dict(artist) for artist in artist_model]


def serialize_albums(album_models, fields):
    album_dicts = []
    for album_model in album_models:
        album_dict = model_to_dict(album_model)
        track_models = album_model.track_set.all()
        if 'songs' in fields:
            album_dict['songs'] = [model_to_dict(track_model) for track_model in track_models]
        if 'track_count' in fields:
            album_dict['track_count'] = album_model.track_count
        if 'album_duration' in fields:
            album_dict['album_duration'] = album_model.album_duration
        if 'longest_track_duration' in fields:
            album_dict['longest_track_duration'] = album_model.longest_track_duration
        if 'shortest_track_duration' in fields:
            album_dict['shortest_track_duration'] = album_model.shortest_track_duration
        album_dicts.append(album_dict)
    return album_dicts
