from django.db import models
from django.db.models import CASCADE
from django.core.urlresolvers import reverse


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genere = models.CharField(max_length=250)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:details', kwargs={'pk':self.pk})

    def __str__(self):
        return self.album_title + '-' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=CASCADE)
    file_type = models.CharField(max_length=150)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
