from django.db import models
from datetime import datetime


class Language(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
        indexes = [
            models.Index(fields=['name'], name='idx_language_name'),
        ]

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=200)
    logo_url = models.URLField(null=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        indexes = [
            models.Index(fields=['name'], name='idx_company_name'),
        ]

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    image_url = models.URLField(null=True)

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"
        indexes = [
            models.Index(fields=['name'], name='idx_artist_name'),
        ]

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
        indexes = [
            models.Index(fields=['name'], name='idx_genre_name'),
        ]

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=200)
    composed_by = models.ManyToManyField(
        Artist, related_name="album_composed_by")
    released_by = models.ManyToManyField(
        Company, related_name="album_composed_by")
    genre = models.ForeignKey(
        Genre, related_name="album_genre", on_delete=models.CASCADE)
    language = models.ForeignKey(
        Language, related_name="album_language", on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    cover_url = models.URLField(null=True)
    casting = models.ManyToManyField(Artist, related_name="album_casting")
    released_on = models.DateTimeField(default=datetime.now)
    added_on = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"
        indexes = [
            models.Index(fields=['name'], name='idx_album_name'),
        ]

    def __str__(self):
        return self.name


class Track(models.Model):
    title = models.CharField(max_length=300)
    alt_title = models.CharField(max_length=300)
    artist = models.ManyToManyField(Artist, related_name="track_artist")
    album = models.ForeignKey(
        Album, related_name="track_album", on_delete=models.CASCADE)
    url = models.URLField(unique=True)
    rating = models.IntegerField(default=0)
    length = models.FloatField(default=0)
    added_on = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "Track"
        verbose_name_plural = "Tracks"
        indexes = [
            models.Index(fields=['title'],
                         name='idx_track_title'),
        ]

    def __str__(self):
        return self.title


class Lyric(models.Model):
    track = models.ForeignKey(
        Track, related_name="lyric_track", on_delete=models.CASCADE)
    author = models.ManyToManyField(Artist, related_name="lyric_author")
    description = models.TextField()

    class Meta:
        verbose_name = "Lyric"
        verbose_name_plural = "Lyrics"

    def __str__(self):
        return self.track
