from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField()
    born_date = models.CharField()


class Genre(models.Model):
    name = models.CharField(unique=True)


class Style(models.Model):
    name = models.CharField(unique=True)


class Period(models.Model):
    name = models.CharField(unique=True)


class Artwork(models.Model):
    author = models.ForeignKey(Artist, on_delete=models.RESTRICT)
    path = models.CharField()
    title = models.CharField()
    date = models.CharField(null=True)
    style = models.ForeignKey(Style, null=True, on_delete=models.RESTRICT)
    period = models.ForeignKey(Period, null=True, on_delete=models.RESTRICT)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.RESTRICT)
    image_url = models.URLField()


class Collection(models.Model):
    name = models.CharField()
    artworks = models.ManyToManyField(Artwork)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
