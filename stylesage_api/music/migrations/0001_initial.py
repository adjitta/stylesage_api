# Generated by Django 3.1.2 on 2021-08-14 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('album_id', models.IntegerField(primary_key=True, serialize=False)),
                ('album_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artist_id', models.IntegerField(primary_key=True, serialize=False)),
                ('artist_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('track_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name_track', models.CharField(max_length=200)),
                ('milliseconds', models.IntegerField()),
                ('album_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.artist'),
        ),
    ]
