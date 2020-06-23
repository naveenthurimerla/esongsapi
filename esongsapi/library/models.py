from django.db import models
from datetime import  datetime

class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=200)
    added_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

class Track(models.Model):
    title  = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, related_name="trackartist", on_delete=models.CASCADE)
    album = models.ForeignKey(Album, related_name="trackalbum", on_delete=models.CASCADE)
    language = models.ForeignKey(Language, related_name="tracklanguage", on_delete=models.CASCADE)
    url = models.URLField(unique=True)
    added_on = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.title