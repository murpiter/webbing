from django.conf import settings
from django.db import models
from django.utils import timezone


class Dress(models.Model):
    img = models.ImageField()
    price = models.IntegerField()
    description = models.TextField()
    link = models.TextField()

    def add(self):
        self.save()

    def __str__(self):
        return self.description

