# Generated by Django 3.1.2 on 2021-08-16 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='media_url',
            field=models.URLField(max_length=500, null=True),
        ),
    ]