from django.forms.models import model_to_dict


def serialize_artists(artist_model):
    return [model_to_dict(artist) for artist in artist_model]


def serialize_albums(album_models):
    album_dicts = []
    for album_model in album_models:
        album_dict = model_to_dict(album_model)
        track_models = album_model.track_set.only('track_id', 'name_track')
        album_dict['songs'] = [model_to_dict(track_model) for track_model in track_models]
        album_dicts.append(album_dict)
    return album_dicts
