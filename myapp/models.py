from django.db import models


class Directors(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()


class Genres(models.Model):
    name = models.CharField(max_length=100)


class Films(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    directors = models.ManyToManyField(Directors)
    genres = models.ManyToManyField(Genres)


class Afisha(models.Model):
    date = models.DateField()
    films = models.ManyToManyField(Films)
