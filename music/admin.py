
from __future__ import unicode_literals
from django.contrib import admin
from music.models import Album, Song

admin.site.register(Album)
admin.site.register(Song)
