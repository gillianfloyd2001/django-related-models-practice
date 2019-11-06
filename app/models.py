from django.db import models


class Album(models.Model):
    title = models.TextField()
    artist_name = models.TextField()


class Song(models.Model):
    title = models.TextField()
    seconds = models.FloatField()
    album = models.ForeignKey(Album, on_delete=models.PROTECT)

    def formatted_duration(seconds):
        minutes = seconds // 60
        return str(f"{minutes}:00")
