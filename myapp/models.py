from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    annotation = models.TextField()
    author = models.CharField(max_length=255)
    year = models.IntegerField()

